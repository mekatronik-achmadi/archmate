# Rust on Arduino

## Setup Rustup

```sh
curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs -o ~/rust.sh

bash ~/rust.sh -y \
--profile minimal \
--no-modify-path
```

```sh
source ~/.cargo/env

rustup override set nightly-2022-06-05
rustup default nightly-2022-06-05
```

## Project

```sh
source ~/.cargo/env
export AVR_CPU_FREQUENCY_HZ=16000000
export CARGO_HTTP_CHECK_REVOKE=false

cargo new blink
cd blink/

cargo add ruduino \
--git https://github.com/avr-rust/ruduino \
--branch master
```

```sh
echo '{
  "arch": "avr",
  "atomic-cas": false,
  "cpu": "atmega328p",
  "data-layout": "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8",
  "eh-frame-header": false,
  "env": "",
  "exe-suffix": ".elf",
  "executables": true,
  "late-link-args": {
    "gcc": [
      "-lgcc"
    ]
  },
  "linker": "avr-gcc",
  "linker-flavor": "gcc",
  "linker-is-gnu": true,
  "llvm-target": "avr-unknown-unknown",
  "max-atomic-width": 8,
  "no-default-libraries": false,
  "os": "unknown",
  "pre-link-args": {
    "gcc": [
      "-mmcu=atmega328p",
      "-Wl,--as-needed"
    ]
  },
  "target-c-int-width": "16",
  "target-endian": "little",
  "target-pointer-width": "16",
  "vendor": "unknown"
}' | tee avr-atmega328p.json
```

```sh
echo '#[no_mangle]
pub extern fn main(){
}' | tee src/main.rs
```

## Test Build

```sh
source ~/.cargo/env
export AVR_CPU_FREQUENCY_HZ=16000000

cargo build -Z build-std=core --target avr-atmega328p.json --release
```

