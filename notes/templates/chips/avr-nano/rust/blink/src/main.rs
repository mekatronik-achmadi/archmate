#![no_std]
#![no_main]

use ruduino::Pin;
use ruduino::legacy::serial;
use ruduino::cores::current::port;

#[no_mangle]
pub extern fn main(){
    const CPU_FREQ_HZ: u64 = 16_000_000;
    const BAUD: u64 = 115200;
    const UBRR: u16 = (CPU_FREQ_HZ/16/BAUD -1) as u16;

    port::B5::set_output();
    serial::Serial::new(UBRR)
        .character_size(serial::CharacterSize::EightBits)
        .mode(serial::Mode::Asynchronous)
        .parity(serial::Parity::Disabled)
        .stop_bits(serial::StopBits::OneBit)
        .configure();

    loop {
        port::B5::set_high();
        ruduino::delay::delay_ms(200);
        port::B5::set_low();
        ruduino::delay::delay_ms(200);

        for &chr in b"AVR Rust OK\n"{
            serial::transmit(chr);
        }
    }
}

