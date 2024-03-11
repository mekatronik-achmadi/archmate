extern "C" {
    fn calc_pwr(x: u8, y: u8) -> u16;
}

fn main(){
    // must use unsafe keyword
    unsafe{
        println!("Power C in Rust: {}",calc_pwr(4, 3));
    }
}