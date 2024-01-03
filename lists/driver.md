# Driver Packages

## Official

### install vulkan mesa driver

vulkan-radeon lib32-vulkan-radeon
vulkan-icd-loader lib32-vulkan-icd-loader
lib32-vulkan-intel lib32-vulkan-mesa-layers
vulkan-tools vulkan-intel vulkan-mesa-layers

### install intel-nvidia driver

```sh
echo "Install NVIDIA drivers first"
```

bumblebee primus lib32-primus
nvidia-prime bbswitch-dkms
primus_vk lib32-primus_vk
virtualgl lib32-virtualgl

--------------------------------------------------------------------------------

## AUR

### install gpu driver

#### nvidia-390 (utils,dkms,opencl)

- https://aur.archlinux.org/packages/nvidia-390xx-utils/
- https://aur.archlinux.org/packages/lib32-nvidia-390xx-utils/

### install scanners

#### brother mfc-j220

- https://aur.archlinux.org/packages/brscan3/
- https://aur.archlinux.org/packages/brother-mfc-j220/

### install printers

#### canon

- https://aur.archlinux.org/packages/cnijfilter-ip2700series/

#### hp

- https://aur.archlinux.org/packages/hplip-plugin/

### install some usb drivers

#### tl-wn823n (rtl8192eu)

```sh
echo "activate LED"
sed -i '2i EXTRA_CFLAGS += -DCONFIG_RTW_LED' src/8192eu/Makefile
```

- https://aur.archlinux.org/packages/8192eu-dkms-git/

--------------------------------------------------------------------------------

## Configurations

### configure new driver modeset

```sh
sudo sed -i 's#loglevel=3 quiet#loglevel=3 driver=nonfree nouveau.modeset=0 i915.modeset=1 radeon.modeset=1 quiet#' \
/etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### configure nvidia

#### prevent nouveau

```sh
sudo sed -i 's@kms @@g' /etc/mkinitcpio.conf
sudo mkinitcpio -p archmate
```

#### bumblebee setup

```sh
ls /usr/lib/modprobe.d/bumblebee.conf

sudo gpasswd -a $USER video
sudo gpasswd -a $USER bumblebee
sudo sed -i '0,/Driver=/s//Driver=nvidia/' /etc/bumblebee/bumblebee.conf
sudo sed -i 's@PMMethod=auto@PMMethod=bbswitch@g' /etc/bumblebee/bumblebee.conf
sudo sed -i 's@#   BusID "PCI:01:00:0"@   BusID "PCI:01:00:0"@g' /etc/bumblebee/xorg.conf.nvidia
sudo systemctl enable bumblebeed

sudo reboot
```

#### bumblebee usage

```sh
glxgears
optirun glxgears
optirun glxspheres64
#optirun glxspheres32
```

```sh
optirun wine program.exe
optirun -b primus wine program.exe

# if exit kill all wineserver
killall wineserver
```

#### optirun exit

```sh
optirun --status
lsmod | grep nvidia
sudo rmmod nvidia_drm nvidia_modeset nvidia
echo 'OFF' | sudo tee /proc/acpi/bbswitch
```

### configure printer drivers

```sh
sudo rm -vf /usr/share/applications/hp-uiscan.desktop
```

### configure usb-wifi drivers

#### tl-wn823n (rtl8192eu)

```sh
#sudo dkms install --no-depmod 8192eu/r257.744bbe5 -k $(uname -r)
#sudo depmod -a
#sudo modprobe 8192eu

echo "blacklist rtl8xxxu
options 8192eu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8xxxu.conf
```
