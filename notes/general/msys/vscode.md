#  VSCode in MSYS2

# Download install

VSCode: https://code.visualstudio.com/download

## Settings

Setting file located at **%APPDATA%\Roaming\Code\User\settings.json**

```json
{
  "C_Cpp.intelliSenseEngine": "default",
  "C_Cpp.autocompleteAddParentheses": true,
  "C_Cpp.default.compileCommands": "compile_commands.json",
  "clangd.arguments": [
    "-header-insertion=never"
  ],
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
  "extensions.ignoreRecommendations": true,
  "files.trimTrailingWhitespace": true,
  "files.enableTrash": false,
  "git.openRepositoryInParentFolders": "never",
  "git.enableSmartCommit": true,
  "security.workspace.trust.untrustedFiles": "open",
  "terminal.integrated.fontSize": 10,
  "terminal.integrated.gpuAcceleration": "canvas",
  "debug.console.wordWrap": false,
  "workbench.startupEditor": "none",
  "workbench.colorTheme": "Default Light+",
  "window.restoreWindows": "none",
  "telemetry.telemetryLevel": "off",
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  "workbench.activityBar.location": "hidden",
  "window.commandCenter": false,
  "window.titleBarStyle": "native",
  "update.mode": "none",
  "terminal.integrated.profiles.windows": {
    "msys64": {
      "path": "C:\\msys64\\usr\\bin\\bash.exe",
      "args": ["--login","-i"],
      "env": {
        "MSYSTEM": "MINGW64",
        "CHERE_INVOKING": "1",
        "MSYS2_PATH_TYPE": "inherit"
      }
    }
  },
  "terminal.integrated.defaultProfile.windows": "msys64",
}
```

## Setup extensions

```sh
code --list-extensions

code --force --install-extension ms-python.python
code --force --install-extension ms-python.vscode-pylance
code --force --install-extension ms-vscode.cpptools
code --force --install-extension cschlosser.doxdocgen
code --force --install-extension mads-hartmann.bash-ide-vscode

code --force --install-extension oderwat.indent-rainbow
code --force --install-extension pkief.material-icon-theme
code --force --install-extension tejasvi.rainbow-brackets-2
code --force --install-extension wayou.vscode-todo-highlight

code --force --install-extension rust-lang.rust-analyzer
```

```sh
# not really recommended as it may difficult to use

code --force --install-extension vscodevim.vim
code --force --install-extension ms-pyright.pyright
```

## PlatformIO extension

```sh
code --force --install-extension platformio.platformio-ide
code --force --install-extension ms-vscode.vscode-serial-monitor
```
