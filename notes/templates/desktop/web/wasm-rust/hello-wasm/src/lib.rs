mod utils;

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn power() {
    let x: u8 = 4;
    let y: u8 = 3;

    let mut res = 1;
    let mut i = 0;
    while i<y {
        res = res * x;
        i = i + 1;
    }

    alert("Rust WASM: {res}");
}
