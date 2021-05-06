##### install base system
linux base base-devel
linux-headers linux-firmware
multilib-devel terminus-font

##### install base tools
bash-completion mkinitcpio
squashfs-tools rsync zsync
cdrtools archiso syslinux
dkms arch-install-scripts
neofetch lsb-release dtc
nano dialog bc tmux tree
nano-syntax-highlighting
curl wget openssh sshfs
intel-ucode amd-ucode
mkinitcpio-archiso

##### install posix meta
posix posix-software-development
posix-xsi posix-c-development

##### install cli tools
ranger lynx
moc atool most
python lua perl
fdupes w3m imlib2
poppler highlight
mediainfo libcaca

##### install cli editor
vim vim-jedi
vim-nerdcommenter
vim-ctrlp vim-nerdtree
vim-airline vim-surround
vim-tagbar vim-ultisnips

##### install xorg server
xorg xorg-apps xorg-drivers
xorg-xinit xorg-fonts

##### install login manager
lightdm lightdm-gtk-greeter
lightdm-gtk-greeter-settings

##### install install mate-desktop
mate mate-extra zenity
ttf-liberation onboard
parcellite meld ghex
redshift python-xdg
gnome-disk-utility
xdg-user-dirs-gtk
ghostwriter xchm
mypaint shotwell
ttf-inconsolata
qt5ct xdotool
dconf-editor
python-caja
ttf-dejavu

##### install gtk libraries
gtk2 gtk3 glade
python-wxpython
python-gobject
wxgtk2 wxgtk3
gtkmm gtkmm3

##### install themes and icons
gnome-icon-theme-extras gnome-themes-extra
arc-solid-gtk-theme papirus-icon-theme
gtk-engines gtk-engine-murrine

##### install networking system
networkmanager nm-connection-editor
network-manager-applet modemmanager
mobile-broadband-provider-info iftop
bind-tools netctl ppp wpa_supplicant
traceroute wavemon mtr bmon nethogs
tcpdump fping gnu-netcat inetutils
net-tools bridge-utils iwd ethtool
crda wireless_tools usb_modeswitch
iw gnome-keyring dhclient dnsmasq

##### install audio system
alsa-lib alsa-plugins
alsa-utils alsa-firmware
portaudio pavucontrol jack
pulseaudio pulseaudio-equalizer
pulseaudio-alsa pulseaudio-bluetooth
libcanberra-pulse sound-theme-freedesktop

##### install gio filesystem
gvfs gvfs-mtp gvfs-google
gvfs-gphoto2 gvfs-afc
gvfs-smb gvfs-nfs

##### install compression tools
lrzip lzip lzop zip unzip zstd
tar libarchive unrar lxsplit
xz bzip2 gzip lz4 p7zip arj
unarj lhasa cpio rpmextract

##### install build tools
npm yarn nodejs
subversion mercurial
git tig tk bzr cvs cloc
vala autogen pkg-config
gnome-common mate-common
pkgconf gendesk help2man
autoconf automake cscope
cmake extra-cmake-modules
dos2unix doxygen graphviz
jre8-openjdk jdk8-openjdk
tcsh gobject-introspection
meson ninja qt5-base setconf

##### install clang compiler
clang llvm lld
boost swig sip
shiboken2 eigen

##### install python installer
cython python-setuptools
python-wheel python-pip
python-distutils-extra

#### install internet tools
firefox thunderbird
firefox-dark-reader
firefox-ublock-origin
qbittorrent filezilla
uget aria2 wkhtmltopdf

##### install bluetooth support
blueman bluez
bluez-utils

##### install multimedia
cheese guvcview ffmpeg
gstreamer gst-libav
ffmpegthumbnailer
gst-plugins-base
gst-plugins-good
gst-plugins-bad
vlc mplayer
rhythmbox

##### install cd-dvd tools
fuseiso mdf2iso
brasero bchunk
squashfuse
dvdauthor
vcdimager

##### install printing support
cups cups-pdf
ghostscript gsfonts
system-config-printer
gutenprint foomatic-db-engine
foomatic-db foomatic-db-nonfree

##### install system information
hardinfo hwloc hwinfo lshw
lm_sensors xsensors hddtemp
htop atop dstat libstatgrab
lsof nmon sysstat procps-ng
usbutils dmidecode hwdetect
hdparm sdparm smartmontools
linux-tools arandr read-edid
ltrace strace mesa-demos ccze

##### install disk tools
ntfs-3g exfat-utils
gparted dosfstools
gpart e2fsprogs
gptfdisk mtools

###### install vbox guest
virtualbox-guest-utils
virtualbox-guest-dkms

##### install boot system
grub os-prober
efibootmgr
edk2-shell
edk2-ovmf

--------------------------------------------------------------------------------

##### install additional mate desktop
- gtk3-nocsd-git: https://aur.archlinux.org/packages/gtk3-nocsd-git/
- python-polib: https://aur.archlinux.org/packages/python-polib/
- caja-rename: https://aur.archlinux.org/packages/caja-rename/
- mate-tweak: https://aur.archlinux.org/packages/mate-tweak/
- brisk-menu: https://aur.archlinux.org/packages/brisk-menu/

##### install ms fonts
- ttf-tahoma: https://aur.archlinux.org/packages/ttf-tahoma/
- ttf-ms-fonts: https://aur.archlinux.org/packages/ttf-ms-fonts/
- ttf-vista-fonts: https://aur.archlinux.org/packages/ttf-vista-fonts/

##### install additional tools
- inxi: https://aur.archlinux.org/packages/inxi/
- git-cola: https://aur.archlinux.org/packages/git-cola/ (--nocheck)
- pandoc-bin: https://aur.archlinux.org/packages/pandoc-bin/
- fake-hwclock: https://aur.archlinux.org/packages/fake-hwclock/
- qt5-styleplugins: https://aur.archlinux.org/packages/qt5-styleplugins/

##### install additional programming tools
- clang-bear: https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/clang-bear/
- vim-addons: https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vim-addons/

###### install vim-coc plugins
- vim-coc-git: https://aur.archlinux.org/packages/vim-coc-git/
- vim-coc-pairs-git: https://aur.archlinux.org/packages/vim-coc-pairs-git/
- vim-coc-snippets-git: https://aur.archlinux.org/packages/vim-coc-snippets-git/
- vim-coc-highlight-git: https://aur.archlinux.org/packages/vim-coc-highlight-git/
- vim-coc-sh-git: https://aur.archlinux.org/packages/vim-coc-sh-git/
- vim-coc-clangd-git: https://aur.archlinux.org/packages/vim-coc-clangd-git/
- vim-coc-pyright-git: https://aur.archlinux.org/packages/vim-coc-pyright-git/
- vim-coc-ultisnips: https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vimcoc-ultisnips/

##### install archmate
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/custom/

~~~
archmate-font
archmate-icon
archmate-theme
archmate-default
archmate-archiso
archmate-install
~~~

--------------------------------------------------------------------------------

##### configure timezone

~~~
sudo ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
~~~

