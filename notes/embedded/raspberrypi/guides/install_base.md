# RaspberryPi Base Installation

## Disk Install

### prepare disk

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
echo ${DEVDISK}

sudo parted ${DEVDISK} mklabel msdos
```

```sh
sudo parted ${DEVDISK} mkpart primary fat32 0% 200
sudo parted ${DEVDISK} mkpart primary ext4 200 100%

sudo mkfs.fat -F32 ${DEVDISK}1
sudo parted ${DEVDISK} set 1 boot on
sudo parted ${DEVDISK} set 1 lba on
sudo mkfs.ext4 ${DEVDISK}2
```

### download image

```sh
wget -c http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-armv7-latest.tar.gz
```

### deploy image

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
echo ${DEVDISK}

sudo mkdir -p /mnt/mmc/{boot,root}
sudo mount ${DEVDISK}1 /mnt/mmc/boot
sudo mount ${DEVDISK}2 /mnt/mmc/root

mkdir -p armv7h/;cd armv7h/

sudo bsdtar -xpf ../ArchLinuxARM-rpi-armv7-latest.tar.gz -C /mnt/mmc/root
sudo sync

sudo mv -vf /mnt/mmc/root/boot/* /mnt/mmc/boot/
sudo sync

sudo umount /mnt/mmc/root /mnt/mmc/boot
```

--------------------------------------------------------------------------------

## Qemu run

### mount disk (host-pc)

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
sudo mount ${DEVDISK}2 /mnt/mmc/root
sudo mount ${DEVDISK}1 /mnt/mmc/root/boot
```

### copy qemu-arm-static (host-pc)

```sh
sudo cp -vf /usr/bin/qemu-arm-static /mnt/mmc/root/usr/bin/
```

### test chroot into mounted sdcard (host-pc)

```sh
sudo arch-chroot /mnt/mmc/root /bin/bash
```

```sh
pacman -V
```

```sh
exit
```

--------------------------------------------------------------------------------

## Install packages

### chroot into mounted sdcard (host-pc)

```sh
sudo arch-chroot /mnt/mmc/root /bin/bash
```

### generate locale (qemu-chroot)

```sh
echo "LANG=en_US.UTF-8" > /etc/locale.conf
echo "en_US ISO-8859-1" > /etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
```

### download database (host-pc)

```sh
mkdir -p databases/;cd databases/

echo "
http://mirror.archlinuxarm.org/armv7h/core/core.db
http://mirror.archlinuxarm.org/armv7h/extra/extra.db
http://mirror.archlinuxarm.org/armv7h/community/community.db
http://mirror.archlinuxarm.org/armv7h/alarm/alarm.db
http://mirror.archlinuxarm.org/armv7h/aur/aur.db
" > ../dbase.txt
wget -c -i ../dbase.txt
cd ../

sudo mkdir -p /mnt/mmc/root/var/lib/pacman/sync/
sudo rsync -avh databases/ /mnt/mmc/root/var/lib/pacman/sync/
```

### generate upgrade packages urls (qemu-chroot)

```sh
pacman -Sup > /home/alarm/upgrade_pkgs.txt
```

### download upgrade packages (host-pc)

```sh
cp -vf /mnt/mmc/root/home/alarm/upgrade_pkgs.txt ./

mkdir -p packages/official/;cd packages/official/
wget -c -i ../../upgrade_pkgs.txt
cd ../../

sudo mkdir -p /mnt/mmc/root/var/cache/pacman/pkg/
sudo rsync -avh packages/official/ /mnt/mmc/root/var/cache/pacman/pkg/
```

### upgrade packages (qemu-chroot)

```sh
sed -i "s#= Required DatabaseOptional#= Never#g" /etc/pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" /etc/pacman.conf
sed -i "s#= Optional#= Never#g" /etc/pacman.conf

pacman -Su --noconfirm
```

### copy install packages list (host-pc)

```sh
cp -vf ../archrpi/pkg_basic.txt /mnt/mmc/root/home/alarm/basiclist.txt
cp -vf ../archrpi/pkg_openbox.txt /mnt/mmc/root/home/alarm/openboxlist.txt
cp -vf ../archrpi/pkg_more.txt /mnt/mmc/root/home/alarm/morelist.txt
cp -vf ../archrpi/pkg_server.txt /mnt/mmc/root/home/alarm/serverlist.txt
```

### generate install packages urls (qemu-chroot)

```sh
pacman -Sp $(cat /home/alarm/basiclist.txt) \
$(cat /home/alarm/openboxlist.txt) \
$(cat /home/alarm/morelist.txt) \
$(cat /home/alarm/serverlist.txt) > /home/alarm/install_pkgs.txt
```

### download install packages (host-pc)

```sh
cp -vf /mnt/mmc/root/home/alarm/install_pkgs.txt ./

mkdir -p packages/official/;cd packages/official/
wget -c -i ../../install_pkgs.txt
cd ../../

sudo rsync -avh packages/official/ /mnt/mmc/root/var/cache/pacman/pkg/
```

### install install packages (qemu-chroot)

```sh
sed -i "s#= Required DatabaseOptional#= Never#g" /etc/pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" /etc/pacman.conf
sed -i "s#= Optional#= Never#g" /etc/pacman.conf

pacman -S --noconfirm $(cat /home/alarm/basiclist.txt)
pacman -S --noconfirm $(cat /home/alarm/openboxlist.txt)
#pacman -S --noconfirm $(cat /home/alarm/morelist.txt)
#pacman -S --noconfirm $(cat /home/alarm/serverlist.txt)
```

### copy openbox default package (host-pc)

```sh
cp -vf ../archrpi/archmate-openbox-0.1-1-any.pkg.tar.zst \
/mnt/mmc/root/home/alarm/
```

### install openbox default package (qemu-chroot)

```sh
pacman -U --noconfirm --assume-installed light \
/home/alarm/archmate-openbox-0.1-1-any.pkg.tar.zst
```

--------------------------------------------------------------------------------

## Global Configuration

### basic config.txt (qemu-chroot)

```sh
echo 'gpu_mem=128
initramfs initramfs-linux.img followkernel

hdmi_force_hotplug=1
max_framebuffers=2
disable_overscan=1
display_auto_detect=1

dtparam=audio=on
camera_auto_detect=1
dtoverlay=disable-bt

[pi2]
dtoverlay=vc4-kms-v3d

[pi3]
dtoverlay=vc4-kms-v3d

[pi4]
arm_boost=1
dtoverlay=vc4-fkms-v3d

[all]
' > /boot/config.txt
```

### set hostname (qemu-chroot)

```sh
echo "alarmrpi" > /etc/hostname
```

### silent cli (qemu-chroot)

```sh
echo '
boot_delay=0
disable_splash=1
avoid_warnings=1' >> /boot/config.txt

sed -i '$s/$/ audit=0 quiet loglevel=0/' /boot/cmdline.txt
```

### sudoers no password (qemu-chroot)

```sh
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

### disable passwords (qemu-chroot)

```sh
passwd -d root
passwd -d alarm
```

### console font (qemu-chroot)

```sh
echo "FONT=ter-112n
FONT_MAP=8859-2
" > /etc/vconsole.conf
mkinitcpio -p linux-rpi
```

### enable timesync (qemu-chroot)

```sh
systemctl enable systemd-timesyncd
systemctl enable fake-hwclock fake-hwclock-save
```

### enable network manager (qemu-chroot)

```sh
systemctl disable dhcpd4
systemctl disable wpa_supplicant
systemctl disable systemd-networkd
systemctl disable systemd-resolved

ln -svf /run/NetworkManager/resolv.conf /etc/resolv.conf
systemctl enable NetworkManager
```

### enable ssh server (qemu-chroot)

```sh
mkdir -p /etc/ssh
echo "
PermitRootLogin yes
AuthorizedKeysFile .ssh/authorized_keys
PermitEmptyPasswords yes
ChallengeResponseAuthentication no
UsePAM yes
PrintMotd no
Subsystem sftp /usr/lib/ssh/sftp-server
X11Forwarding yes
X11UseLocalhost yes
X11DisplayOffset 10
AllowTcpForwarding yes
" > /etc/ssh/sshd_config

systemctl enable sshd.service
```

### shell autologin (qemu-chroot)

```sh
mkdir -p /etc/systemd/system/getty@tty1.service.d/

echo "[Service]
TTYVTDisallocate=no
" > /etc/systemd/system/getty@tty1.service.d/noclear.conf

echo "[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin alarm --noissue --noclear %I 38400 linux
" > /etc/systemd/system/getty@tty1.service.d/autologin.conf
```

### some profiles (qemu-chroot)

```sh
mkdir -p /etc/profile.d/
echo '
export PATH=$PATH:~/.local/bin
export QT_QPA_PLATFORMTHEME=qt5ct
export VISUAL=vim
export EDITOR=vim
export PAGER=most
export VIEWER=most
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export FT2_SUBPIXEL_HINTING=2
' | tee /etc/profile.d/archrpi-profile.sh
```

### vim modify (qemu-chroot)

```sh
mkdir -p /etc/
echo '" /usr/share/vim/vimfiles/archlinux.vim' > /etc/vimrc
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
endif' >> /etc/vimrc
```

### user group access (qemu-chroot)

```sh
groupadd -fr video
groupadd -fr lock
groupadd -fr uucp
groupadd -fr tty

gpasswd -a alarm video
gpasswd -a alarm lock
gpasswd -a alarm uucp
gpasswd -a alarm tty
```

--------------------------------------------------------------------------------

## Xorg Configuration

### fbdev config file (qemu-chroot)

```sh
echo 'Section "Device"
    Identifier    "FBDEV"
    Driver        "fbdev"
    Option        "fbdev" "/dev/fb0"
    Option        "SwapbufferWait" "true"
EndSection' > /etc/X11/xorg.conf.d/99-fbdev.conf
```

### xorg no blank (qemu-chroot)

```sh
echo 'Section "ServerFlags"
    Option "StandbyTime" "0"
    Option "SuspendTime" "0"
    Option "OffTime" "0"
    Option "BlankTime" "0"
EndSection' >  /etc/X11/xorg.conf.d/noblank.conf
```

### configure gtk theme (qemu-chroot)

```sh
mkdir -pv /etc/gtk-2.0/
echo '
gtk-icon-theme-name = "Papirus-Light"
gtk-theme-name = "Arc-Lighter-solid"
gtk-font-name = "Liberation Sans 8"
' | tee /etc/gtk-2.0/gtkrc

mkdir -pv /etc/gtk-3.0/
echo '
[Settings]
gtk-icon-theme-name = Papirus-Light
gtk-theme-name = Arc-Lighter-solid
gtk-font-name = Liberation Sans 8
gtk-application-prefer-dark-theme = false
' | tee /etc/gtk-3.0/settings.ini
```

--------------------------------------------------------------------------------

## User Configuration

### configure bash (qemu-chroot)

```sh
echo "alias sudo='sudo -E'
alias htop='htop -C'
alias mc='mc --nocolor'
export MAKEFLAGS=-j$(nproc)
alias makepkg='makepkg --nocheck --skippgpcheck'
alias bat='bat --theme=GitHub'
PS1='\[\033[01m\][\u@\h \W]\$ \[\033[00m\]'
" | tee -a /home/alarm/.bashrc
chown -vf alarm:alarm /home/alarm/.bashrc
```

```sh
echo '
[[ -f ~/.bashrc ]] && . ~/.bashrc
source ~/.bashrc

if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    echo "SSH Login Success"
else
    if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
        # for idle cli or tigervnc
        true

        # for runnable scripts
        #bash ~/script.sh

        # for runnable gui
        #startx /path/program
    fi
fi' | tee /home/alarm/.bash_profile
chown -vf alarm:alarm /home/alarm/.bash_profile
```

### configure gitk (qemu-chroot)

```sh
mkdir -p /home/alarm/.config/git/
echo 'set mainfont {{Liberation Sans} 8}
set textfont {{LiterationMono Nerd Font} 8}
set uifont {{Liberation Sans} 8 bold}' > /home/alarm/.config/git/gitk
chown -Rvf alarm:alarm /home/alarm/.config/
```

### configure xterm (qemu-chroot)

```sh
echo "XTerm*faceName: LiterationMono Nerd Font Mono
XTerm*faceSize: 8
XTerm*background: white
XTerm*foreground: black
XTerm*selectToClipboard: true
XTerm*eightBitInput: false
XTerm*eightBitOutput: true
Xft.autohint: 0
Xft.antialias: 1
Xft.hinting: true
Xft.hintstyle: hintslight
Xft.dpi: 96
Xft.rgba: rgb
Xft.lcdfilter: lcddefault" | tee /home/alarm/.Xdefaults
chown -vf alarm:alarm /home/alarm/.Xdefaults
```

--------------------------------------------------------------------------------

## Clean-Up

### package cache (qemu-chroot)

```sh
rm -vf /home/alarm/archmate-openbox*
rm -vf /home/alarm/{upgrade_pkgs.txt,install_pkgs.txt}
rm -vf /home/alarm/{basiclist.txt,openboxlist.txt}
rm -vf /home/alarm/{morelist.txt,serverlist.txt}
rm -vf /var/cache/pacman/pkg/*
```

### exit from mounted sdcard chroot (qemu-chroot)

```sh
exit
```

### umount disk (host-pc)

```sh
sudo umount /mnt/mmc/root/boot/
sudo umount /mnt/mmc/root/
```

### clear url list files (host-pc)

```sh
rm -vf dbase.txt upgrade_pkgs.txt install_pkgs.txt
```
