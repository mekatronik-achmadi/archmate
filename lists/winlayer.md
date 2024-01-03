# Windows Layer Packages

## Official

### install wine

wine wine-mono wine_gecko
samba smbclient vkd3d
winetricks msitools
cabextract icoutils

### install wine lib32

lib32-alsa-plugins lib32-alsa-lib lib32-libjpeg-turbo
lib32-libxslt lib32-gst-plugins-base-libs lib32-vkd3d
lib32-giflib lib32-libpng lib32-libldap lib32-gnutls
lib32-sdl2 lib32-v4l-utils lib32-libpulse lib32-mesa
lib32-libxcomposite lib32-libxinerama lib32-ncurses
lib32-mpg123 lib32-openal lib32-gtk3 lib32-gtk2

--------------------------------------------------------------------------------

## AUR

### install wine additional

- https://aur.archlinux.org/packages/icoextract/

--------------------------------------------------------------------------------

## Configurations

### wine no LD_PRELOAD

```sh
echo "" >> ~/.bashrc
echo '#Wine without LD_PRELOAD' >> ~/.bashrc
echo "alias wine='LD_PRELOAD= wine'" >> ~/.bashrc
```

### wine command prompt cmd

```sh
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine
winetricks settings winxp

wineconsole cmd
wineconsole --backend=user cmd
```

### wine improve font

```sh
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine
winetricks settings winxp
winetricks corefonts
```

```sh
winetricks fontsmooth=gray
winetricks fontsmooth=bgr
winetricks fontsmooth=rgb
```
