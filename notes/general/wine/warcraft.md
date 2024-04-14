# Warcraft-3 on Wine

## Setup Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/warcraft
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

```sh
cd Warcraft
sudo mount WC3_v1.29.iso /mnt/

cd /mnt
wine setup.exe

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
' | tee warcraft.reg

regedit warcraft.reg
```

## Run Games

```sh
unset LD_PRELOAD
export WINEDIR=/home/development/Virtuals/WineDir/warcraft
export WINEPREFIX=$WINEDIR

cd "$WINEDIR/drive_c/Program Files/Warcraft 3/"

sudo unshare -n sudo -E -u $USER \
wine "Warcraft III.exe"
```

## Some Keys

```
Warcraft 3
----------------

N9UBI4-GRQS-TDV29O-QF8H-7SMKLM
1YREOT-636V-59GAGA-8SYH-7FBJ43
JAXDO1-2Z6F-G7NZTI-H0QK-BE543P
CFMOSV-X0WD-U17ITP-RVPR-UTX4YP
QA1GX3-2UBS-6BM34T-Z7NO-P0H2W5

Warcraft 3: The Frozen Throne
----------------

WGMNX2-EGT7-8KD9EV-H6ZR-ZPH7PZ
B47XWP-VTNP-HHXZZF-DJ4B-MMFGPX
ZP944Z-8W4D-FJ4YCR-GGYV-2F6DHE
8NBFN2-KZHW-CXGJTM-2CJ4-FH4GWB
ETHTR9-FM7Z-DN84YW-F2JB-2DHMVY
```
