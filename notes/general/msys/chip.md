# Chip Tools

## AVR Compiler

```sh
pacman -S $(echo "
mingw-w64-x86_64-avr-binutils
mingw-w64-x86_64-avr-gcc
mingw-w64-x86_64-avr-libc
mingw-w64-x86_64-avrdude
")
```

## ARM Compiler

```sh
pacman -S $(echo "
mingw-w64-x86_64-arm-none-eabi-binutils
mingw-w64-x86_64-arm-none-eabi-gcc
mingw-w64-x86_64-arm-none-eabi-newlib
")
```

## Python Serial Plot

```sh
pacman -S $(echo "
mingw-w64-x86_64-python-numpy
mingw-w64-x86_64-python-pyserial
mingw-w64-x86_64-python-matplotlib
")
```
