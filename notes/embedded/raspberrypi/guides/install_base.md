# RaspberryPi Base Installation

## Disk Install

### prepare disk

```sh
lsblk -f -o NAME,FSTYPE
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
lsblk -f -o NAME,FSTYPE
export DEVDISK='/dev/sdb'
```

```sh
echo ${DEVDISK}

sudo mkdir -p /mnt/mmc/{boot,root}
sudo mount ${DEVDISK}1 /mnt/mmc/boot
sudo mount ${DEVDISK}2 /mnt/mmc/root
```

```sh
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
lsblk -f -o NAME,FSTYPE
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

### arch-linux logo (qemu-chroot)

```sh
echo '
                    -@
                   .##@
                  .####@
                  @#####@
                . *######@
               .##@o@#####@
              /############@
             /##############@
            @######@**%######@
           @######`     %#####o
          @######@       ######%
        -@#######h       ######@.`
       /#####h**``       `**%@####@
      @H@*`                    `*%#@
     *`                            `*
' > /etc/motd
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
rm -rvf databases/
mkdir -p databases/
cd databases/

echo "
http://mirror.archlinuxarm.org/armv7h/core/core.db
http://mirror.archlinuxarm.org/armv7h/extra/extra.db
http://mirror.archlinuxarm.org/armv7h/community/community.db
http://mirror.archlinuxarm.org/armv7h/alarm/alarm.db
http://mirror.archlinuxarm.org/armv7h/aur/aur.db
" > ../dbase.txt
wget -c -i ../dbase.txt
cd ../
```

```sh
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

rm -rvf packages/official/
mkdir -p packages/official/
cd packages/official/

wget -c -i ../../upgrade_pkgs.txt

cd ../../
```

```sh
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

wget -c -i ../../install_pkgs.txt

cd ../../
```

```sh
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
pacman -U --noconfirm /home/alarm/archmate-openbox-0.1-1-any.pkg.tar.zst
```

### copy font configuration (host-pc)

```sh
sudo cp -vf ../archrpi/archfont.conf /mnt/mmc/root/etc/fonts/
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
ExecStart=-/sbin/agetty --autologin alarm --noclear %I 38400 linux
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
export PAGER=less
export VIEWER=less
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export FT2_SUBPIXEL_HINTING=2
export FZF_DEFAULT_COMMAND="rg --files"
export FZF_DEFAULT_OPTS="-m"
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
syntax on' >> /etc/vimrc
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

### dkms directory (qemu-chroot)

```sh
cd /usr/lib/modules/$(uname -r)/build/arch/
ln -svf arm armv7l
cd -
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

### configure font (qemu-chroot)

```sh
export FONTCONFLS="
10-scale-bitmap-fonts.conf
10-no-sub-pixel.conf
10-unhinted.conf
10-autohint.conf
10-hinting-none.conf
10-hinting-full.conf
10-hinting-medium.conf
10-hinting-slight.conf
10-sub-pixel-bgr.conf
10-sub-pixel-rgb.conf
10-sub-pixel-vbgr.conf
10-sub-pixel-vrgb.conf
11-lcdfilter-light.conf
11-lcdfilter-legacy.conf
11-lcdfilter-default.conf
70-no-bitmaps.conf"

for i in `echo $FONTCONFLS`;do
    ln -sf /usr/share/fontconfig/conf.avail/$i /etc/fonts/conf.d/$i
done

fc-cache -f > /dev/null
mkfontscale /usr/share/fonts/TTF
mkfontdir /usr/share/fonts/TTF
gdk-pixbuf-query-loaders --update-cache
```

--------------------------------------------------------------------------------

## User Configuration

### configure bash (qemu-chroot)

```sh
echo '[[ $- != *i* ]] && return' | tee /home/alarm/.bashrc
echo "
shopt -s checkwinsize
shopt -s histappend
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias sudo='sudo -E'
alias makepkg='makepkg --nocheck --skippgpcheck'
alias htop='htop -C'
alias mc='mc --nocolor'
alias bat='bat --theme=ansi'
export MAKEFLAGS=-j$(nproc)
export HISTCONTROL=ignorespace:ignoredups:erasedups
export REPOURL='http://mirror.internode.on.net/pub/archlinux'
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
xterm*scrollBar: true
xterm*rightScrollBar: true
UXTerm*faceName: LiterationMono Nerd Font Mono
UXTerm*faceSize: 8
UXTerm*background: white
UXTerm*foreground: black
UXTerm*selectToClipboard: true
UXTerm*eightBitInput: false
UXTerm*eightBitOutput: true
uxterm*scrollBar: true
uxterm*rightScrollBar: true
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

### clean URL lists (host-pc)

```sh
rm -vf *.txt
exit
```

