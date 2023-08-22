#[allow(dead_code)]
struct Coordinates {
    x: i32,
    y: i32,
    z: i32,
}
#[allow(dead_code)]
fn struct_ex() {
    let _my_coords = Coordinates {
        x:0,
        y:0,
        z:0,
    };
}

fn function(x: &i32) {
    println!("{x}");
}

fn main() {
    let mut x: i32 = 5;
    function(&x);
    x += 1;
    println!("{x}");
}
