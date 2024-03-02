from math import cos, sin, pi, radians

def sign(num):
    if num < 0:
        return "-"
    else:
        return "+"

class Quaternion:
    def __init__(self, r, i, j, k):
        self.r = r
        self.i = i
        self.j = j
        self.k = k

    def __mul__(self, other):
        r1 = self.r
        i1 = self.i
        j1 = self.j
        k1 = self.k

        r2 = other.r
        i2 = other.i
        j2 = other.j
        k2 = other.k

        r = r1*r2 - i1*i2 - j1*j2 - k1*k2
        i = r1*i2 + i1*r2 + j1*k2 - k1*j2
        j = r1*j2 - i1*k2 + j1*r2 + k1*i2
        k = r1*k2 + i1*j2 - j1*i2 + k1*r2
        
        return Quaternion(r, i, j, k)
    
    def __abs__(self):
        return (self*self.inv()).r**(1/2)
    
    def unit(self):
        return Quaternion(1/abs(self),0,0,0)*self
    
    def inv(self):
        r = self.r
        i = self.i
        j = self.j
        k = self.k

        return Quaternion(r, -i, -j, -k)
    
    def __str__(self):
        r = self.r
        i = self.i
        j = self.j
        k = self.k
        return f'{r} {sign(i)} {abs(i)}i {sign(j)} {abs(j)}j {sign(k)} {abs(k)}k'
    def __repr__(self):
        r = self.r
        i = self.i
        j = self.j
        k = self.k
        return f'{r} {sign(i)} {abs(i)}i {sign(j)} {abs(j)}j {sign(k)} {abs(k)}k'

def main():
    theta = radians(180)/2
    pos = [cos(theta)] + [sin(theta),0,0]

    q1 = Quaternion(*pos)
    q2 = Quaternion(1,1,1,1).unit()

    print(q1*q2*q1.inv())

if __name__ == "__main__":
    main()
