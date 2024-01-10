# Programming Packages

## Official

### install gitea server

gitea postgresql
memcached redis

### install qt programming

qt5 qt6 qtcreator
x11-ssh-askpass

### install qt python

pyqt-builder
sip python-qtpy
python-pyqt5
pyside2 pyside2-tools
python-pyqt5-3d python-pyqt5-webengine
python-pyqt5-chart python-pyqt5-datavisualization
python-pyqt6
pyside6 pyside6-tools
python-pyqt6-3d python-pyqt6-webengine
python-pyqt6-charts python-pyqt6-datavisualization

### install qt graph additionals

qcustomplot qwt
python-pyqtgraph

### install c/c++ programming

gdb gdb-dashboard
lldb lld valgrind
llvm clang boost

### install javacript programming

nodejs node-gyp yq
npm yarn asar jq

--------------------------------------------------------------------------------

## AUR

### install qwt additionals

```sh
sed -i 's#-p1#-p0#g' PKGBUILD
```

- https://aur.archlinux.org/packages/qwt-qt6-svn/
- https://aur.archlinux.org/packages/python-pyqt-qwt/

### install programmming editor

- https://aur.archlinux.org/packages/eric/
- https://aur.archlinux.org/packages/wxhexeditor/
- https://aur.archlinux.org/packages/wxformbuilder/

### install compiledb

- https://aur.archlinux.org/packages/python-bashlex/
- https://aur.archlinux.org/packages/compiledb/

### install system python bindings

- https://aur.archlinux.org/packages/python-wifiwrapper/
- https://aur.archlinux.org/packages/python-pyalsaaudio/

### install shell additional

- https://aur.archlinux.org/packages/ttyplot-git/
- https://aur.archlinux.org/packages/ncurses5-compat-libs/

--------------------------------------------------------------------------------

## External

### install git tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/git-cola/

### install doxygen tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/custom-doxygen/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/vim-doxygen/

--------------------------------------------------------------------------------

## Configurations

### configure git server

#### instant git web

```sh
ls ./.git
git instaweb -l -p 5757
```

### configure qtcreator

```sh
echo "Help->About Plugins->C++"
echo "check: ClangCodeModel"

echo "Edit->Preferences->Text Editor->Font & Colors"
echo "Family: LiterationMono Nerd Font"
echo "Size: 8"

echo "Edit->Preferences->C++->Code Model"
echo "check: Interpret ambiguous headers as C headers"
echo "check: Ignore precompiled headers"

echo "Edit->Preferences->C++->Clangd"
echo "uncheck: Use clangd"

echo "Edit->Preferences->Analyzer"
echo "uncheck: Analyze open files"

echo "Edit->Preferences->FakeVim"
echo "uncheck: Use FakeVim"
```

### configure vim

#### alternative vim plug

```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "call plug#begin('~/.vim/pack/plug/start')
call plug#end()" | tee ~/.vimrc

vim +PlugStatus
```

#### vim plugins

```sh
echo -e "call plug#begin('~/.vim/pack/plug/start')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'honza/vim-snippets'
Plug 'chrisbra/csv.vim'
Plug 'SirVer/ultisnips'
call plug#end()

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \\: \"\\<C-g>u\\<CR>\\<c-r>=coc#on_enter()\\<CR>\"

hi CocFloating ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow
hi CocInlayHint ctermfg=Black ctermbg=Yellow guifg=Black guibg=Yellow
" | tee ~/.vimrc
```

```sh
node -v
cat ~/.vimrc
mkdir -p ~/.vim/pack/plug/start/

vim +PlugInstall
vim -c "CocInstall coc-pairs coc-snippets"
vim -c "CocInstall coc-json coc-tsserver"
vim -c "CocInstall coc-sh coc-ultisnips"
vim -c "CocInstall coc-clangd coc-jedi"
vim -c "CocInstall coc-html coc-yaml"
vim +PlugClean

echo "For editing PKGBUILD"
echo ":set ft=PKGBUILD"
```

```sh
mkdir -p ~/.vim
echo '{}' > ~/.vim/coc-settings.json
jq -n '
."clangd.arguments"=["-header-insertion=never"] |
."pairs.enableCharacters"=["(","[","\"","'\''","`"]
' ~/.vim/coc-settings.json > ~/.vim/coc-settings.json
cat ~/.vim/coc-settings.json
```

```sh
echo "vim color setting commands
echo ":h cterm-colors"
echo ":h gui-colors"
echo ":hi"
```

### configure clangd

```sh
bear -- gcc -o coba.exe coba.c
bear -- make -j$(nproc)
```

```sh
compiledb gcc -o coba.exe coba.c
compiledb make -j$(nproc)
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
