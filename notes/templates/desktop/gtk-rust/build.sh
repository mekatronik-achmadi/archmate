#!/bin/bash

# to run
#./target/debug/gtk_template

cargo build
cp -vf src/main.glade ./target/debug/

