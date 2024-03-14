extern crate cc;

fn main(){
    println!("cargo:rustc-link-arg=-lm");
    cc::Build::new()
        .file("src/pwr.c")
        .compile("pwr");
}
