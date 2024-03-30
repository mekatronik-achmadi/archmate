# MS Office on Wine

**NOTE:** Installation Failed

Set Wine 32-bit environment

```sh
unset LD_PRELOAD
mkdir -p /home/development/Virtuals/WineDir

export WINEDIR=/home/development/Virtuals/WineDir/office2016
export WINEARCH=win32
export WINEPREFIX=$WINEDIR
```

Setup Wine infrastructures

```sh
winetricks settings win7
winetricks settings fontsmooth=bgr

winetricks msxml3 msxml4
winetricks msxml6 corefonts

winetricks vd=1366x720
```

Setup DirectX

```sh
wine directx_Jun2010_redist/DXSETUP.exe
```

Install from mounted ISO

```sh
wine setup.exe
```

Setup Registry

```sh
echo 'REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\DllOverrides]
"riched20"="native,builtin"

[HKEY_CURRENT_USER\Software\Wine\Direct3D]
"DirectDrawRenderer"="opengl"
"UseGLSL"="enabled"
"MaxVersionGL"=dword:00030002
' | tee msoffice.reg

regedit msoffice.reg
```
