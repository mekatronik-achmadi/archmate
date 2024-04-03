# Run NodeJr

## Setup electron from ArchLinux

Install Electron package

```sh
sudo pacman -S electron22 trash-cli
```

## Setup electron from NPM (Recommended)

Install Electron module

```sh
npm install electron
```

## Run main script

### Using Archlinux package

```sh
electron22 main.js
```

### Using NPM

```sh
npm exec electron .
```

## Package App

**NOTE:** Resulting Package can big,
as it contains Electron and all its dependencies.

Build using NPM

```sh
rm -rf ./appname-linux-x64
npm exec @electron/packager ./ appname
```

Run binary

```sh
./appname-linux-x64/appname
```

