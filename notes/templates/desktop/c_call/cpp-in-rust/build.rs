fn main() {
    cxx_build::bridge("src/main.rs")
        .file("src/pwr.cpp")
        .flag_if_supported("-std=c++14")
        .compile("cxxrust");

    println!("cargo:rerun-if-changed=src/main.rs");
    println!("cargo:rerun-if-changed=src/pwr.cpp");
    println!("cargo:rerun-if-changed=src/pwr.h");
}
