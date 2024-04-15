# CnC RedAlert-3 on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/redalert
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

**NOTE:** Ignore DX installer failure

```sh
cd RedAlert/

mkdir -p $WINEDIR/drive_c/
unzip CnC_RA3.zip -d $WINEDIR/drive_c/

cd "$WINEDIR/drive_c/Red Alert 3/"
wine cmd /c setup.bat
```

## Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee redalert.reg

regedit redalert.reg
```

## Run Games

**NOTE:** Must be no internet to play.

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/redalert
export WINEPREFIX=$WINEDIR

cd "$WINEDIR/drive_c/Red Alert 3/"
wine RA3.exe
```
