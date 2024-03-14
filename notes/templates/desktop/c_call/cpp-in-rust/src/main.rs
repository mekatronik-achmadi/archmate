#[cxx::bridge(namespace = "org::pwr")]
mod ffi {
    unsafe extern "C++" {
        include!("cxxrust/src/main.rs.h");

        //type Pwr;

        //fn power(x: u16, y: u16) -> u16;
    }
}

fn main() {
    //let val = ffi::power(4, 3);

    //println!("Rust from C++: {}",val);
}
