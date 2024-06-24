# MSYS2 Basic

## Non-MSYS2 Download

- 7Zip: https://www.7-zip.org/download.html
- LiberationFontsTTF: https://github.com/liberationfonts/liberation-fonts/releases/tag/2.1.5
- Firefox Browser: https://www.mozilla.org/id/firefox/all/#product-desktop-release
- Latest MSVC++: https://learn.microsoft.com/id-id/cpp/windows/latest-supported-vc-redist
- CopyQ: https://github.com/hluk/CopyQ/releases
- WinMerge: https://winmerge.org/downloads/?lang=en
- Notepad++: https://notepad-plus-plus.org/downloads/
- Git: https://git-scm.com/download/win
- Git-Cola: https://git-cola.github.io/downloads.html
- VSCode: https://code.visualstudio.com/download
- Geany:
	- https://download.geany.org/geany-2.0_setup.exe
	- https://plugins.geany.org/geany-plugins/geany-plugins-2.0_setup.exe

## Setup

### system install

Download: https://github.com/msys2/msys2-installer/releases

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
base base-devel mintty winpty
vim nano openssh unrar zip p7zip
git tig mc neofetch bash-completion
")
```

### devel packages

```sh
pacman -S $(echo "
mingw-w64-x86_64-bat
mingw-w64-x86_64-rust
mingw-w64-x86_64-ctags
mingw-w64-x86_64-python
mingw-w64-x86_64-cython0
mingw-w64-x86_64-python-pip
mingw-w64-x86_64-cmake
mingw-w64-x86_64-toolchain
mingw-w64-x86_64-clang-analyzer
mingw-w64-x86_64-clang-tools-extra
mingw-w64-x86_64-python-virtualenv
")
```

### gtk3 packages

```sh
pacman -S $(echo "
mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python-gobject
mingw-w64-x86_64-glade mingw-w64-x86_64-gtkmm3
")
```

### nodejs packages

```sh
pacman -S $(echo "
mingw-w64-x86_64-jq
mingw-w64-x86_64-yarn
mingw-w64-x86_64-nodejs
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
alias mc='mc --nocolor'
alias bat='bat --theme=ansi'
export MAKEFLAGS=-j$(nproc)
export HISTCONTROL=ignorespace:ignoredups:erasedupsT
PS1='\[\033[01m\][\u@\h \W]\$ \[\033[00m\]'
" | tee -a ~/.bashrc
```

### git profile

```sh
echo '[core]
	pager = cat
	editor = vim
	whitespace = -trailing-space

[gui]
	editor = geany
	spellingdictionary = none
	fontui = -family \"Liberation Sans\" -size 8 -weight normal -slant roman -underline 0 -overstrike 0
	fontdiff = -family \"LiterationMono Nerd Font\" -size 8 -weight normal -slant roman -underline 0 -overstrike 0

[guitool "Pull"]
	cmd = git pull

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

echo 'export GITHUBTOKEN=$(cat ~/GithubToken.txt)' | tee -a ~/.bashrc
```
