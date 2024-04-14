# Starcraft Remastered on Wine

## Download URLs

- https://www.elamigos-games.net/games/starcraft-remastered
- https://www.zpaste.net/p/kuhgc

## Setup Wine 64-bit environment

**NOTE:** Installer failed on 32-bit

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/remastered
export WINEARCH=win64
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

Install Path: **C:\Games\SCRemastered**

```sh
cd Remastered/
sudo mount SCRemastered_*.iso /mnt

cd /mnt
wine setup.exe

cd -
sudo umount /mnt

export TARGETDIR=$WINEDIR/drive_c/Games/SCRemastered
cp -rvf *_crackfix/* $TARGETDIR/
```

## Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee remastered.reg

regedit remastered.reg
```

## Run Games

**NOTE:** Must be no internet to play.

**NOTE:** Run again if failed to start

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/remastered
export WINEPREFIX=$WINEDIR

cd $WINEDIR/drive_c/Games/SCRemastered/
wine x86_64/StarCraft.exe
```
