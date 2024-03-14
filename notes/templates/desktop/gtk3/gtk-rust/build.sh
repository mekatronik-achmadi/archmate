#!/bin/bash

# prepare
cargo add gtk

# to run
cargo build --release
cp -vf src/main.glade ./target/release/

ls ./target/release/gtk_template

cargo run --release

# and to clean target
#cargo clean

