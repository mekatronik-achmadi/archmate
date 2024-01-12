# Other Packages

## AUR

### nvidia

#### nvidia-470 (utils,dkms,opencl)

- https://aur.archlinux.org/packages/nvidia-470xx-utils/
- https://aur.archlinux.org/packages/lib32-nvidia-470xx-utils/

#### nvidia-optimus

- https://aur.archlinux.org/packages/optimus-manager/

### install internet tools

- https://aur.archlinux.org/packages/google-chrome/
- https://aur.archlinux.org/packages/teamviewer/

## install visual studio code

- https://aur.archlinux.org/packages/visual-studio-code-bin/
- https://aur.archlinux.org/packages/visual-studio-code-cli-bin/

## install academic tools

- https://aur.archlinux.org/packages/rstudio-desktop-bin/
- https://aur.archlinux.org/packages/mendeleydesktop-bundled/

--------------------------------------------------------------------------------

## External

### install matlab binary

- https://github.com/mekatronik-achmadi/archmate/tree/master/pkgbuilds/unused/matlab-bin-basic/

### install cadsoft eagle

- https://aur.archlinux.org/packages/openssl-1.0/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/eaglecad/

### install internet tool

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/discord/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/packettracer/

--------------------------------------------------------------------------------

## Configurations

### configure nvidia

#### optimus manager

```sh
sudo systemctl disable bumblebeed
sudo systemctl enable optimus-manager
sudo reboot
```

```sh
# clear switching errors
prime-offload

optimus-manager --no-confirm --switch hybrid
optimus-manager --no-confirm --switch intel
```

#### disable nvidia gpu

```sh
echo '
blacklist nouveau
blacklist nvidia
options nouveau modeset=0' | sudo tee /etc/modprobe.d/blacklist-nvidia.conf

echo '
# Remove NVIDIA USB xHCI Host Controller devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA USB Type-C UCSI devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA Audio devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{power/control}="auto", ATTR{remove}="1"
# Remove NVIDIA VGA/3D controller devices
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x03[0-9]*", ATTR{power/control}="auto", ATTR{remove}="1"' | \
sudo tee /etc/udev/rules.d/00-remove-nvidia.rules

sudo systemctl disable optimus-manager
sudo reboot

lsmod | grep nvi
lsmod | grep nou
lspci | grep -i nvidia
```

### configure matlab

```sh
echo "09806-07443-53955-64350-21751-41297"
```

```sh
sudo mount R2018a_glnxa64_dvd1.iso /mnt/
/mnt/install &
sudo umount /mnt/
sudo mount R2018a_glnxa64_dvd2.iso /mnt/
```

```sh
# install folder: /home/developments/Packages/Matlab-2018a/built/matlab-2018a/
cd /home/developments/Packages/Matlab-2018a/built/
ls matlab-2018a/
mv -vf ./matlab-2018a/ matlab-bin-basic/matlab-2018a/
cd matlab-bin-basic/
makepkg -sir
sudo pacman -S libxcrypt-compat
```

```sh
sudo cp libmwlmgrimpl.so /opt/mathworks/matlab-2018a/bin/glnxa64/matlab_startup_plugins/lmgrimpl/
sudo matlab
sudo chown -R $USER:users $HOME/.matlab/R2018a/
```

```sh
matlab-gui
cd /opt/mathworks/addons/schemer/
schemer_import
```

```sh
# fix graphic low level issue
echo "-Djogl.disable.openglarbcontext=1" | sudo tee -a /opt/mathworks/matlab-2018a/bin/glnxa64/java.opts
```

### configure teamviewer

```sh
sudo rm -f /usr/share/applications/teamviewerapi.desktop

sudo systemctl enable teamviewerd
sudo systemctl start teamviewerd
```

### configure cisco packet simulator

```sh
sudo ln -svf /opt/packettracer/packettracer /usr/bin/packettracer
```

### configure vscode

#### settings (windows/linux)

```sh
VSCONFDIR=~/.config/Code/User

mkdir -p "$VSCONFDIR"
echo "{}" > "$VSCONFDIR/settings.json"

jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."C_Cpp.intelliSenseEngine"="disabled" |
."doxdocgen.file.customTag"=["@addtogroup ","@{"] |
."doxdocgen.file.fileOrder"=["file","brief","empty","custom"] |
."editor.fontFamily"="'\''Liberation Mono'\''" |
."editor.fontSize"=10 |
."editor.minimap.enabled"=false |
."files.trimTrailingWhitespace"=true |
."files.enableTrash"=false |
."git.openRepositoryInParentFolders"="never" |
."terminal.integrated.fontSize"=10 |
."terminal.integrated.gpuAcceleration"="canvas" |
."debug.console.wordWrap"=false |
."workbench.startupEditor"="none" |
."workbench.activityBar.visible"=false |
."workbench.colorTheme"="Default Light+" |
."security.workspace.trust.untrustedFiles"="open" |
."window.restoreWindows"="none" |
."telemetry.enableTelemetry"=false |
."telemetry.enableCrashReporter"=false
' | tee "$VSCONFDIR/temp.json"

rm -f "$VSCONFDIR/settings.json"
mv "$VSCONFDIR/temp.json" "$VSCONFDIR/settings.json"

cat "$VSCONFDIR/settings.json"
```

#### extension (windows/linux)

```sh
code --list-extensions

#code --force --install-extension vscodevim.vim
#code --force --install-extension ms-pyright.pyright
code --force --install-extension cschlosser.doxdocgen
code --force --install-extension ms-python.python
```

#### windows terminal settings (windows-only)

```sh
code $WINDOWS_VSCODE_INSTALL_PATH/settings.json
```

```json
 "terminal.integrated.profiles.windows": {
    "msys64": {
        "path": "C:\\msys64\\usr\\bin\\bash.exe",
        "args": [
            "--login",
            "-i"
        ],
          "env": {
            "MSYSTEM": "MINGW64",
            "CHERE_INVOKING": "1"
        }
    },
},
"terminal.integrated.defaultProfile.windows": "msys64",
```

#### arduino-platformio (windows-only)
-
```sh
code --list-extensions

code --force --install-extension ms-vscode.cpptools
code --force --install-extension platformio.platformio-ide
code --force --install-extension vsciot-vscode.vscode-arduino
code --force --install-extension ms-vscode.vscode-serial-monitor
```

```sh
VSCONFDIR=~/.config/Code/User

jq '
."C_Cpp.intelliSenseEngine"="default" |
."arduino.commandPath"="arduino-cli" |
."arduino.enableUSBDetection"=true |
."arduino.logLevel"="verbose" |
."arduino.path"="/usr/bin/" |
."arduino.useArduinoCli"=true
' "$VSCONFDIR/settings.json" | tee "$VSCONFDIR/temp.json"

rm -f "$VSCONFDIR/settings.json"
mv "$VSCONFDIR/temp.json" "$VSCONFDIR/settings.json"

cat "$VSCONFDIR/settings.json"
-```
