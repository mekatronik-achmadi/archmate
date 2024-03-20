# Qt C++

Create build folder and Makefile

```sh
mkdir -p build/
cd build/

qmake-qt5 ../
```

to also check using CLazy

```sh
cmake-qt5 ../ \
-spec linux-clang \
QMAKE_CXX="clazy"
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

