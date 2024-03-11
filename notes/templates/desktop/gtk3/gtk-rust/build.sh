#!/bin/bash

# prepare
cargo add gtk

# to run
cargo build
cp -vf src/main.glade ./target/debug/

ls ./target/debug/gtk_template

cargo run

# and to clean target
#cargo clean

