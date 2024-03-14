extern crate bindgen;

use std::env;
use std::path::PathBuf;

fn main() {
    println!("cargo:rustc-link-arg=-L./");
    println!("cargo:rustc-link-arg=-lpwr");

    let bindings = bindgen::Builder::default()
        .header("src/pwr.h")
        .clang_arg("-std=c++11")
        .clang_arg("-x")
        .clang_arg("c++")
        .parse_callbacks(Box::new(bindgen::CargoCallbacks))
        .generate()
        .expect("Unable to generate bindings");

    let out_path = PathBuf::from(env::var("OUT_DIR").unwrap());

    bindings
        .write_to_file(out_path.join("bindings.rs"))
        .expect("Failed write bindings");
}
