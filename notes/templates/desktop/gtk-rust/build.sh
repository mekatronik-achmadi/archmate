#!/bin/bash

# to run

# using built binary
#./target/debug/gtk_template

# or using cargo
#cargo run

# and to clean target
#cargo clean

cargo build
cp -vf src/main.glade ./target/debug/

