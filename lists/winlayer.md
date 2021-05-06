##### install wine
wine winetricks
cabextract icoutils
wine-mono wine_gecko
wine-nine samba vkd3d

##### install wine lib32
lib32-mpg123 lib32-openal lib32-v4l-utils lib32-libpulse
lib32-alsa-plugins lib32-alsa-lib lib32-libjpeg-turbo
lib32-libxslt lib32-gst-plugins-base-libs lib32-vkd3d
lib32-giflib lib32-libpng lib32-libldap lib32-gnutls
lib32-libxcomposite lib32-libxinerama lib32-ncurses
lib32-sdl2 lib32-mesa lib32-gtk3 lib32-gtk2

--------------------------------------------------------------------------------

##### install wine additional
- https://aur.archlinux.org/packages/msitools/
- https://aur.archlinux.org/packages/exe-thumbnailer/

--------------------------------------------------------------------------------

##### wine no LD_PRELOAD

~~~
echo "" >> ~/.bashrc
echo '#Wine without LD_PRELOAD' >> ~/.bashrc
echo "alias wine='LD_PRELOAD= wine'" >> ~/.bashrc
~~~

##### wine command prompt cmd

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine
winetricks settings winxp

wineconsole cmd
wineconsole --backend=user cmd

sudo ln -svf /usr/lib32/libncursesw.so.6 /usr/lib32/libncursesw.so.5
wineconsole --backend=curses cmd
~~~

##### wine improve font

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine
winetricks settings winxp
winetricks corefonts
~~~

~~~
winetricks fontsmooth=gray
winetricks fontsmooth=bgr
winetricks fontsmooth=rgb
~~~

