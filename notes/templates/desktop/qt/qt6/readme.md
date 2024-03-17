# Qt C++

Create build folder and Makefile

```sh
mkdir -p build/
cd build/

qmake6 ../
```

Generate compile_commands.json

```sh
bear -- make
cp -vf compile_commands.json ../
```

Clean and build binary

```sh
make Clean
make all
```

Run the binary

```sh
./gui
```

