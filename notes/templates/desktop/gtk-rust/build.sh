#!/bin/bash

# prepare
cargo add gtk

# to run
cargo build
cp -vf src/main.glade ./target/debug/

# using built binary
#./target/debug/gtk_template

# or using cargo
#cargo run

# and to clean target
#cargo clean

