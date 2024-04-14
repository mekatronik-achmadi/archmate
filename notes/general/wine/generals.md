# CnC Generals on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/generals
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

## Some Keys

```text
# Zero Hour Keys
64UU-HJLH-PJCK-M7AK-KUE9
PDWW-HYA4-TPQD-T8KT-ZC3J
PBVM-6LAP-T942-ASVR-WZZ5
P57F-BDA8-TRC6-AAYF-NP55
P322-KQAF-TDUR-LHK4-X259
PCG8-ZPAK-TVH4-K4VM-NHZ6
P3HZ-VXA4-TFUQ-LX9N-PAJM
PHLU-C7AY-TABD-4FF6-46P2
PJRZ-T5AE-TC8J-M9EL-588L
PVGY-5JA7-TR8J-GEE8-KXRQ
PP6E-65AY-TTGU-RPQ3-VVGA (used in example below)
4EFF-YZNG-6AS4-3QJQ-44YG (Jimbus edition)
```

## Install Games

```sh
cd Generals/
tar -xf setup.tar.gz
wine setup.exe
```

## Some Settings

```sh
mkdir -p "$HOME/Documents/Command and Conquer Generals Data/"
mkdir -p "$HOME/Documents/Command And Conquer Generals Zero Hour Data/"

echo '
AntiAliasing = 1
BuildingOcclusion = no
DrawScrollAnchor =
DynamicLOD = yes
ExtraAnimations = no
GameSpyIPAddress = 127.0.0.2
Gamma = 50
HeatEffects = no
IPAddress = 127.0.0.2
IdealStaticGameLOD = High
LanguageFilter = false
MaxParticleCount = 100
MoveScrollAnchor = 0
MusicVolume = 79
Resolution = 800 600
Retaliation = yes
SFX3DVolume = 79
SFXVolume = 71
ScrollFactor = 50
SendDelay = no
ShowSoftWaterEdge = no
ShowTrees = yes
StaticGameLOD = low
UseAlternateMouse = yes
UseCloudMap = no
UseDoubleClickAttackMove = yes
UseLightMap = no
UseShadowDecals = yes
UseShadowVolumes = no
VoiceVolume = 70
' | tee "$HOME/Documents/Command and Conquer Generals Data/Options.ini"

cp -vf "$HOME/Documents/Command and Conquer Generals Data/Options.ini" \
"$HOME/Documents/Command And Conquer Generals Zero Hour Data/"
```

## Setup Registry

```sh
regedit /D "HKEY_LOCAL_MACHINE\SOFTWARE\Electronic Arts\EA Games\Command and Conquer Generals Zero Hour\ergc"

echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00040005

[HKEY_LOCAL_MACHINE\SOFTWARE\Electronic Arts\EA Games\Command and Conquer Generals Zero Hour\ergc]
@="PP6E65AYTTGURPQ3VVGA"
' | tee generals.reg

regedit generals.reg
```

## Run Games

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/generals
export WINEPREFIX=$WINEDIR

cd "$WINEDIR/drive_c/Program Files/CnCGenerals/"
wine ZeroHour/generals.exe
```
