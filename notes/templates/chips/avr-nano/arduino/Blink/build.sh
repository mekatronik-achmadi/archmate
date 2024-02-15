#!/bin/bash

# arduino-cli core install arduino:avr
# arduino-cli compile --build-path ./build --only-compilation-database --fqbn arduino:avr:nano

arduino-cli compile --build-path ./build --export-binaries --fqbn arduino:avr:nano

