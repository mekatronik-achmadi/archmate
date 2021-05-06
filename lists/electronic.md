##### install kicad
kicad kicad-library
kicad-library-3d

##### install circuit simulator
simavr gpsim ngspice

##### install stm32 programming
libopencm3 stlink
arm-none-eabi-gcc
arm-none-eabi-newlib

##### install atmega programming
avr-gcc avr-libc
arduino-avr-core
arduino avrdude
arduino-builder
arduino-ctags

##### install serial terminal
python-pyusb
minicom picocom
python-pyserial
esptool moserial

--------------------------------------------------------------------------------

##### install serial port tools
- https://aur.archlinux.org/packages/cutecom/
- https://aur.archlinux.org/packages/interceptty/

##### install stm32 additional
- https://aur.archlinux.org/packages/stm32flash/
- https://aur.archlinux.org/packages/stm32cubemx/

##### install esp8266 sdk

~~~
remove python2 and python2-pyserial from depends
change expat version to 2.3.0 in crosstool-NG/config/companion-libs/expat.in
~~~
- https://aur.archlinux.org/packages/esp-open-sdk-git/

##### install kicad additional library
- https://aur.archlinux.org/packages/kicad-library-digikey-git/
- https://aur.archlinux.org/packages/kicad-library-sparkfun-git/
- https://aur.archlinux.org/packages/kicad-interactive-html-bom-plugin/

##### install arduino additional tools
- https://aur.archlinux.org/packages/simulide-svn/
- https://aur.archlinux.org/packages/arduino-mk/

--------------------------------------------------------------------------------

##### install cadsoft eagle
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/eaglecad/

##### install kicad additional libraries
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/kicad-user/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/kicad-radio/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/kicad-seeed/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/kicad-smisioto/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/kicad-teardrops/

##### install stm32 libraries
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/ugfxlib/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/stm32chlib/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/libopencm3-demos/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/stm32chlib-bluepill/

##### install esp8266 libraries
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/esp8266lib/

##### install stm32 tools
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/stlink-updater/

#### install wxserterm
- https://github.com/mekatronik-achmadi/wxserterm/

##### install atmega tools
- https://github.com/mekatronik-achmadi/atmega-dev/

~~~
atmega-tools
atmega-demos
qtcreator-arduino
~~~

--------------------------------------------------------------------------------

##### configure kicad

~~~
for i in `pacman -Qlq kicad | grep desktop`;do sudo sed -i "s#Categories=Science;Electronics;#Categories=Development;#g" $i;done
~~~

##### kicad custom symbol/footprint

~~~
https://techexplorations.com/blog/kicad/blog-kicad-5-recipe-how-to-create-a-new-component-symbol/
https://techexplorations.com/kicad-4-book/index-p=111.html
~~~

##### configure tty access

~~~
sudo groupadd -fr lock
sudo groupadd -fr uucp

sudo gpasswd -a $USER lock
sudo gpasswd -a $USER uucp
~~~

##### configure cutecom

~~~
sudo sed -i "s#X-KDE-StartupNotify=false#Categories=Development;#g" /usr/share/applications/cutecom.desktop
~~~

##### configure arduino-IDE

~~~
sudo sed -i 's#("-DAPP_DIR=$APPDIR")#("-DAPP_DIR=$APPDIR" "-Dawt.useSystemAAFontSettings=on" "-Dswing.aatext=true" "-Djdk.util.zip.ensureTrailingSlash=false")#g' /usr/share/arduino/arduino
~~~

~~~
File -> Preferences -> Additional Board Manager URLs
Tools -> Board: -> Boards Manager

https://arduino.esp8266.com/stable/package_esp8266com_index.json
https://dan.drown.org/stm32duino/package_STM32duino_index.json
~~~

##### configure st-link

~~~
sudo st-updater
sudo st-flash write ch.bin 0x8000000
sudo st-flash erase
~~~

##### configure stm32cubemx

~~~
sudo groupadd -fr cubemxnoinet
sudo iptables -I OUTPUT 1 -m owner --gid-owner cubemxnoinet -j DROP
sudo ip6tables -I OUTPUT 1 -m owner --gid-owner cubemxnoinet -j DROP
sudo gpasswd -a $USER cubemxnoinet
sudo -g cubemxnoinet stm32cubemx
~~~

##### configure esptool

~~~
sudo esptool -p /dev/ttyUSB0 -b 115200 erase_flash
sudo esptool -p /dev/ttyUSB0 -b 115200 write_flash 0x000000 ai-thinker-0.9.5.2-9600.bin
sudo esptool -p /dev/ttyUSB0 -b 115200 write_flash \
0x000000 nodemcu-dev-7-modules.bin \
0x3fc000 esp_init_data_default.bin
~~~

##### configure vim clang

~~~
sed -i 's#"-mno-thumb-interwork",##g' compile_commands.json
~~~
