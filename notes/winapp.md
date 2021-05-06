## Wine Blocked Internet

#### setup

~~~
sudo groupadd -fr winenoinet
sudo iptables -I OUTPUT 1 -m owner --gid-owner winenoinet -j DROP
sudo ip6tables -I OUTPUT 1 -m owner --gid-owner winenoinet -j DROP
sudo gpasswd -a username winenoinet
~~~

#### usage

~~~
unset LD_PRELOAD
export WINEARCH=win32
sudo -g winenoinet LD_PRELOAD=  WINEPREFIX=~/WineDir/winefolder/ wine program.exe &> /dev/null
~~~

---------------------------------------------------------

## Registry

#### riched20.reg

~~~
REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\DllOverrides]
"riched20"="native,builtin"
~~~

#### gaming.reg

~~~
REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"csmt"=dword:00000001
"MaxVersionGL"=dword:00040005
~~~

#### vdesktop.reg

~~~
REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Explorer\Desktops]
"Default"="1024x768"
~~~

---------------------------------------------------------

## Real-Time Strategy Games

#### Starcraft-BW

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/winebw
winetricks settings winxp
regedit DX_Display/gaming.reg
wine DX_Display/directx/DXSETUP.exe
~~~

~~~
cd StarCraft_BW/
mkdir -p StarcraftBroodwar/
bsdtar --strip-components=1 -xvf Starcraft_BroodWar.zip -C StarcraftBroodwar/
~~~

~~~
cd StarCraft_BW/StarcraftBroodwar/
LD_PRELOAD=  WINEPREFIX=~/WineDir/winebw/ wine StarCraft.exe &> /dev/null
~~~

#### Starcraft-2

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/winesc
winetricks settings winxp
regedit DX_Display/gaming.reg
wine DX_Display/directx/DXSETUP.exe
~~~

~~~
cd StarCraft/
sudo mount rld-sciivoid.iso /mnt;cd /mnt
wine setup.exe

cp -rvf Crack/* "$HOME/.winesc/drive_c/Program Files/StarCraft_II/"
cd "~/WineDir/winesc/drive_c/Program Files/StarCraft_II/"
wine cmd /c "Run me first.bat"
chmod -Rvf u+w Battle.net/
~~~

~~~
cd "~/WineDir/winesc/drive_c/Program Files/StarCraft_II/"
LD_PRELOAD=  WINEPREFIX=~/WineDir/winesc/ wine "StarCraft II Offline.exe" &> /dev/null
~~~

#### Warcraft-3

##### Patch 1.29

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/winewc
winetricks settings winxp
regedit DX_Display/gl3d.reg
wine DX_Display/directx/DXSETUP.exe
~~~

~~~
cd Warcraft/
sudo mount WC3_v1.29.iso /mnt;cd /mnt
wine setup.exe

cd "~/WineDir/winewc/drive_c/Program\ Files/Warcraft\ 3/"
LD_PRELOAD= wine "Warcraft III.exe" &> /dev/null

echo "RoC: N9UBI4-GRQS-TDV29O-QF8H-7SMKLM"
echo "TFT: WGMNX2-EGT7-8KD9EV-H6ZR-ZPH7PZ"
~~~

~~~
cd "$HOME/WineDir/winewc/drive_c/Program Files/Warcraft 3/"
LD_PRELOAD=  WINEPREFIX=~/WineDir/winewc/ wine "Warcraft III.exe" &> /dev/null
~~~

##### Patch 1.26 + Dota

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/winewc
winetricks settings winxp
regedit DX_Display/gaming.reg
wine DX_Display/directx/DXSETUP.exe
~~~

~~~
cd Warcraft/
yes | unrar x WC3_Dota.rar
cd ../
~~~

~~~
cd Warcraft/Warcraft*/
LD_PRELOAD=  WINEPREFIX=~/WineDir/winewc/ wine "Frozen Throne.exe" &> /dev/null
~~~

## Simulation Games

#### Railworks 3

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/winerw/
winetricks settings winxp
regedit DX_Display/gl3d.reg
wine DX_Display/directx/DXSETUP.exe
~~~

~~~
cd Railworks/
sudo mount Railworks_3.iso /mnt/;cd /mnt/
wine Setup.exe
cd -;sudo umount /mnt
~~~

~~~
cd "$HOME/WineDir/winerw/drive_c/Program Files/Railworks 3/"
LD_PRELOAD=  WINEPREFIX=~/WineDir/winerw/ wine RailWorks.exe &> /dev/null
~~~

---------------------------------------------------------

## Microsoft Office

#### install MS-Office 2013

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine-office2013
winetricks msxml3 msxml4
winetricks msxml6 corefonts
winetricks settings winxp
wine DX_Display/directx/DXSETUP.exe
winetricks settings fontsmooth=bgr
regedit riched20.reg
regedit DX_Display/gaming.reg
LD_PRELOAD= wine setup.exe &> /dev/null
~~~

---------------------------------------------------------

## Programming

#### install Proteus 8.6

~~~
unset LD_PRELOAD
export WINEARCH=win32
export WINEPREFIX=~/WineDir/wine86
winetricks msxml3 msxml4
winetricks msxml6 corefonts
winetricks settings winxp
winetricks settings fontsmooth=bgr
regedit DX_Display/gaming.reg
wine DX_Display/directx/DXSETUP.exe
LD_PRELOAD= wine Proteus_8.6_SP2_Pro.exe &> /dev/null
~~~
