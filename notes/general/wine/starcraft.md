# Starcraft-2 on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/starcraft
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

Install path: **Z:\home\development\Virtuals\WineDir\Games\StarCraft**

```sh
cd Starcraft/
wine setup.exe
```

## Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee starcraft.reg

regedit starcraft.reg
```

## Run Games

**NOTE:** Must be no internet to play.

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/starcraft
export WINEPREFIX=$WINEDIR

cd /home/development/Virtuals/WineDir/Games/StarCraft
wine *Offline.exe
```

## Crack Game (Optional)

Account tag: **dlr@dr.com**

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/starcraft
export WINEPREFIX=$WINEDIR

cd /home/development/Virtuals/WineDir/Games/StarCraft
wine cmd /c "Run me first.bat"
```
