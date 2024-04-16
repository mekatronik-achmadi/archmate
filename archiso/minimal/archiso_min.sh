#!/bin/bash

if [ $UID != 0 ];then
	echo -e "This script must run as root"
	exit
fi

######################### Archiso Prepare #########################

echo $REPOURL
export ISOVER='mate_012024'
export ISONAME='minimal_012024'
export DIRPATH="/home/development/Packages/ArchMate-x86_64/$ISOVER"
export DBPATH="$DIRPATH/databases"
export PKGPATH="$DIRPATH/packages/official"
export CSTPATH="$DIRPATH/packages/custom"
export PKGLIST='../pkg-minimal-x86_64.txt'
export PKGCUSTOM='false'

mkdir -pv archlive/
cp -rvf /usr/share/archiso/configs/releng/* archlive/
cd archlive/

cp -vf $PKGLIST ./packages.x86_64
sed -i 's/ /\n/g' ./packages.x86_64

mkdir -pv work/x86_64/airootfs/

sed -i 's#iso_label="ARCH_$(date +%Y%m)"#iso_label="ARCH_LINUX"#g' profiledef.sh
sed -i 's#iso_version="$(date +%Y.%m.%d)"#iso_version="$ISONAME"#g' profiledef.sh
sed -i "s#'-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M'#'-limit' '75' '-comp' 'zstd' '-b' '1M'#g" profiledef.sh

######################### Archiso Configs #########################

sed -i "s#APPEND -pxe- pxe -sys- sys -iso- sys#\
APPEND -sys- sys -iso- sys#g" syslinux/syslinux.cfg

delNum=$(grep -n "LABEL pxe" syslinux/syslinux.cfg | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" syslinux/syslinux.cfg
sed -i "${delNum}d" syslinux/syslinux.cfg
sed -i "${delNum}d" syslinux/syslinux.cfg

######################### Pacman Configs ##########################

export URLREPO="$REPOURL/\$repo/os/\$arch"
echo "[options]
HoldPkg           = pacman glibc
Architecture      = x86_64
SigLevel          = Never
LocalFileSigLevel = Never
ParallelDownloads = 5

[core]
Server = $URLREPO

[extra]
Server = $URLREPO

[multilib]
Server = $URLREPO
" | tee pacman.conf

if [ "$PKGCUSTOM" = "true" ];then
    echo "[custom]" | tee -a pacman.conf
    echo "Server = file:///home/custompkgs" | tee -a pacman.conf
fi

export URLREPO="$REPOURL/\$repo/os/\$arch"
sed -i "s#Include = /etc/pacman.d/mirrorlist#Server = $URLREPO#g" pacman.conf

######################### Basic Configs ##########################

mkdir -pv airootfs/etc/
echo '
                    -@
                   .##@
                  .####@
                  @#####@
                . *######@
               .##@o@#####@
              /############@
             /##############@
            @######@**%######@
           @######`     %#####o
          @######@       ######%
        -@#######h       ######@.`
       /#####h**``       `**%@####@
      @H@*`                    `*%#@
     *`                            `*
' | tee airootfs/etc/motd

sed -i "s#archiso_pxe_common archiso_pxe_nbd archiso_pxe_http archiso_pxe_nfs#consolefont#g" airootfs/etc/mkinitcpio.conf
sed -i "s#memdisk archiso_shutdown archiso#memdisk archiso#g" airootfs/etc/mkinitcpio.conf
sed -i "s#archiso_kms#kms#g" airootfs/etc/mkinitcpio.conf
sed -i "s#xz#zstd#g" airootfs/etc/mkinitcpio.conf

echo "archlive" | tee airootfs/etc/hostname

echo "LANG=en_US.UTF-8" | tee airootfs/etc/locale.conf
echo "en_US ISO-8859-1" | tee airootfs/etc/locale.gen
echo "en_US.UTF-8 UTF-8" | tee -a airootfs/etc/locale.gen

echo "FONT=ter-112n
FONT_MAP=8859-2
" | tee airootfs/etc/vconsole.conf

echo "root ALL=(ALL) ALL
%wheel ALL=(ALL) NOPASSWD: ALL

@includedir /etc/sudoers.d
" | tee airootfs/etc/sudoers

mkdir -pv airootfs/etc/ssh
echo "
PermitRootLogin yes
AuthorizedKeysFile .ssh/authorized_keys
PermitEmptyPasswords yes
ChallengeResponseAuthentication no
UsePAM yes
PrintMotd no
Subsystem sftp /usr/lib/ssh/sftp-server
X11Forwarding yes
X11UseLocalhost yes
X11DisplayOffset 10
AllowTcpForwarding yes
" | tee airootfs/etc/ssh/sshd_config


######################### Systemd Configs ##########################

export SYSTEMD='airootfs/etc/systemd/system/multi-user.target.wants'
mkdir -pv ${SYSTEMD}

ln -svf /usr/lib/systemd/system/systemd-timesyncd.service ${SYSTEMD}/systemd-timesyncd.service
ln -svf /usr/lib/systemd/system/vboxservice.service ${SYSTEMD}/vboxservice.service
ln -svf /usr/lib/systemd/system/sshd.service ${SYSTEMD}/sshd.service

rm -vf airootfs/etc/systemd/system/dbus-org.freedesktop.network1.service
rm -vf airootfs/etc/systemd/system/multi-user.target.wants/systemd-networkd.service
rm -vf airootfs/etc/systemd/system/sockets.target.wants/systemd-networkd.socket
rm -vf airootfs/etc/systemd/system/network-online.target.wants/systemd-networkd-wait-online.service
rm -vf airootfs/etc/systemd/system/systemd-networkd-wait-online.service.d/*

rm -vf airootfs/etc/systemd/system/dbus-org.freedesktop.resolve1.service
rm -vf airootfs/etc/systemd/system/sysinit.target.wants/systemd-resolved.service
rm -vf airootfs/etc/systemd/system/multi-user.target.wants/systemd-resolved.service

mkdir -pv airootfs/etc/systemd/system/getty@tty1.service.d/
echo "[Service]
TTYVTDisallocate=no
" | tee airootfs/etc/systemd/system/getty@tty1.service.d/noclear.conf

echo "[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin live --noclear %I 38400 linux
" | tee airootfs/etc/systemd/system/getty@tty1.service.d/autologin.conf

rm -vf airootfs/etc/systemd/logind.conf.d/do-not-suspend.conf
echo '[login]
HandleLidSwitch=suspend
HandleLidSwitchDocked=suspend
' | tee airootfs/etc/systemd/logind.conf.d/lid-suspend.conf

######################### User Configs ############################

echo 'root:x:0:0:root:/root:/bin/bash
live:x:1000:984:live:/home/live:/bin/bash
' | tee airootfs/etc/passwd

echo 'root:x:0:root
tty:x:5:live
video:x:985:live
power:x:98:live
wheel:x:998:live
storage:x:987:live
autologin:x:969:
wireshark:x:150:live
' | tee airootfs/etc/group

echo 'root::14871::::::
live::18740:0:99999:7:::
' | tee airootfs/etc/shadow

echo 'root:::root
tty:!*::live
video:!*::live
power:!*::live
wheel:!*::live
storage:!*::live
autologin:!*::
wireshark:!*::live
' | tee airoot/etc/gshadow

######################### CLI Configs ############################

mkdir -pv airootfs/etc/skel/
echo '
[[ -f ~/.bashrc ]] && . ~/.bashrc
source ~/.bashrc

if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    echo "SSH Login Success"
else
    if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
        true
    fi
fi' | tee airootfs/etc/skel/.bash_profile

echo '[[ $- != *i* ]] && return' | tee airootfs/etc/skel/.bashrc
echo "
shopt -s checkwinsize
shopt -s histappend
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias sudo='sudo -E'
alias makepkg='makepkg --nocheck --skippgpcheck'
alias htop='htop -C'
alias bat='bat --theme=ansi'
alias mc='mc --nocolor'
export MAKEFLAGS=-j$(nproc)
export HISTCONTROL=ignorespace:ignoredups:erasedups
export REPOURL='http://mirror.internode.on.net/pub/archlinux'
PS1='\[\033[01m\][\u@\h \W]\$ \[\033[00m\]'
" | tee -a airootfs/etc/skel/.bashrc

mkdir -pv airootfs/etc/profile.d/
echo 'export PATH=$PATH:~/.local/bin
export VISUAL=nano
export EDITOR=nano
export PAGER=less
export VIEWER=less
' | tee airootfs/etc/profile.d/arch-profile.sh

######################### GUI Configs ############################

######################### Archiso Packages #########################

mkdir -pv work/x86_64/airootfs/etc/
cp -vf pacman.conf work/x86_64/airootfs/etc/pacman.conf

mkdir -pv work/x86_64/airootfs/var/lib/pacman/sync/
rsync -avh $DBPATH/ work/x86_64/airootfs/var/lib/pacman/sync/

mkdir -pv work/x86_64/airootfs/var/cache/pacman/pkg/
rsync -avh $PKGPATH/ work/x86_64/airootfs/var/cache/pacman/pkg/

if [ "$PKGCUSTOM" = "true" ];then
    rsync -avh $CSTPATH/ work/x86_64/airootfs/var/cache/pacman/pkg/
fi

######################### Archiso Building #########################

mkarchiso -v ./

chown -v 1000:users out/*.iso
mv -v out/*.iso ../

echo "Arch Linux Live ISO completed"

