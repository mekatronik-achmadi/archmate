# MSYS Guidance

## Windows Recommendations

- 7Zip: https://www.7-zip.org/download.html
- LiberationFontsTTF: https://github.com/liberationfonts/liberation-fonts/releases/tag/2.1.5
- Firefox Browser: https://www.mozilla.org/id/firefox/all/#product-desktop-release
- Latest MSVC++: https://learn.microsoft.com/id-id/cpp/windows/latest-supported-vc-redist
- CopyQ: https://github.com/hluk/CopyQ/releases
- Ghostwriter: https://ghostwriter.kde.org/download/
- MarkText: https://www.marktext.cc/
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
base base-devel gvim mc git tig bear
winpty neofetch bash-completion tmux
")
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
mingw-w64-x86_64-ttf-liberation-mono-nerd
mingw-w64-x86_64-nodejs mingw-w64-x86_64-yarn
")
```

### basic profile

```sh
echo "
export PATH=$PATH:~/.local/bin
export VISUAL=vim
export EDITOR=vim
export PAGER=less
export VIEWER=less
" | tee /etc/profile.d/msys_profile.sh
```

## Vim CoC

### install vim-plug

- https://github.com/junegunn/vim-plug/

```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "
call plug#begin('~/.vim/pack/plug/start')
call plug#end()" > ~/.vimrc

vim +PlugStatus
```

### install plugins

**WARNING:**  Python error on Vim Ultisnips

```sh
echo "
call plug#begin('~/.vim/pack/plug/start')
    Plug 'preservim/nerdcommenter'
    Plug 'preservim/nerdtree'
    Plug 'jlanzarotta/bufexplorer'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'airblade/vim-gitgutter'
    Plug 'godlygeek/tabular'
    Plug 'preservim/tagbar'
    Plug 'lervag/vimtex'
    Plug 'chrisbra/csv.vim'
\"    Plug 'ryanoasis/vim-devicons'
\"    Plug 'SirVer/ultisnips'
\"    Plug 'honza/vim-snippets'
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
let g:tagbar_width=30
let g:NERDTreeWinSize=30
syntax on
if has(\"gui_running\")
  set guifont=LiterationMono\ Nerd\ Font\ Mono\ 8
\"  colorscheme evening
endif" | tee ~/.vimrc
```

```sh
# install extensions
#node -v;cat ~/.vimrc
mkdir -p ~/.vim/pack/plug/start/

vim +PlugInstall
vim -c "CocInstall coc-pairs coc-snippets"
vim -c "CocInstall coc-sh coc-ultisnips"
vim -c "CocInstall coc-clangd coc-jedi"
vim -c "CocInstall coc-html coc-yaml"
vim -c "CocInstall coc-json coc-tsserver"
vim +PlugClean

echo "For editing PKGBUILD"
echo ":set ft=PKGBUILD"
```

```sh
mkdir -p ~/.vim

jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"]
' > ~/.vim/coc-settings.json

vim ~/.vim/coc-settings.json
```

## Generate Clangd compile_commands.json

```sh
bear -- gcc -o coba.exe coba.c
bear -- make -j$(nproc)
```

```sh
pip install compiledb

compiledb gcc -o coba.exe coba.c
compiledb make -j$(nproc)
```

### VSCode

#### settings

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

#### extension

```sh
code --list-extensions

#code --force --install-extension vscodevim.vim
#code --force --install-extension ms-pyright.pyright
#code --force --install-extension llvm-vs-code-extensions.vscode-clangd
code --force --install-extension cschlosser.doxdocgen
code --force --install-extension ms-python.python
code --force --install-extension ms-vscode.cpptools

code --force --install-extension platformio.platformio-ide
code --force --install-extension vsciot-vscode.vscode-arduino
code --force --install-extension ms-vscode.vscode-serial-monitor
```
