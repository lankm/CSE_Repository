struct Position {
    time: u64,
    pos: [i128;3], // x, y, z
    vel: [i64;3],
}
// struct Rotation {
//     rot: [i32;4], // quaternion
//     time: u64,
//     rot_vel: [i32;4],
// }

impl Position {
    fn new() -> Position {
        Position { time:0, pos:[1,2,3], vel:[1,1,1] }
    }

    fn update(&mut self, time: &u64) {
        let dt = time - self.time;

        for i in 0..3 {
            self.pos[i] = self.pos[i] + i128::from(self.vel[i]) * i128::from(dt)
        }

        self.time = self.time + dt
    }

    fn accelerate(&mut self, &acc: &[i64;3]) {
        for i in 0..3 {
            self.vel[i] = self.vel[i] + acc[i]
        }
    }
}

fn main() {
    let mut p = Position::new();
    let num: u64 = 10;
    p.update(&num);
    println!("{}", p.pos[1]);
}
