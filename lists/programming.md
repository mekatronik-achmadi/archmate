# Programming Packages

## Official

### install gitea server

gitea postgresql
memcached redis

### install qt programming

qt5 qt6 clazy sip python-qtpy pyqt-builder
python-pyqt5 pyside2 pyside2-tools
python-pyqt5-3d python-pyqt5-webengine
python-pyqt5-chart python-pyqt5-datavisualization
python-pyqt6 pyside6 pyside6-tools
python-pyqt6-3d python-pyqt6-webengine
python-pyqt6-charts python-pyqt6-datavisualization

### install qt graph additionals

qcustomplot qwt
python-pyqtgraph

### install c/c++ programming

rust rust-analyzer
rust-src rust-bindgen
rust-wasm cargo-generate
cargo-edit cargo-feature
tcsh boost swig valabind
clang llvm libc++ lld lldb
gdb gdb-dashboard cppcheck

### install javacript programming

nodejs npm yarn asar
bash-language-server
jq yq node-gyp ts-node

### install webassembly

emscripten rust-wasm
wasm-pack wasm-bindgen

--------------------------------------------------------------------------------

## AUR

### install qwt additionals

```sh
sed -i 's#-p1#-p0#g' PKGBUILD
```

- https://aur.archlinux.org/packages/qwt-qt6-svn/
- https://aur.archlinux.org/packages/python-pyqt-qwt/

### install programming tools

- https://aur.archlinux.org/packages/wxhexeditor/
- https://aur.archlinux.org/packages/wxformbuilder/

### install additional system python

- https://aur.archlinux.org/packages/python-ttkthemes/
- https://aur.archlinux.org/packages/python-wifiwrapper/
- https://aur.archlinux.org/packages/python-pyalsaaudio/

### install programming tools
- https://aur.archlinux.org/packages/noi-desktop-bin/
- https://aur.archlinux.org/packages/visual-studio-code-bin/

--------------------------------------------------------------------------------

## External

### install git tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/git-cola/

### install doxygen tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/custom-doxygen/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/vim-doxygen/

--------------------------------------------------------------------------------

## Configurations

### configure compiledb

**NOTE:** Only use if Bear or PlatformIO is not available

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv compiledb --system-site-packages

source $HOME/PyEnv/compiledb/bin/activate
pip install compiledb
deactivate
```

```sh
source $HOME/PyEnv/compiledb/bin/activate
compiledb -n make
deactivate

bat compile_commands.json
```

### configure git server

#### instant git web

```sh
ls ./.git
git instaweb -l -p 5757
```

### configure vim

#### alternative vim plug

```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "call plug#begin('~/.vim/pack/plug/start')
call plug#end()" | tee ~/.vimrc
mkdir -p ~/.vim/pack/plug/start/

vim +PlugStatus
```

#### vim plugins settings

```sh
echo -e "call plug#begin('~/.vim/pack/plug/start')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'honza/vim-snippets'
Plug 'chrisbra/csv.vim'
Plug 'SirVer/ultisnips'
Plug 'junegunn/fzf.vim'
Plug 'preservim/vim-markdown'
call plug#end()

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \\: \"\\<C-g>u\\<CR>\\<c-r>=coc#on_enter()\\<CR>\"

\":h cterm-colors
\":h gui-colors
\":hi
hi CocFloating ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow
hi CocInlayHint ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow

nnoremap <silent> <C-f> :Files<CR>
nnoremap <silent> <C-g> :Rg<CR>

let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_toc_autofit = 1
let g:vim_markdown_autowrite = 1
" | tee ~/.vimrc
```

#### vim plugin install

```sh
node -v;ls ~/.vimrc
mkdir -p ~/.vim/pack/plug/start/

vim +PlugInstall
vim -c "CocInstall coc-pairs coc-snippets coc-ultisnips"
vim -c "CocInstall coc-clangd coc-jedi coc-json coc-tsserver"
vim -c "CocInstall coc-sh coc-html coc-yaml coc-rust-analyzer"
vim +PlugClean
```

```sh
mkdir -p ~/.vim

jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"] |
."rust-analyzer.server.path"="/usr/bin/rust-analyzer"
' > ~/.vim/coc-settings.json

bat ~/.vim/coc-settings.json
```

### configure clangd

```sh
bear -- gcc -o coba.exe coba.c
bear -- make -j$(nproc)
```

```sh
# Initial clangd config without header cleaning

mkdir -p ~/.config/clangd/
echo "
Diagnostics:
  UnusedIncludes: None
" | tee ~/.config/clangd/config.yaml

sed -i 's@UnusedIncludes: Strict@UnusedIncludes: None@g' ~/.config/clangd/config.yaml
```

### configure vscode

#### settings

```sh
VSCONFDIR=~/.config/Code/User
mkdir -p "$VSCONFDIR"
echo "{}" > "$VSCONFDIR/settings.json"

jq '
."C_Cpp.intelliSenseEngine"="default" |
."C_Cpp.autocompleteAddParentheses"=true |
."C_Cpp.default.compileCommands"="compile_commands.json" |
."clangd.arguments"=["-header-insertion=never"] |
."doxdocgen.file.customTag"=["@addtogroup ","@{"] |
."doxdocgen.file.fileOrder"=["file","brief","empty","custom"] |
."editor.fontFamily"="'\''Liberation Mono'\''" |
."editor.fontSize"=10 |
."editor.minimap.enabled"=false |
."extensions.ignoreRecommendations"=true |
."files.trimTrailingWhitespace"=true |
."files.enableTrash"=false |
."git.openRepositoryInParentFolders"="never" |
."git.enableSmartCommit"=true |
."security.workspace.trust.untrustedFiles"="open" |
."terminal.integrated.fontSize"=10 |
."terminal.integrated.gpuAcceleration"="canvas" |
."debug.console.wordWrap"=false |
."workbench.startupEditor"="none" |
."workbench.activityBar.visible"=false |
."workbench.colorTheme"="Default Light+" |
."window.restoreWindows"="none" |
."window.commandCenter"=false |
."window.titleBarStyle"="native" |
."telemetry.telemetryLevel"="off" |
."telemetry.enableTelemetry"=false |
."telemetry.enableCrashReporter"=false |
."update.mode"="none"
' "$VSCONFDIR/settings.json" | tee "$VSCONFDIR/temp.json"

rm -f "$VSCONFDIR/settings.json"
mv "$VSCONFDIR/temp.json" "$VSCONFDIR/settings.json"
```

#### extensions

```sh
code --list-extensions

code --force --install-extension ms-python.python
code --force --install-extension ms-python.vscode-pylance
code --force --install-extension ms-vscode.cpptools
code --force --install-extension cschlosser.doxdocgen
code --force --install-extension rust-lang.rust-analyzer
code --force --install-extension mads-hartmann.bash-ide-vscode

code --force --install-extension oderwat.indent-rainbow
code --force --install-extension pkief.material-icon-theme
code --force --install-extension tejasvi.rainbow-brackets-2
code --force --install-extension wayou.vscode-todo-highlight
```

```sh
# not really recommended as it may difficult to use

code --force --install-extension vscodevim.vim
code --force --install-extension ms-pyright.pyright
```

```sh
# Using Clangd instead Microsoft C/C++

code --force --uninstall-extension ms-vscode.cpptools
code --force --install-extension llvm-vs-code-extensions.vscode-clangd

sed -i 's#Engine": "default"#Engine": "disabled"#g' \
~/.config/VSCodium/User/settings.json
```

### configure rustup

#### setup

```sh
curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs -o ~/rust.sh

bash ~/rust.sh -y --no-modify-path

sed -i '/cargo/d' ~/.bashrc
sed -i '/cargo/d' ~/.profile
sed -i '/cargo/d' ~/.bash_profile
```

```sh
source ~/.cargo/env

cargo -V
```

```sh
source ~/.cargo/env

rustup component add rust-src
rustup component add rust-analyzer
```

#### changing default channel

```sh
rustup override set [nightly|stable]

rustup default [nightly|stable]
```

#### vim-coc default analyzer

```sh
jq '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"] |
."rust-analyzer.server.path"=""
' ~/.vim/coc-settings.json > ~/.vim/temp.json

mv ~/.vim/temp.json ~/.vim/coc-settings.json

bat ~/.vim/coc-settings.json
```
