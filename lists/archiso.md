# ArchISO Packages

## Official

### install basic system

linux linux-headers linux-firmware
base base-devel multilib-devel

### install basic tools

bash-completion mkinitcpio
squashfs-tools rsync dkms
most highlight mc fdupes
neofetch lsb-release dtc
nano dialog bc tmux tree
curl wget openssh sshfs
pacman-contrib mlocate
virtualbox-guest-utils
intel-ucode amd-ucode
git tig terminus-font
arch-install-scripts
mkinitcpio-archiso
cdrtools syslinux
libxcrypt-compat
zsh-completions
pv archinstall

### install posix meta

posix posix-software-development
posix-xsi posix-c-development

### install vim editor

gvim vim-nerdtree vim-surround
vim-nerdcommenter vim-gitgutter
vim-airline vim-tagbar vim-tabular

### install xorg server

xorg xorg-apps xorg-drivers
xorg-xinit xorg-fonts
xsel xclip xterm
xorg-fonts-misc
xorg-xmessage

### install login manager

lightdm lightdm-gtk-greeter

### install mate desktop

mate mate-extra
dconf dconf-editor

### install themes and icons

icon-naming-utils gtk-update-icon-cache
papirus-icon-theme arc-solid-gtk-theme
gtk-engines gtk-engine-murrine
gnome-themes-extra libcanberra
sound-theme-freedesktop

### install gtk 2/3 libraries

gtk3 wxgtk3 glade
gtk2 gtkmm gtkmm3
python-wxpython
python-gobject

### install desktop basic

tk ttf-liberation onboard
ttf-liberation-mono-nerd
xdg-desktop-portal-gtk
ttf-dejavu ttf-droid
libappindicator-gtk3
redshift python-xdg
archlinux-wallpaper
xdg-desktop-portal
xdg-user-dirs-gtk

### install desktop tools

geany geany-plugins
qt5-base qt6-base
qt5ct qt6ct scrot
xdotool shotwell
parcellite meld

### install openbox session

openbox obconf tint2 feh xpdf bashrun
volumeicon xarchiver brightnessctl

### install lxde-gtk3 session

lxdm-gtk3 lxterminal
lxde-common lxpanel-gtk3
lxde-icon-theme gpicview
lxhotkey-gtk3 lxinput-gtk3
pcmanfm-gtk3 lxsession-gtk3
lxrandr-gtk3 lxappearance-gtk3

### install networking system

networkmanager nm-connection-editor
network-manager-applet modemmanager
mobile-broadband-provider-info iftop
bind-tools netctl ppp wpa_supplicant
net-tools wavemon bmon nethogs gping
crda iw iwd wireless_tools tigervnc
bridge-utils ethtool usb_modeswitch
traceroute dhcp dnsmasq nss-mdns
openresolv dhclient dhcpcd mtr
gnu-netcat nmap termshark
tcpdump fping inetutils

### install audio system

pulseaudio portaudio
jack2 pulseaudio-jack
alsa-utils alsa-firmware
alsa-ucm-conf sof-firmware
alsa-oss alsa-lib alsa-plugins
pulseaudio-equalizer pavucontrol
pulseaudio-alsa pulseaudio-bluetooth

### install gio filesystem

gvfs gvfs-gphoto2 gvfs-afc
gvfs-mtp gvfs-smb gvfs-nfs

### install compression tools

tar atool xz libarchive unrar unarj
lhasa rpmextract lxsplit unrar-free
bzip2 gzip lz4 p7zip zip unzip
lrzip lzip lzop zstd cpio

### install build tools

subversion automake
mk-configure autogen
cblas openblas lapack
gobject-introspection
mate-common gnome-common
pkgconf gendesk help2man
mercurial breezy cvs cloc
cmake extra-cmake-modules
dos2unix doxygen graphviz
bear autoconf meson ninja

### install java basic

jre8-openjdk jdk8-openjdk

### install python installer

python-pkgconfig python-wheel
python-build python-installer
python-pipenv python-virtualenv
python-pip python-distutils-extra
cython0 pybind11 python-setuptools

### install internet tools

firefox filezilla uget aria2
vimb qbittorrent-nox qbittorrent

### install bluetooth support

blueman bluez
bluez-utils

### install multimedia

ffmpegthumbnailer
ffmpeg gst-libav
gst-plugins-good
gst-plugins-base
vlc guvcview

### install libva driver

intel-media-driver
libva-intel-driver
libva-vdpau-driver
libva-mesa-driver
libva libva-utils
libvdpau-va-gl
vdpauinfo

### install cd-dvd tools

fuseiso mdf2iso
brasero bchunk
squashfuse
dvdauthor
vcdimager

### install printing support

cups cups-pdf
ghostscript gsfonts
system-config-printer
gutenprint foomatic-db-engine
foomatic-db foomatic-db-nonfree

### install image scanner

sane sane-airscan
ipp-usb simple-scan

### install system information

lm_sensors xsensors hddtemp
lsof nmon sysstat procps-ng
usbutils dmidecode hwdetect
hdparm sdparm smartmontools
htop ltrace strace mesa-demos
linux-tools arandr read-edid
hwloc hwinfo lshw mesa-utils
ccze inxi atop libstatgrab

### install disk tools

ntfs-3g exfat-utils
gparted dosfstools
gpart e2fsprogs
gptfdisk mtools
fuse2 fuse3

### install boot system

grub os-prober
efibootmgr
edk2-shell
edk2-ovmf

--------------------------------------------------------------------------------

## Non-Official

### install additional base

- qt5gtk2: https://aur.archlinux.org/packages/qt5gtk2/
- qt6gtk2: https://aur.archlinux.org/packages/qt6gtk2/
- brisk-menu: https://aur.archlinux.org/packages/brisk-menu/
- gtk3-nocsd-git: https://aur.archlinux.org/packages/gtk3-nocsd-git/
- mate-tweak: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/mate-tweak/
- mate-zenity: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/mate-zenity/

### install additional tools

- downgrade: https://aur.archlinux.org/packages/downgrade/
- fake-hwclock: https://aur.archlinux.org/packages/fake-hwclock/
- hardinfo-git: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/hardinfo/

### install vim additionals

- vim-plug-git: https://aur.archlinux.org/packages/vim-plug-git/
- vim-devicons-git: https://aur.archlinux.org/packages/vim-devicons-git/

### install custom packages

- archmate-font: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-font/
- archmate-theme: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-theme/
- archmate-lxde3: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-lxde3/
- archmate-openbox: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-openbox/
- archmate-archiso: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-archiso/
- archmate-desktop: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-desktop/
- archmate-install: https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom/archmate-install/

--------------------------------------------------------------------------------

## Configurations

### repository setting

```sh
# ArchLinux Repository Main Server URL
# Lower Mirror Score means better
# Look for 100% synced mirror from here:
#   https://archlinux.org/mirrors/status/#successful
export REPOURL='http://mirror.internode.on.net/pub/archlinux'
```

### after installation

```sh
sudo systemctl enable systemd-timesyncd
sudo systemctl start systemd-timesyncd
sudo systemctl enable fake-hwclock fake-hwclock-save
sudo systemctl start fake-hwclock fake-hwclock-save

sudo ln -svf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
sudo date -s "3 JAN 2024 20:46"

echo "LANG=en_US.UTF-8" | sudo tee /etc/locale.conf
echo "en_US ISO-8859-1" | sudo tee /etc/locale.gen
echo "en_US.UTF-8 UTF-8" | sudo tee -a /etc/locale.gen
sudo locale-gen

sudo mkdir -vp /var/lib/pacman/sync/
sudo mkdir -vp /var/cache/pacman/pkg/

export ISOVER='mate_012024'
export DIRPATH="/home/developments/Packages/ArchMate-x86_64/$ISOVER"
sudo rsync -avh $DIRPATH/databases/ /var/lib/pacman/sync/
sudo rsync -avh $DIRPATH/packages/official/ /var/cache/pacman/pkg/

echo "install driver packages"
pluma lists/driver.md
```

### pacman-key problem

```sh
# optionally only if had problems
# need internet connection and proper time setting

sudo pacman-key --init
sudo pacman-key --populate archlinux

# if initialitation keep failed
#sudo pacman-key --refresh-keys
```

### configure booting

#### GRUB-BIOS from Live ISO

```sh
sudo mount /dev/sda1 /mnt/
sudo arch-chroot /mnt/

grub-install --recheck --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg

exit
sudo umount /mnt/
```

#### GRUB-UEFI from Live ISO

```sh
sudo mount /dev/sda2 /mnt/
sudo mount /dev/sda1 /mnt/boot/EFI
sudo arch-chroot /mnt/

# reinstall grub for default uefi
grub-install --recheck --target=x86_64-efi --efi-directory=/boot/EFI/ --bootloader-id=grub_uefi

# reinstall grub for removable uefi
grub-install --recheck --removable --target=x86_64-efi --efi-directory=/boot/EFI/ --bootloader-id=grub_uefi

grub-mkconfig -o /boot/grub/grub.cfg

exit
sudo umount /mnt/boot/EFI
sudo umount /mnt/
```

#### GRUB include Windows

```sh
echo 'Reconfig GRUB to include Windows'
sudo sed -i 's|#GRUB_DISABLE_OS_PROBER=false|GRUB_DISABLE_OS_PROBER=false|g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

#### GRUB SWAP partition

```sh
sudo mkswap /dev/sdxy
sudo swapon /dev/sdxy

SWAPUUID=$(sudo blkid -s UUID -o value /dev/sdxy)
echo "UUID=$SWAPUUID none swap defaults 0 0" | sudo tee -a /etc/fstab
```

### generic configurations

#### modify pacstrap

```sh
sudo bash /usr/share/archmate-archiso/pacstrap_modify
```

#### configure git user

```sh
git config --global init.defaultBranch main
git config --global user.name "mekatronik-achmadi"
git config --global user.email "mekatronik.achmadi@gmail.com"

echo "export GITHUBTOKEN=$(cat ~/GithubToken.txt)" | tee -a ~/.bashrc
```

#### create new user with/without password

```sh
sudo useradd -m -g users -G wheel,storage,power,tty,video -s /bin/bash -c username username

# change password
sudo passwd username

# remove password password
sudo passwd -d username
```

#### configure networkmanager

```sh
sudo systemctl disable systemd-networkd
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-networkd
sudo systemctl stop systemd-resolved

sudo ln -svf /run/NetworkManager/resolv.conf /etc/resolv.conf
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
```

#### configure bluetooth

```sh
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo bluetoothctl
```

#### configure vim

```sh
sudo mkdir -p /etc
echo '" /usr/share/vim/vimfiles/archlinux.vim' | sudo tee /etc/vimrc
echo 'runtime! archlinux.vim
autocmd BufWritePre * %s/\s\+$//e
filetype plugin on
filetype indent on
filetype plugin indent on
set expandtab ts=4 sw=4 ai
set conceallevel=0
set encoding=utf-8
set termguicolors
set ic is hls
set number
set wrap!
set mouse=a
let g:tagbar_width=20
let g:NERDTreeWinSize=20
syntax on
if has("gui_running")
  colorscheme shine
  set guifont=LiterationMono\ Nerd\ Font\ Mono\ 8
endif' | sudo tee -a /etc/vimrc
```

#### configure profile

```sh
sudo mkdir -p /etc/profile.d/
echo '
export PATH=$PATH:~/.local/bin
export QT_QPA_PLATFORMTHEME=qt5ct
export VISUAL=vim
export EDITOR=vim
export PAGER=most
export VIEWER=most
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export FT2_SUBPIXEL_HINTING=2
export GTK_CSD=0
export LD_PRELOAD=/usr/lib/libgtk3-nocsd.so.0:$LD_PRELOAD
' | sudo tee /etc/profile.d/arch-profile.sh
```

#### configure gtk theme

```sh
sudo mkdir -pv /etc/gtk-2.0/
echo '
gtk-icon-theme-name = "Papirus-Light"
gtk-theme-name = "Arc-Lighter-solid"
gtk-font-name = "Liberation Sans 8"
' | sudo tee /etc/gtk-2.0/gtkrc

sudo mkdir -pv /etc/gtk-3.0/
echo '
[Settings]
gtk-icon-theme-name = Papirus-Light
gtk-theme-name = Arc-Lighter-solid
gtk-font-name = Liberation Sans 8
gtk-application-prefer-dark-theme = false
' | sudo tee /etc/gtk-3.0/settings.ini
```

#### configure alternative session default

```sh
sudo rm -vf /etc/systemd/logind.conf.d/do-not-suspend.conf
echo '[login]
HandleLidSwitch=suspend
HandleLidSwitchDocked=suspend
' | sudo tee /etc/systemd/logind.conf.d/lid-suspend.conf

# check available session
ls /usr/share/xsessions/ | cut -d. -f1

# using openbox
sudo sed -i 's#session=mate#session=openbox#g' /etc/lightdm/lightdm.conf

# using LXDE
sudo sed -i 's#session=mate#session=LXDE#g' /etc/lightdm/lightdm.conf
```

#### configure login without lightdm

```sh
sudo mkdir -p /etc/systemd/system/getty@tty1.service.d/

echo "[Service]
TTYVTDisallocate=no
" | sudo tee /etc/systemd/system/getty@tty1.service.d/noclear.conf

echo -e "[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin $USER --noissue --noclear %I 38400 linux
" | sudo tee /etc/systemd/system/getty@tty1.service.d/autologin.conf
```

#### desktop session without lighdm

```sh
# using LXDE
startx /usr/bin/startlxde

# using openbox
startx /usr/bin/openbox-session

# using Mate
startx /usr/bin/mate-session
```

#### cli mount disks

```sh
# list attached disk
lsblk -f -o NAME,FSTYPE,LABEL,FSAVAIL

# mount a partition
udisksctl mount -b /dev/sdb2

# check partition
lsblk -f -o NAME,FSTYPE,LABEL,FSAVAIL

# unmount partition
udisksctl unmount -b /dev/sdb2

# power off disks
udisksctl power-off -b /dev/sdb2
```

#### configure vnc server

```sh
vncpasswd

x0vncserver -rfbauth ~/.vnc/passwd
#x0vncserver -geometry 1280x1024+0+0 -rfbauth ~/.vnc/passwd
```

#### configure vnc viewer

```sh
# Menu/Fullscreen -> F8

vncviewer <ip_number>:0
```

#### configure firefox

- https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/
- https://addons.mozilla.org/en-US/firefox/addon/adblock-for-firefox/

#### configure google drive

- https://workspace.google.com/marketplace/app/file_checksum/982370769845

#### configure electron menu

```sh
sudo rm -vf /usr/share/applications/electron*
```

--------------------------------------------------------------------------------

## Notes

### updated list

- [x] [archiso](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/archiso.md)
- [x] [driver](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/driver.md)
- [x] [media](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/media.md)
- [x] [design](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/design.md)
- [x] [virtual](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/virtual.md)
- [ ] [winlayer](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/winlayer.md)
- [ ] [networking](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/networking.md)
- [ ] [electronic](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/electronic.md)
- [ ] [programming](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/programming.md)
- [ ] [college](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/college.md)
- [x] [other](https://github.com/mekatronik-achmadi/archmate/blob/main/lists/other.md)
