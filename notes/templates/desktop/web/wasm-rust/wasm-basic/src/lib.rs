use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn power(x: u16, y: u16) {
    let mut res: u16 = 1;
    let mut i: u16 = 0;

    while i<y {
        res = res * x;
        i = i + 1;
    }

    unsafe{
        alert(&format!("Power Rust: {}", res));
    }
}

