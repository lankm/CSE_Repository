# Design Doc
The purpose of this document is to define a language agnostic definition of an object-like structure which can be used in newtonian physics applications. A key point of these definitions is the idea of newtonian relativity. AKA absolute position and velocity should not be known at any point, only relative position and velocity. Additionally for performance concerns, calculations of objects are not forced to be along fixed timesteps. Instead physics calculations can be ignored if there is no acceleration and no requests for related data.

Both postition and rotation are based on the center of mass.

Type definitions generally follow rust syntax.

If not explicitly stated, every integer number is treated as if the last fourth of bits are the decimal components. Ex: u64 -> u48 integer component and u16 decimal component. Some decision for data-type utilize how this applies to multiplication to avoid a bitshift and loss of precision.

If not explicitly stated, all units are in SI standard units. Generlaly this means that the representation of 1 from the above section corelates with 1 meter.

## Translation

```
Struct
- Public
- Private
    - pos: [i64:3]  // x, y, z position. max: ±940au, min: 0.015mm
    - vel: [i32:3]  // x, y, z velocity. max: ±8,338,608m/s, min: 3.9mm/s
    - time: u32     // time of last update. max: 97d, min: 3.9ms
Methods
- Public
    - get_dist()    // relative L2 distance; calls update()
    - get_vel()     // relative velocity
    - acc()         // changes vel; calls update()
- Private
    - update()      // updates position with linear interpolation
```

Note on the time variable. This should be implemented with some form of global time. Additionally because the max time is not 'unbelevably' large, it will overflow. An occasional update to objects that are at the trailing end of the 'time circle' should must be done to keep consistancy.

retrieving current acceleration and higher derivitive terms must be calculated over time from a calling class because acceleration does not persist. Keeping track of acceleration and higher derivitive terms would compramize the performance of the system by adding variables to keep track of. These calculations are simple and can be limited to scenarios that require them.

Multithreading and concurrency details still need to be figured out.

## Rotation

```
Struct
- Public
- Private
    - ori: [i32:4]  // current orientation. integers represent range of -1 to 1
    - rot: [i32:3]  // rotation vector. i j k
    - vel: i32      // counterclockwise rotation rate. theta/sec
    - time: u32     // time of last update. holdover from Translation
Methods
- Public
    - get_ori()     // gets current rotation quaternion. calls update()
    - get_rot()     // gets rotation vector
    - get_vel()     // gets rotation velocity
- Private
    - update()      // updates ori by rotating around rot with velocity vel
```

Rotation follows similar principles of translation. ori is a transformation quaternion in the form **ori = cos(t) + sin(t)(bi + cj + dk)** where t is fixed. This rotates any given point around an axis through the center of mass to an initial position. rot is of the form (bi + cj+ dk) and is the current vector which there is velocity around. To calculate the rotation quaternion, calculate **q = cos(vel\*time) + sin(vel\*time)\*rot**. To update ori simple left multiply: **ori = q\*ori**

Fixed point arithmatic is done similarly to the Translation class but due to the requirement of multiplying two quaternions to update ori, small differences are made. If the max value (representing 1) is the same as the int max, squaring and bitshifting does not return the same value (1*1 / 1). Instead the max value is a single bit in the most significant signed bit. Ex: 0100 0000 = 1, 11000000 = -1. This is done because 0111 1111 \* 0111 1111 >> 7 = 0111 1110. Small precision errors should be avoided to avoid having to check when they accumulate. Additionally integer division is floor division which loses more information than rounding. The process should be multiplying two 32 bit numbers in a 64 bit register, add ~1/2 then bitshift. This process has more precision (for most rotations) than floating point numbers, and faster. With basic testing, about 50% faster on a Ryzen 3600.
```
// C code example
uint64_t num = 1<<30;
uint64_t res = (num*num + (uint64_t)(1<<29)) >> 30;
```


The intermediate axis theorem is not considered at this time.

gyroscopic precession is not considered at this time.

## Object
```
Struct
- Public
    - translation: Translation      //
    - mass: u32                     // total mass
    - rotation: Rotation            //
    - moi: [u32:3]                  // moment of inertia
- Private


Methods
- Public
- Private
```

This encapsulates both the current translation and current rotation of an object. An Object can be pushed and rotated with forces and torques.
