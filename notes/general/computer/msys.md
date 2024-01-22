# MSYS Guidance

## Windows Recommendations

- 7Zip: https://www.7-zip.org/download.html
- LiberationFontsTTF: https://github.com/liberationfonts/liberation-fonts/releases/tag/2.1.5
- Firefox Browser: https://www.mozilla.org/id/firefox/all/#product-desktop-release
- Latest MSVC++: https://learn.microsoft.com/id-id/cpp/windows/latest-supported-vc-redist
- CopyQ: https://github.com/hluk/CopyQ/releases
- Ghostwriter: https://ghostwriter.kde.org/download/
- WinMerge: https://winmerge.org/downloads/?lang=en
- Notepad++: https://notepad-plus-plus.org/downloads/
- Git: https://git-scm.com/download/win
- VSCode: https://code.visualstudio.com/download/

## Installation

### base packages

Download: https://www.msys2.org/

Install as usual and Choose **MSYS2 MINGW64** as default profile.

To run from Windows' Run dialog (Windows+R)

```bat
C:\msys64\mingw64.exe
```

### add to Path Environment

- C:\msys64\usr\bin
- C:\msys64\mingw64\bin

### update/upgrade (optional)

```sh
pacman -Sy
pacman -Su --noconfirm
```

### basic packages

```sh
pacman -S $(echo "
base base-devel nano neofetch
git tig winpty bash-completion
")
```

### basic profile

```sh
echo "
export PATH=$PATH:~/.local/bin
export VISUAL=nano
export EDITOR=nano
export PAGER=less
export VIEWER=less
" | tee /etc/profile.d/msys_profile.sh
```

### additional devel packages

```sh
pacman -S $(echo "
mingw-w64-x86_64-python
mingw-w64-x86_64-cython0
mingw-w64-x86_64-python-pip
mingw-w64-x86_64-toolchain
mingw-w64-x86_64-clang-analyzer
mingw-w64-x86_64-clang-tools-extra
")
```

### gtk3 programming

```sh
pacman -S $(echo "
mingw-w64-x86_64-gtk3
mingw-w64-x86_64-gtkmm3
mingw-w64-x86_64-glade")
```

## CLang compile commands

```sh
pip install compiledb

compiledb gcc -o main main.c
compiledb make all
```

## VSCode

### settings

- %APPDATA%\Code\User\settings.json.

```json
{
  "clangd.arguments": [
    "-header-insertion=never"
  ],
  "C_Cpp.intelliSenseEngine": "default",
  "doxdocgen.file.customTag": [
    "@addtogroup ",
    "@{"
  ],
  "doxdocgen.file.fileOrder": [
    "file",
    "brief",
    "empty",
    "custom"
  ],
  "editor.fontFamily": "'Liberation Mono'",
  "editor.fontSize": 10,
  "editor.minimap.enabled": false,
  "files.trimTrailingWhitespace": true,
  "files.enableTrash": false,
  "git.openRepositoryInParentFolders": "never",
  "terminal.integrated.fontSize": 10,
  "terminal.integrated.gpuAcceleration": "canvas",
  "debug.console.wordWrap": false,
  "workbench.startupEditor": "none",
  "workbench.colorTheme": "Default Light+",
  "security.workspace.trust.untrustedFiles": "open",
  "window.restoreWindows": "none",
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  "workbench.activityBar.location": "hidden",
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
    }
  },
  "terminal.integrated.defaultProfile.windows": "msys64",
  "arduino.commandPath": "arduino-cli",
  "arduino.enableUSBDetection": true,
  "arduino.logLevel": "verbose",
  "arduino.path": "/usr/bin/",
  "arduino.useArduinoCli": true
}
```

### extension

```sh
# list installed
code --list-extensions

# generic
#code --force --install-extension vscodevim.vim
#code --force --install-extension ms-pyright.pyright
code --force --install-extension llvm-vs-code-extensions.vscode-clangd
code --force --install-extension cschlosser.doxdocgen
code --force --install-extension ms-python.python

# arduino/platformio
# clangd extension must be disabled
code --force --install-extension ms-vscode.cpptools
code --force --install-extension platformio.platformio-ide
code --force --install-extension vsciot-vscode.vscode-arduino
code --force --install-extension ms-vscode.vscode-serial-monitor
```
