# WASM C++

## Install

```sh
sudo pacman -S gcc emscripten nodejs
```

## Test the C source

```sh
gcc -o main main.c pwr.c -lm

./main 4 3
```

## Compile into WASM

load profile if not already

```sh
source /etc/profile.d/emscripten.sh
```

Compile to both html, javascript, and WASM

```sh
emcc main.c pwr.c -o main.html
```

**NOTE:** WASM Module compilation generated in **/home/achmaday/.emscripten_cache/**

## Run Server to Test

Install necessary NodeJS modules

```sh
npm install
```

Run the server

```sh
node run.js
```

Open in webbrowser

```sh
firefox http://localhost:8001/
```

