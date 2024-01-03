# Electronic Packages

## Official

### install stm32 programming

arm-none-eabi-gcc arm-none-eabi-gdb
arm-none-eabi-newlib stlink sdcc

### install atmega programming

avr-gcc avr-gdb avr-libc avrdude

### install arduino programming

arduino-cli arduino-avr-core

### install serial terminal

minicom picocom moserial screen
dfu-util esptool socat gtkwave
python-pyserial python-pyusb

--------------------------------------------------------------------------------

## AUR

### install serial port tools

- https://aur.archlinux.org/packages/interceptty/
- https://aur.archlinux.org/packages/serialplot-hg/

### install stm32 tools

- https://aur.archlinux.org/packages/stm32flash/
- https://aur.archlinux.org/packages/stm32cubemx/

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

### install arduino tools

- https://aur.archlinux.org/packages/simulide/
- https://aur.archlinux.org/packages/arduino-mk/
- https://aur.archlinux.org/packages/arduino-ide-bin/

### install stm8 tools

- https://aur.archlinux.org/packages/stm8cubemx/
- https://aur.archlinux.org/packages/stm8flash-git/

--------------------------------------------------------------------------------

## External

### install stm32 libraries

- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/ugfxlib/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32chlib/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32chlib2/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32freertos/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32-chibios17/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32-chibios20/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm32chlib-bluepill/

### install esp libraries

- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/esp32-idf/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/esp32-idf
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/esp32-dsp/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/esp8266-rtos/

### install stm32 tools

- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stlink-updater/

### install atmega tools

- https://github.com/mekatronik-achmadi/atmega-dev/tree/master/atmega-tools/
- https://github.com/mekatronik-achmadi/atmega-dev/tree/master/atmega-demos/
- https://github.com/mekatronik-achmadi/atmega-dev/tree/master/qtcreator-arduino/

### install stm8 tools

- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm8gal/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/pkgbuilds/optional/stm8spl/

--------------------------------------------------------------------------------

## Configurations

### configure tty access

```sh
sudo groupadd -fr lock
sudo groupadd -fr uucp

sudo gpasswd -a $USER lock
sudo gpasswd -a $USER uucp
```

### configure cutecom

```sh
sudo sed -i "s#X-KDE-StartupNotify=false#Categories=Development;#g" /usr/share/applications/cutecom.desktop
```

### configure simutron

```sh
sudo sed -i "s#Categories=Electronics;#Categories=Development;#g" /usr/share/applications/simutron.desktop
```

### configure arduino-IDE

```text
File -> Preferences -> Additional Board Manager URLs
Tools -> Board: -> Boards Manager

https://arduino.esp8266.com/stable/package_esp8266com_index.json
https://dan.drown.org/stm32duino/package_STM32duino_index.json
https://dl.espressif.com/dl/package_esp32_index.json
```

```sh
mkdir -p ~/Arduino/libraries/
cd ~/Arduino/libraries/
git clone https://github.com/sandeepmistry/arduino-LoRa.git LoRa
```

### configure arduino-CLI

```sh
arduino-cli config init

arduino-cli sketch new LED
cd LED/

arduino-cli core update-index
arduino-cli core search nano
arduino-cli core install arduino:avr
arduino-cli core list

arduino-cli lib search DHT11 | grep DHT11
arduino-cli lib install "DHT11"

arduino-cli compile --fqbn arduino:avr:nano

arduino-cli board list
arduino-cli upload --fqbn arduino:avr:nano --port /dev/ttyUSB0
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
# using openocd
sudo openocd -f /usr/share/openocd/scripts/interface/stlink-v2.cfg -f /usr/share/openocd/scripts/target/stm32f4x.cfg

# using st-util
sudo st-util -p 3333
```

```sh
$> arm-none-eabi-gdb build/ch.elf
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
cd $HOME
virtualenv --python=/usr/bin/python3.9 esp-python --system-site-packages

source $HOME/esp-python/bin/activate
pip install kconfiglib future cryptography pyserial pyparsing==2.2.0
deactivate
```

#### esp8266 programming

```sh
export IDF_PATH=/opt/esp8266-rtos
export PATH="$IDF_PATH/tools:$PATH"
export GNUMAKEFLAGS="-j$(nproc)"
source $HOME/esp-python/bin/activate

cp -r $IDF_PATH/examples/get-started/hello_world/ ./
cd hello_world/
```

```sh
echo '# idf_monitor.py only works in 74880 baudrate
CONFIG_CONSOLE_UART_BAUDRATE=115200
CONFIG_ESP_CONSOLE_UART_BAUDRATE=115200' > sdkconfig.defaults

make defconfig
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
export GNUMAKEFLAGS="-j$(nproc)"
source $HOME/esp-python/bin/activate

cp -r $IDF_PATH/examples/get-started/blink/ ./
cd blink/;
```

```sh
echo '# disable outdated sertificate bundle
CONFIG_MBEDTLS_CERTIFICATE_BUNDLE_DEFAULT_CMN=y
' > sdkconfig.defaults

make defconfig
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

#### install requirements

```sh
sudo pacman -S clangd python-pipenv python-virtualenv
```

#### install inside virtualenv

```sh
cd $HOME
virtualenv platformio --system-site-packages
source $HOME/platformio/bin/activate

mkdir -p $HOME/.platformio/
pip install platformio

deactivate
```

#### install udev

```sh
UDEV=https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules
curl -fsSL $UDEV | sudo tee /etc/udev/rules.d/99-platformio-udev.rules

sudo gpasswd -a $USER lock
sudo gpasswd -a $USER uucp

sudo udevadm control --reload-rules
sudo udevadm trigger
```

#### manager webserver

```sh
source $HOME/platformio/bin/activate

sed -i "s@'dark'@'light'@g" $HOME/.platformio/packages/contrib-piohome/index.html

pio home --host=0.0.0.0 --no-open

#xdg-mime default vimb.desktop x-scheme-handler/http
#pio home --host=0.0.0.0
```

#### example arduino avr

```sh
source $HOME/platformio/bin/activate

mkdir -p blink/;cd blink/
pio project init --ide vim --board nanoatmega328
pio project config

echo -e '#PlatformIO Makefile
all:
\tpio -f -c vim run

upload:
\tpio -f -c vim run --target upload

clean:
\tpio -f -c vim run --target clean

program:
\tpio -f -c vim run --target program

uploadfs:
\tpio -f -c vim run --target uploadfs

update:
\tpio -f -c vim update
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

bear -- make all

vim src/main.c
```

#### run a serial monitor

```sh
source $HOME/platformio/bin/activate

pio device monitor -p /dev/ttyUSB0 -b 9600
```

