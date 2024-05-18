# Driver Packages

## Official

### install vulkan drivers

vulkan-intel lib32-vulkan-intel
amdvlk lib32-amdvlk vulkan-tools
vulkan-swrast lib32-vulkan-swrast
vulkan-radeon lib32-vulkan-radeon
vulkan-icd-loader lib32-vulkan-icd-loader
vulkan-mesa-layers lib32-vulkan-mesa-layers

### install intel-nvidia driver

```
# Install NVIDIA drivers first
```

bumblebee primus lib32-primus
nvidia-prime bbswitch-dkms
primus_vk lib32-primus_vk
virtualgl lib32-virtualgl

### install additonal drivers

android-udev python-pyudev libusb-compat
scrcpy libmtp android-file-transfer

--------------------------------------------------------------------------------

## AUR

### install gpu driver

#### nvidia-390 (utils,dkms,opencl)

- https://aur.archlinux.org/packages/nvidia-390xx-utils/
- https://aur.archlinux.org/packages/lib32-nvidia-390xx-utils/

### install some usb drivers

#### tl-wn823n (rtl8192eu)

```sh
echo "activate LED"
sed -i '2i EXTRA_CFLAGS += -DCONFIG_RTW_LED' src/8192eu/Makefile
```

- https://aur.archlinux.org/packages/8192eu-dkms-git/

--------------------------------------------------------------------------------

## Configurations

### configure newer gpu modeset

```sh
sudo sed -i 's#loglevel=3 quiet#loglevel=3 driver=nonfree nouveau.modeset=0 i915.modeset=1 radeon.modeset=1 quiet#' \
/etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### configure nvidia

#### prevent nouveau

```sh
sudo sed -i 's@kms @@g' /etc/mkinitcpio.conf
sudo mkinitcpio -p archlinux
```

#### disable nvidiafb

```sh
echo 'blacklist nvidiafb
' | sudo tee /etc/modprobe.d/rtl8xxxu.conf
```

#### bumblebee setup

```sh
sudo lspci | grep -i vga
bat /usr/lib/modprobe.d/bumblebee.conf

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
optirun --status
lsmod | grep nvidia
watch -n1 nvidia-smi

glxgears
optirun glxgears
```

#### optirun exit

```sh
optirun --status
lsmod | grep nvidia
watch -n1 nvidia-smi

sudo rmmod nvidia_drm nvidia_modeset nvidia
echo 'OFF' | sudo tee /proc/acpi/bbswitch
```

### configure android MTP

**WARNING:** MTPFs won't work.

**NOTE:** Sometimes, GVFS-MTP works better

```sh
sudo groupadd -fr adbusers
sudo gpasswd -a $USER adbusers
sudo reboot

mtp-detect
```

get access permission:
- Caja/PCManFM:
    + open mount path in file manager
    + reload, it will ask permission
    + reload again

```sh
mkdir -p ~/MTP_mnt
aft-mtp-mount ~/MTP_mnt

caja ~/MTP_mnt
pcmanfm ~/MTP_mnt

umount ~/MTP_mnt
```

```sh
mkdir -p ~/MTP_mnt
aft-mtp-mount ~/MTP_mnt

# exit MC if empty
mc ~/MTP_mnt

# re-mount after ask permission
umount ~/MTP_mnt
aft-mtp-mount ~/MTP_mnt

# check again if not empty
mc ~/MTP_mnt

umount ~/MTP_mnt
```

### configure some usb drivers

#### tl-wn823n (rtl8192eu)

```sh
#sudo dkms install --no-depmod 8192eu/r257.744bbe5 -k $(uname -r)
#sudo depmod -a
#sudo modprobe 8192eu

echo "blacklist rtl8xxxu
options 8192eu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8xxxu.conf
```
