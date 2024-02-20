# PlatformIO

## Setup

```sh
cd $HOME
virtualenv platformio --system-site-packages

source $HOME/platformio/bin/activate
mkdir -p $HOME/.platformio/
pip install platformio

UDEV=https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules
curl -fsSL $UDEV | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
sudo udevadm control --reload-rules
sudo udevadm trigger

deactivate
cd -
```

## Home Webpage

```
source $HOME/platformio/bin/activate
pio home --shutdown-timeout 1 &

#xdg-open http://localhost:8008/ &
```

## Project

### Setup

```sh
source $HOME/platformio/bin/activate
mkdir -p blink/;cd blink/

pio project init --board nodemcu
pio project init --ide vim --board nodemcu
```

### Build

```sh
source $HOME/platformio/bin/activate
export MAKEFLAGS=-j$(nproc)

make compiledb
make all

ls .pio/build/nodemcu/firmware.bin
make upload
```

### Serial

```sh
source $HOME/platformio/bin/activate
make monitor
```

