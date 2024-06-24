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

```sh
wsl -- ls /mnt/c/
```

### termination

```sh
# terminate specific distro
wsl --terminate ubuntu-20.04

# shutdown WSL kernel
wsl --shutdown
```

## Ubuntu-20.04 WSL 

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
echo '
export PATH=$PATH:~/.local/bin
export VISUAL=vim
export EDITOR=vim
export PAGER=less
export VIEWER=less
' | sudo tee /etc/profile.d/wsl_profile.sh

echo '[[ $- != *i* ]] && return' |  tee ~/.bashrc
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
PS1='\[\033[01m\][\u@\h \W]\$ \[\033[00m\]'
" | tee -a ~/.bashrc
```
