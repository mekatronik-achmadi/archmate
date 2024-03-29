# MS Office on Wine

**NOTE:** Installation Unsuccesful

Set Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/office2013
export WINEARCH=win32
export WINEPREFIX=$WINEDIR
```

Setup Wine infrastructures

```sh
winetricks msxml3 msxml4
winetricks msxml6 corefonts

winetricks settings win7
winetricks settings fontsmooth=bgr
```

Setup DirectX

```sh
wine directx_Jun2010_redist/DXSETUP.exe
```

Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\DllOverrides]
"riched20"="native,builtin"

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
' | tee msoffice.reg

regedit msoffice.reg
```

Mount and install from ISO

```sh
sudo mount Office2013/Office_2013_x86.iso /mnt
cd /mnt

wine setup.exe >/dev/null 2>&1

cd -
sudo umount /mnt
```

