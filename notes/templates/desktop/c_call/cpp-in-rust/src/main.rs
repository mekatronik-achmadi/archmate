mod ffi {
    // bindings.rs was auto generated
    // the C++ class converten to Rust 'impl'
    include!(concat!(env!("OUT_DIR"), "/bindings.rs"));
}

fn main() {
    unsafe{
        let mut rwp = ffi::Pwr::new();
        let val = ffi::Pwr::power(&mut rwp, 4, 4);

        println!("Power Rust from C++: {}",val);
    }
}
