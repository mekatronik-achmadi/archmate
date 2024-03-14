#!/bin/bash

# prepare
cargo add fltk

# to run
cargo build --release

ls ./target/release/fltk_template

cargo run

# and to clean target
#cargo clean

