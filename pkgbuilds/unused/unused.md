# Other Packages

## Official

### install ubuntu fonts

ttf-ubuntu-mono-nerd
ttf-ubuntu-font-family

--------------------------------------------------------------------------------

## AUR

### install scanners

#### brother mfc-j220

- https://aur.archlinux.org/packages/brscan3/
- https://aur.archlinux.org/packages/brother-mfc-j220/

### install printers

#### canon

- https://aur.archlinux.org/packages/cnijfilter-ip2700series/rs

### install nvidia drivers

#### nvidia-470 (utils,dkms,opencl)

- https://aur.archlinux.org/packages/nvidia-470xx-utils/
- https://aur.archlinux.org/packages/lib32-nvidia-470xx-utils/

#### nvidia-optimus

- https://aur.archlinux.org/packages/optimus-manager/

### install internet tools

- https://aur.archlinux.org/packages/hyperspace-bin/
- https://aur.archlinux.org/packages/google-chrome/

### install remote desktop

- https://aur.archlinux.org/packages/anydesk-bin/
- https://aur.archlinux.org/packages/teamviewer/

## install academic tools

- https://aur.archlinux.org/packages/zotero-bin/
- https://aur.archlinux.org/packages/rstudio-desktop-bin/
- https://aur.archlinux.org/packages/mendeleydesktop-bundled/

### install wps office

- https://aur.archlinux.org/packages/libtiff5/
- https://aur.archlinux.org/packages/wps-office/
- https://aur.archlinux.org/packages/ttf-wps-fonts/

--------------------------------------------------------------------------------

## External

### install matlab binary

- https://github.com/mekatronik-achmadi/archmate/tree/master/pkgbuilds/unused/matlab-bin-basic/

### install cadsoft eagle

- https://aur.archlinux.org/packages/openssl-1.0/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/eaglecad/

### install internet tool

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/discord/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/telegram/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/ungoogled/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/packettracer/

### install additional themes

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/themes/archmate-classic/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/themes/archmate-ubuntu/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/themes/archmate-win10/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/themes/archmate-menu/

### install lubuntu desktop

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/lubuntu/lxde/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/lubuntu/theme/

--------------------------------------------------------------------------------

## Configurations

### configure nvidia

#### optimus manager

```sh
sudo systemctl disable bumblebeed
sudo systemctl enable optimus-manager
sudo reboot
```

```sh
# clear switching errors
prime-offload

optimus-manager --no-confirm --switch hybrid
optimus-manager --no-confirm --switch intel
```

#### disable nvidia gpu

```sh
echo '
blacklist nouveau
blacklist nvidia
options nouveau modeset=0' | sudo tee /etc/modprobe.d/blacklist-nvidia.conf

echo '
# Remove NVIDIA USB xHCI Host Controller devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA USB Type-C UCSI devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA Audio devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA VGA/3D controller devices
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x03[0-9]*", ATTR{power/control}="auto", ATTR{remove}="1"' | \
sudo tee /etc/udev/rules.d/00-remove-nvidia.rules

sudo systemctl disable optimus-manager
sudo reboot

lsmod | grep nvi
lsmod | grep nou
lspci | grep -i nvidia
```

### configure matlab

```sh
echo "09806-07443-53955-64350-21751-41297"
```

```sh
sudo mount R2018a_glnxa64_dvd1.iso /mnt/
/mnt/install &
sudo umount /mnt/
sudo mount R2018a_glnxa64_dvd2.iso /mnt/
```

```sh
# install folder: /home/developments/Packages/Matlab-2018a/built/matlab-2018a/
cd /home/developments/Packages/Matlab-2018a/built/
ls matlab-2018a/
mv -vf ./matlab-2018a/ matlab-bin-basic/matlab-2018a/
cd matlab-bin-basic/
makepkg -sir
sudo pacman -S libxcrypt-compat
```

```sh
sudo cp libmwlmgrimpl.so /opt/mathworks/matlab-2018a/bin/glnxa64/matlab_startup_plugins/lmgrimpl/
sudo matlab
sudo chown -R $USER:users $HOME/.matlab/R2018a/
```

```sh
matlab-gui
cd /opt/mathworks/addons/schemer/
schemer_import
```

```sh
# fix graphic low level issue
echo "-Djogl.disable.openglarbcontext=1" | sudo tee -a /opt/mathworks/matlab-2018a/bin/glnxa64/java.opts
```

### configure remote desktop

#### anydesk

```sh
sudo systemctl enable anydesk
sudo systemctl start anydesk
```

#### teamviewer

```sh
sudo rm -f /usr/share/applications/teamviewerapi.desktop

sudo systemctl enable teamviewerd
sudo systemctl start teamviewerd
```

### configure cisco packet simulator

```sh
sudo ln -svf /opt/packettracer/packettracer /usr/bin/packettracer
```

### configure wps office

```sh
sudo rm -f /usr/share/applications/wps-office-pdf.desktop
sudo rm -f /usr/share/applications/wps-office-prometheus.desktop
sudo sed -i '/^$/d' /usr/share/desktop-directories/wps-office.directory
echo 'NoDisplay=true' | sudo tee -a /usr/share/desktop-directories/wps-office.directory
```

