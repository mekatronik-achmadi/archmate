# Rust on Arduino

## Sources

- https://github.com/avr-rust/blink
- https://github.com/avr-rust/ruduino

## Setup Rustup

```sh
curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs -o ~/rust.sh

bash ~/rust.sh -y --no-modify-path
```

```sh
source ~/.cargo/env

rustup override set nightly
rustup component add rust-src
rustup component add rust-analyzer

# changing default channel
#rustup default stable
#rustup default nightly
```

## Project

```sh
source ~/.cargo/env
export AVR_CPU_FREQUENCY_HZ=16000000
rustup override set nightly

cargo new blink
cd blink/

cargo add ruduino \
--git https://github.com/avr-rust/ruduino
```

```sh
echo '{
  "arch": "avr",
  "cpu": "atmega328p",
  "data-layout": "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8",
  "env": "",
  "executables": true,
  "linker": "avr-gcc",
  "linker-flavor": "gcc",
  "linker-is-gnu": true,
  "llvm-target": "avr-unknown-unknown",
  "os": "unknown",
  "position-independent-executables": false,
  "exe-suffix": ".elf",
  "eh-frame-header": false,
  "pre-link-args": {
    "gcc": ["-mmcu=atmega328p"]
  },
  "late-link-args": {
    "gcc": ["-lgcc", "-lc"]
  },
  "target-c-int-width": "16",
  "target-endian": "little",
  "target-pointer-width": "16",
  "vendor": "unknown",
  "panic-strategy": "abort"
}' | tee avr-atmega328p.json
```

example of **src/main.rs**

```rust
#![no_std]
#![no_main]

use ruduino::Pin;
use ruduino::cores::current::port;

#[no_mangle]
pub extern fn main(){
    port::B5::set_output();

    loop {
        port::B5::set_high();
        ruduino::delay::delay_ms(200);
        port::B5::set_low();
        ruduino::delay::delay_ms(200);
    }
}
```

## Test Build

Build binary crates

```sh
source ~/.cargo/env
export AVR_CPU_FREQUENCY_HZ=16000000
rustup override set nightly

cargo +nightly build --release \
--target ./avr-atmega328p.json \
-Z build-std=core
```

Convert ELF to Intel HEX

```sh
avr-objcopy -O ihex \
target/avr-atmega328p/release/blink.elf \
target/avr-atmega328p/release/blink.hex
```
