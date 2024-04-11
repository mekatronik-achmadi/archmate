# Railworks-3 on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/railworks
export WINEARCH=win32
export WINEPREFIX=$WINEDIR
```

```sh
winetricks settings winxp
winetricks settings fontsmooth=bgr
```

## Setup DirectX

```sh
wine directx_Jun2010_redist/DXSETUP.exe
```

## Install Games

### RW3 Version

```sh
cd Railworks/
sudo mount Railworks_3.iso /mnt/

cd /mnt
wine Setup.exe

cd -
sudo umount /mnt
```

### SKidrow version (Recommended)

Install Path: **C:\Railworks**

```sh
cd Railworks/
sudo mount sr-r3ts12.iso /mnt/

cd /mnt
wine Setup.exe

export TARGETDIR=$WINEDIR/drive_c/Railworks
cp -vf /mnt/SKIDROW/SKIDROW.ini $TARGETDIR/
cp -vf /mnt/SKIDROW/RailWorks.exe $TARGETDIR/
cp -vf /mnt/SKIDROW/Steamclient.dll $TARGETDIR/
cp -vf /mnt/SKIDROW/LocalisedStrings.dll $TARGETDIR/

cd -
sudo umount /mnt
```

## Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee railworks.reg

regedit railworks.reg
```

## Run Games

### RW-3 version

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/railworks
export WINEPREFIX=$WINEDIR

cd "$WINEDIR/drive_c/Program Files/Railworks 3/"
wine "Railworks.exe"
```

### Skidrow version (Recommended)

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/railworks
export WINEPREFIX=$WINEDIR

cd $WINEDIR/drive_c/Railworks/
wine "Railworks.exe"
```

### Some Worked Addons

- https://steamcommunity.com/app/24010/discussions/3/1700542332319483278/
- http://www.trensim.com/lib/rs/

