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
winetricks corefonts
winetricks settings winxp
winetricks settings fontsmooth=bgr
```

## Setup DirectX

```sh
wine directx_Jun2010_redist/DXSETUP.exe
```

## Install Games

```sh
cd Railworks/
sudo mount Railworks_3.iso /mnt/

cd /mnt
wine Setup.exe

cd -
sudo umount /mnt
```

## Setup Registry

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/railworks
export WINEPREFIX=$WINEDIR

echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee railworks.reg

regedit railworks.reg
```

## Run Games

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/railworks
export WINEPREFIX=$WINEDIR

cd "$WINEDIR/drive_c/Program Files/Railworks 3/"
wine "Railworks.exe"
```
