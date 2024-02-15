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

#firefox http://localhost:8008/ &
```

## Project

### Setup

```sh
source $HOME/platformio/bin/activate

pio project init --ide vim --board esp32dev
#pio project init --ide vscode --board esp32dev
```

### Build

```sh
source $HOME/platformio/bin/activate

export MAKEFLAGS=-j$(nproc)
make all

ls .pio/build/esp32dev/*.hex
```

### Serial

```sh
source $HOME/platformio/bin/activate

pio device monitor -p /dev/ttyUSB0 -b 9600
```

