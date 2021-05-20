#### updated list:
- [x] archiso.md
- [x] base.md
- [x] cad.md
- [x] campus.md
- [x] driver.md
- [x] electronic.md
- [x] multimedia.md
- [x] networking.md
- [x] programming.md
- [x] qt.md
- [x] virtual.md
- [x] winlayer.md

--------------------------------------------------------------------------------

#### archived official packages

##### install kernel lts
linux-lts linux-lts-headers

--------------------------------------------------------------------------------

#### archived aur packages

##### install arm-linux-gnueabihf toolchain
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-binutils/
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-linux-api-headers/
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc-stage1/ (temporary)
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-glibc-headers/ (temporary)
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc-stage2/ (temporary)
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-glibc/
- https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/

##### install ns2 network simulator
- https://aur.archlinux.org/packages/tclcl/
- https://aur.archlinux.org/packages/otcl/ (--asdeps)
- https://aur.archlinux.org/packages/ns/
- https://aur.archlinux.org/packages/nam/
- https://aur.archlinux.org/packages/xgraph/

--------------------------------------------------------------------------------

#### archived external packages

##### install stm32 libraries
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/freertos/

##### install esp8266 libraries
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/esp8266-rtos/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/esp32-idf/

##### install vns ns2
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/ns2-vns/

##### install python seabreeze
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/seabreeze/libseabreeze
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/seabreeze/python-seabreeze

##### install matlab binary
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/matlab-bin/matlab-bin-all/

--------------------------------------------------------------------------------

#### archived configurations

##### configure kernel to use

~~~
echo "use LTS kernel"
sudo sed -i 's#GRUB_DEFAULT="linux"#GRUB_DEFAULT="linux-lts"#g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
~~~

~~~
echo "use latest kernel"
sudo sed -i 's#GRUB_DEFAULT="linux-lts"#GRUB_DEFAULT="linux"#g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
~~~
