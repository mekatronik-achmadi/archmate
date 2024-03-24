# Compiling

## Using Makefile

create compile_commands.json

```sh
bear -- make
```

clean and compile binary

```sh
make clean
make all
```

## Using CMake

not tested for now

## Run binary

Unset loaded library for memleak checker

```sh
unset LD_PRELOAD
```

run binary

```sh
./.build/ugfx-x11
```

