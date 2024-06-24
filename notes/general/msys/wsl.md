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

### set default distro

```sh
# check installed distro
wsl --list --verbose

# set to LTS distro
wsl --set-default ubuntu-20.04
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

drive C: -> **/mnt/c**
Windows User -> **/mnt/c/Users/Administrator/**

```sh
wsl -- ls /mnt/c/
wsl -- ls /mnt/c/Users/Administrator/
```

### termination

```sh
# terminate specific distro
wsl --terminate ubuntu-20.04

# shutdown WSL kernel
wsl --shutdown
```

## Ubuntu-20.04 WSL 

**Notes:** Avoid install GUI/X11 packages as WSL run like a container

### start-up

```sh
wsl -d ubuntu-20.04
```

### update databases

```sh
sudo apt-get update
```

### basic packages

```sh
sudo apt-get install git tig mc bat neofetch vim nano zip p7zip bash-completion
```

### basic profiles

```sh
sudo su

echo '
export PATH=$PATH:~/.local/bin
export VISUAL=vim
export EDITOR=vim
export PAGER=less
export VIEWER=less
' | tee /etc/profile.d/wsl_profile.sh

exit
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
alias wsl='cmd.exe /c start cmd.exe /c wsl.exe'
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
