# PlatformIO

## Setup

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv platformio --system-site-packages

source $HOME/PyEnv/platformio/bin/activate
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
source $HOME/PyEnv/platformio/bin/activate
pio home --no-open &
xdg-open http://localhost:8008/ &
```

## Project

### Setup

```sh
source $HOME/PyEnv/platformio/bin/activate
mkdir -p blink/;cd blink/

pio project init -b bluepill_f103c8
```

```sh
source $HOME/PyEnv/platformio/bin/activate
mkdir -p blink-rtos/;cd blink-rtos/

pio project init -b bluepill_f103c8 -O "lib_deps=stm32duino/STM32duino FreeRTOS"
```

### Build

```sh
source $HOME/PyEnv/platformio/bin/activate
export MAKEFLAGS=-j$(nproc)

make compiledb
make all

ls .pio/build/bluepill_f103c8/firmware.bin
make upload
```

### Serial

```sh
source $HOME/PyEnv/platformio/bin/activate
make monitor
```

