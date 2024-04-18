# CnC RedAlert-2 on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/redalertold
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
cd RedAlertOld/
unrar x 'Command.&.Conquer.Red.Alert.II.rar'

cd "Command.&.Conquer.Red.Alert.II/game"
wget -c https://github.com/FunkyFr3sh/cnc-ddraw/releases/latest/download/cnc-ddraw.zip
unzip cnc-ddraw.zip
wine "cnc-ddraw config.exe"
```

## Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005
' | tee redalertold.reg

regedit redalertold.reg
```

## Run Games

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/redalertold
export WINEPREFIX=$WINEDIR

cd "RedAlertOld/Command.&.Conquer.Red.Alert.II/game"
wine Ra2.exe
```
