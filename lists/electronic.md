# Electronic Packages

## Official

### install stm32 programming

arm-none-eabi-gcc arm-none-eabi-gdb
arm-none-eabi-newlib stlink

### install atmega programming

avr-gcc avr-gdb avr-libc avrdude

### install additional tools

python-pyserial socat picocom moserial
python-pyusb esptool screen dfu-util

--------------------------------------------------------------------------------

## AUR

### install serial port tools

- https://aur.archlinux.org/packages/interceptty/
- https://aur.archlinux.org/packages/serialplot-hg/

### install stm32 tools

- https://aur.archlinux.org/packages/stm32flash/

### install esp8266 compiler

```sh
sed -i "s#'expat' 'gdbm'#'expat' 'mpdecimal' 'gdbm'#g" PKGBUILD
```

- https://aur.archlinux.org/packages/python39/
- https://aur.archlinux.org/packages/xtensa-lx106-elf-gcc-bin/

### install esp32 compiler

```sh
sed -i "s#'python2-pyserial' 'python2-cryptography' 'python2-pyparsing'##g" PKGBUILD
```

- https://aur.archlinux.org/packages/xtensa-esp32-elf-gcc-bin/

### install simulator

- https://aur.archlinux.org/packages/simulide/

### install stm8 tools

- https://aur.archlinux.org/packages/stm8flash-git/

--------------------------------------------------------------------------------

## External

### install stm32 libraries

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/ugfxlib/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm32chlib/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm32-chibios17/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm32-chibios20/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm32chlib-bluepill/

### install esp libraries

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/esp32-idf/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/esp32-dsp/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/esp8266-rtos/

### install stm32 tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm32cubemx/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stlink-updater/

### install atmega tools

- https://github.com/mekatronik-achmadi/atmega-dev/tree/master/atmega-tools/
- https://github.com/mekatronik-achmadi/atmega-dev/tree/master/atmega-demos/

### install stm8 tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm8spl/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/stm8gal/

--------------------------------------------------------------------------------

## Configurations

### configure tty access

```sh
sudo groupadd -fr lock
sudo groupadd -fr uucp
sudo groupadd -fr dialout

sudo gpasswd -a $USER lock
sudo gpasswd -a $USER uucp
sudo gpasswd -a $USER dialout
```

### configure st-link

#### update st-link

```sh
sudo st-updater
```

#### command examples

```sh
sudo st-info --probe
sudo st-info --reset

sudo st-flash --connect-under-reset erase
sudo st-flash --reset --connect-under-reset --format ihex write ./build/ch.hex
```

#### debugging via st-link

```sh
sudo st-util -p 3333

arm-none-eabi-gdb build/ch.elf
(gdb) target extended-remote localhost:3333
(gdb) r
(gdb) CTRL+C
(gdb) c
(gdb) CTRL+C
(gdb) q
```

```sh
cp -vf /usr/share/gdb-dashboard/.gdbinit ~/
sed -i 's#monokai#sas#' ~/.gdbinit

$> arm-none-eabi-gdb build/ch.elf
>>> target extended-remote localhost:3333
>>> disass main
>>> monitor reset init
>>> monitor targets
>>> monitor reset run
```

### configure esp programming

#### mandatory python setup

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv --python=/usr/bin/python3.9 esp-python --system-site-packages

source $HOME/PyEnv/esp-python/bin/activate
pip install kconfiglib future cryptography pyserial pyparsing==2.2.0
deactivate
```

#### esp8266 programming

```sh
export IDF_PATH=/opt/esp8266-rtos
export PATH="$IDF_PATH/tools:$PATH"
export MAKEFLAGS="-j$(nproc)"
export GNUMAKEFLAGS="-j$(nproc)"
source $HOME/PyEnv/esp-python/bin/activate

cp -r $IDF_PATH/examples/get-started/hello_world/ ./
cd hello_world/
```

```sh
echo '# idf_monitor.py only works in 74880 baudrate
CONFIG_CONSOLE_UART_BAUDRATE=115200
CONFIG_ESP_CONSOLE_UART_BAUDRATE=115200' > sdkconfig.defaults

make defconfig
bear -- make app
```

```sh
make erase_flash # need once per chip
make bootloader-flash # need once per chip
make partition_table-flash # need once per chip
```

```sh
make app
make app-flash
```

```sh
make monitor # CTRL+] to exit
```

#### esp32 programming

```sh
export IDF_PATH=/opt/esp-idf
export PATH="$IDF_PATH/tools:$PATH"
export MAKEFLAGS="-j$(nproc)"
export GNUMAKEFLAGS="-j$(nproc)"
source $HOME/PyEnv/esp-python/bin/activate

cp -r $IDF_PATH/examples/get-started/blink/ ./
cd blink/;
```

```sh
echo '# disable outdated sertificate bundle
CONFIG_MBEDTLS_CERTIFICATE_BUNDLE_DEFAULT_CMN=y
' > sdkconfig.defaults

make defconfig
bear -- make app
```

```sh
make erase_flash # need once per chip
make bootloader-flash # need once per chip
make partition_table-flash # need once per chip
```

```sh
make app
make app-flash
```

```sh
make monitor # CTRL+] to exit
```

### configure platformio

#### install inside virtualenv

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv platformio --system-site-packages

mkdir -p $HOME/.platformio/
source $HOME/PyEnv/platformio/bin/activate
pip install platformio

deactivate
```

#### install udev

```sh
UDEV=https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules
curl -fsSL $UDEV | sudo tee /etc/udev/rules.d/99-platformio-udev.rules

sudo udevadm control --reload-rules
sudo udevadm trigger
```

#### install inside vscode

```sh
code --force --install-extension platformio.platformio-ide
code --force --install-extension ms-vscode.vscode-serial-monitor
```

Menu List:

- Open PlatformIO: **View** -> **Open View** -> **PlatformIO**
	+ Home: **Quick Access** -> **PIO Home** -> **Open**
	+ Project: **Project Tasks** -> **Pick a Folder**
	+ Build/Upload: **Project Tasks** -> ProjectName/Default -> **General**
- Serial Port: **View** -> **Open View** -> **Serial Monitor**

#### manager webserver

```sh
source $HOME/PyEnv/platformio/bin/activate

pio home --no-open &
#pio home --host=0.0.0.0 --no-open &

xdg-open http://localhost:8008/ &

#sed -i "s@'dark'@'light'@g" $HOME/.platformio/packages/contrib-piohome/index.html
```

#### example avr chip

```sh
source $HOME/PyEnv/platformio/bin/activate

mkdir -p blink/;cd blink/
pio project init -b nanoatmega328

echo -e '#PlatformIO Makefile
all:
\tpio run

compiledb:
\tpio run --target compiledb

upload:
\tpio run -v --target upload

clean:
\tpio run --target clean

monitor:
\tpio device monitor -p /dev/ttyUSB0 -b 115200
' | tee Makefile
```

```sh
echo '#include <Arduino.h>

void setup(){
    Serial.begin(9600);
}

void loop(){
    delay(250);
}
' | tee src/main.cpp

make all
ls .pio/build/*/firmware.bin
ls .pio/build/*/firmware.hex

rm -f compile_commands.json
make compiledb
```

#### using frameworks/libraries

```sh
source $HOME/PyEnv/platformio/bin/activate

pio project init -b nanoatmega328 -O "framework=arduino"
pio project init -b nanoatmega328 -O "lib_deps=feilipu/FreeRTOS"

rm -f compile_commands.json
make compiledb
```

#### arduino bootloader using USBAsp

```sh
cd ~/.platformio/packages/framework-arduino-avr/bootloaders/atmega/

avrdude -C /etc/avrdude.conf \
-p m328p -P usb -c usbasp \
-U flash:w:ATmegaBOOT_168_atmega328.hex:a
```
