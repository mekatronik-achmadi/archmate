# Windows Subsystem for Linux

## Setup WSL

**Note:** Run setup everything inside Windows' CMD as Administrator

### check status

```sh
wsl --status
```

### list available distro

```sh
wsl --list --online
```

### install LTS distro

**Note:** It may requires Windows restart to start WSL kernel.

**Note:** Re-run this command if distro installation hangs.

```sh
wsl --install -d ubuntu-20.04
```

Installed distro folder:

```
C:\Users\<username>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows*
```

### set default distro

```sh
# check installed distro
wsl --list --verbose

# set to LTS distro
wsl --set-default ubuntu-20.04
```

### termination

```sh
# terminate specific distro
wsl --terminate ubuntu-20.04

# shutdown WSL kernel
wsl --shutdown
```

### disable sudo password

```sh
wsl -d ubuntu-20.04

sudo su
```

**Notes:** This example use **wsl** as username example

```sh
echo 'wsl ALL:(ALL) NOPASSWD:ALL' | tee -a /etc/sudoers
```

```sh
exit

wsl --terminate -d ubuntu-20.04
```

### removing distro

```sh
wsl --unregister ubuntu-20.04
```

### disable/enable wsl autostart

enable:

```sh
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

disable:

```sh
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart
```

## WSL Usage

**Note:** This doesn't have to be run as Administrator

### run from CMD

```sh
# run without argument
wsl

# run on specific distro
wsl -d ubuntu-20.04

# run a Linux command
wsl -- neofetch
wsl -d ubuntu-20.04 -- neofetch
```

### drive path

Paths:
- drive C: -> **/mnt/c**
- Windows User -> **/mnt/c/Users/<username>/**

```sh
wsl -- ls /mnt/c/
wsl -- ls /mnt/c/Users/Administrator/
```

## Ubuntu-20.04 WSL

**Notes:** Avoid install GUI/X11 packages as WSL run like a container

### start-up

```sh
wsl -d ubuntu-20.04
```

### update\upgrade

```sh
sudo apt-get update
sudo apt-get upgrade
```

### basic packages

```sh
sudo apt-get install $(echo "
git tig mc bat neofetch vim nano p7zip
zip cython python3-pip python3-virtualenv
unrar bash-completion cmake build-essential
")
```

### basic profiles

```sh
echo '
export PATH=$PATH:~/.local/bin
export VISUAL=vim
export EDITOR=vim
export PAGER=less
export VIEWER=less
' | sudo tee /etc/profile.d/wsl_profile.sh
```

```sh
echo "
shopt -s checkwinsize
shopt -s histappend
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias makepkg='makepkg --nocheck --skippgpcheck'
alias mc='mc --nocolor'
alias bat='bat --theme=ansi'
export MAKEFLAGS=-j$(nproc)
export HISTCONTROL=ignorespace:ignoredups:erasedupsT
" | tee -a ~/.bashrc
```

### git profile

```sh
echo '[core]
	pager = cat
	editor = vim
	whitespace = -trailing-space

[diff]
	renames = true
	tool = vimdiff

[color]
	ui = auto

[credential]
	helper = cache --timeout=3600

[advice]
	addIgnoredFile = false

[init]
	defaultBranch = main

[user]
	name =
	email =
' > ~/.gitconfig

git config --global user.name "mekatronik-achmadi"
git config --global user.email "mekatronik.achmadi@gmail.com"
```

### vim profile

**Notes:** CoC currently doesn't work for Vim inside WSL

```sh
mkdir -p ~/.vim/autoload/
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

```sh
echo "
call plug#begin('~/.vim/pack/plug/start')
    Plug 'm-pilia/vim-pkgbuild'
    Plug 'dense-analysis/ale'
    Plug 'preservim/nerdcommenter'
    Plug 'preservim/nerdtree'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'airblade/vim-gitgutter'
    Plug 'godlygeek/tabular'
    Plug 'preservim/tagbar'
    Plug 'preservim/vim-markdown'
    Plug 'chrisbra/csv.vim'
    Plug 'lervag/vimtex'
call plug#end()

let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_toc_autofit = 1
let g:vim_markdown_autowrite = 1

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

vim +PlugInstall
```

