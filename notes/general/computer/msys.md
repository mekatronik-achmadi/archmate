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
- Git-Cola: https://git-cola.github.io/downloads.html
- VSCodium: https://github.com/VSCodium/vscodium/releases/

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
base base-devel vim neofetch
git tig winpty bash-completion
nano openssh mc unrar zip p7zip
")
```

### basic profile

```sh
echo '
export PATH=$PATH:~/.local/bin
export VISUAL=vim
export EDITOR=vim
export PAGER=less
export VIEWER=less
' | tee /etc/profile.d/msys_profile.sh

echo '[[ $- != *i* ]] && return' |  tee ~/.bashrc
echo "
shopt -s checkwinsize
shopt -s histappend
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias makepkg='makepkg --nocheck --skippgpcheck'
alias less='less -N'
alias mc='mc --nocolor'
export MAKEFLAGS=-j$(nproc)
export HISTCONTROL=ignorespace:ignoredups:erasedupsT
" | tee -a ~/.bashrc
```

### additional devel packages

```sh
pacman -S $(echo "
mingw-w64-x86_64-python
mingw-w64-x86_64-cython0
mingw-w64-x86_64-python-pip
mingw-w64-x86_64-ctags
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

## Vim

### install vim plug

```sh
mkdir -p ~/.vim/autoload/
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "call plug#begin('~/.vim/pack/plug/start')
call plug#end()" | tee ~/.vimrc

mkdir -p ~/.vim/pack/plug/start/

vim +PlugStatus
```

### configurations

**NOTE:** Ultisnips are problematic in Windows

```sh
echo "
call plug#begin('~/.vim/pack/plug/start')
    Plug 'preservim/nerdcommenter'
    Plug 'preservim/nerdtree'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'airblade/vim-gitgutter'
    Plug 'godlygeek/tabular'
    Plug 'preservim/tagbar'
    Plug 'chrisbra/csv.vim'
\"    Plug 'SirVer/ultisnips'
    Plug 'honza/vim-snippets'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

let g:coc_data_home = 'C:\\\\msys64\\\\home\\\\$USER\\\\.config\\\\coc'

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \\: \"\\<C-g>u\\<CR>\\<c-r>=coc#on_enter()\\<CR>\"

hi CocFloating ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow
hi CocInlayHint ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow

autocmd BufWritePre * %s/\s\+$//e
filetype plugin on
filetype indent on
filetype plugin indent on
set expandtab ts=4 sw=4 ai
set conceallevel=0
set encoding=utf-8
set termguicolors
set ic is hls
set number
set wrap!
set mouse=a
let g:tagbar_width=20
let g:NERDTreeWinSize=20
syntax on" | tee ~/.vimrc
```

### install plugins

```sh
pacman -S $(echo "
mingw-w64-x86_64-jq
mingw-w64-x86_64-yarn
mingw-w64-x86_64-nodejs
")
```

```sh
vim +PlugInstall
vim -c "CocInstall coc-pairs coc-snippets coc-json"
vim -c "CocInstall coc-clangd coc-jedi coc-tsserver"
vim +PlugClean

echo "For editing PKGBUILD"
echo ":set ft=PKGBUILD"
```

```sh
mkdir -p ~/.vim

jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"] |
."snippets.ultisnips.enable"=false
' > ~/.vim/coc-settings.json

vim ~/.vim/coc-settings.json
```

## VSCodium

### marketplace

Product file located at: **%ProgramFiles%/VSCodium/resources/app/product.json**

```json
{
  "extensionsGallery": {
    "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
    "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
    "itemUrl": "https://marketplace.visualstudio.com/items"
  },
}
```

### settings

Setting file located at **%APPDATA%\Roaming\VSCodium\User\settings.json**

```json
{
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
  "telemetry.telemetryLevel": "off",
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  "workbench.activityBar.location": "hidden",
  "window.commandCenter": false,
  "window.titleBarStyle": "native",
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
}
```

### extensions

```sh
vscodium --list-extensions

#vscodium --force --install-extension vscodevim.vim
#vscodium --force --install-extension ms-pyright.pyright

vscodium --force --install-extension cschlosser.doxdocgen
vscodium --force --install-extension ms-vscode.cpptools
vscodium --force --install-extension ms-python.python
vscodium --force --install-extension mads-hartmann.bash-ide-vscode

```

### arduino/platformio

```sh
vscodium --force --install-extension platformio.platformio-ide
vscodium --force --install-extension vsciot-vscode.vscode-arduino
vscodium --force --install-extension ms-vscode.vscode-serial-monitor
```

Optional settings to **%APPDATA%\Roaming\VSCodium\User\settings.json**

```json
"arduino.path": "/usr/bin/",
"arduino.commandPath": "arduino-cli",
"arduino.useArduinoCli": true,
"arduino.enableUSBDetection": true,
"arduino.logLevel": "verbose",
```
