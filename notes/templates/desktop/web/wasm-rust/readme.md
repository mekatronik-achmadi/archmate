# WASM Rust

## Install

```sh
sudo pacman -S jq nodejs npm rust-wasm wasm-pack wasm-bindgen
```

## Template

A basic template to be used with Cargo Generate can be found in [Github](https://github.com/rustwasm/wasm-pack-template)

## Compile into WASM

Build using WASM-Pack tool (requires internet to download modules)

```sh
wasm-pack build
```

The result will generated in **pkg/** folder.

## Setup Server to Test

Ge NodeJS WASM App modules

```sh
npm init wasm-app www
cd www/
```

set the content of main script **index.js**:

```js
import * as wasm from "hello-wasm-pack";

wasm.power();
```

then install necessary modules inside wasm-app (www):

```sh
npm install
```

add previous dependencies using command:

```sh
jq '
."dependencies"={"hello-wasm":"file:../pkg"}
' package.json > temp.json

mv temp.json package.json
```


and run install again:

```sh
npm install
```

## Run Server

```sh
npm run start
```

And it failed at NPM server start, LMAO
