#!/bin/bash

if [ $UID != 0 ];then
	echo -e "This script must run as root"
	exit
fi

#pacman-key --init
#pacman-key --populate archlinux

######################### Archiso Prepare #########################

export DBPATH='/home/developments/Packages/ArchMate-x86_64/databases'
export PKGPATH='/home/developments/Packages/ArchMate-x86_64/packages/official'
export CSTPATH='/home/developments/Packages/ArchMate-x86_64/packages/custom'
export REPOURL='http://mirror.labkom.id/archlinux'
export PKGLIST='../pkg-cli-x86_64.txt'
export PKGCUSTOM='true'

mkdir -p archlive/
cp -rv /usr/share/archiso/configs/releng/* archlive/
cd archlive/

cp -v $PKGLIST ./packages.x86_64
sed -i 's/ /\n/g' ./packages.x86_64

mkdir -p work/x86_64/airootfs/

sed -i 's#iso_label="ARCH_$(date +%Y%m)"#iso_label="ARCH_LINUX"#g' profiledef.sh
sed -i 's#iso_version="$(date +%Y.%m.%d)"#iso_version="cli"#g' profiledef.sh

######################### Archiso Configs #########################

sed -i "s#APPEND -pxe- pxe -sys- sys -iso- sys#\
APPEND -sys- sys -iso- sys#g" syslinux/syslinux.cfg

delNum=$(grep -n "LABEL pxe" syslinux/syslinux.cfg | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" syslinux/syslinux.cfg
sed -i "${delNum}d" syslinux/syslinux.cfg
sed -i "${delNum}d" syslinux/syslinux.cfg

sed -i "s#Architecture = auto#Architecture = x86_64#g" pacman.conf

sed -i "s#= Required DatabaseOptional#= Never#g" pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" pacman.conf
sed -i "s#= Optional#= Never#g" pacman.conf

delNum=$(grep -n '\[testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[community-testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[multilib-testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[custom\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

sed -i "s@\#\[multilib\]@\[multilib\]@g" pacman.conf
sed -i "s@\#Include@Include@g" pacman.conf

if [ "$PKGCUSTOM" = "true" ];then
    echo "[custom]" >> pacman.conf
    echo "Server = file:///home/custompkgs" >> pacman.conf
fi

export URLREPO="$REPOURL/\$repo/os/\$arch"
sed -i "s#Include = /etc/pacman.d/mirrorlist#Server = $URLREPO#g" pacman.conf

sed -i "s#archiso_pxe_common archiso_pxe_nbd archiso_pxe_http archiso_pxe_nfs#consolefont#g" airootfs/etc/mkinitcpio.conf

echo "archlive" > airootfs/etc/hostname

echo "LANG=en_US.UTF-8" > airootfs/etc/locale.conf
echo "en_US ISO-8859-1" >> airootfs/etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> airootfs/etc/locale.gen

echo "FONT=ter-112n
FONT_MAP=8859-2
" > airootfs/etc/vconsole.conf

echo "root ALL=(ALL) ALL
%wheel ALL=(ALL) NOPASSWD: ALL

@includedir /etc/sudoers.d
" > airootfs/etc/sudoers

mkdir -p airootfs/etc/skel
echo "[[ -f ~/.bashrc ]] && . ~/.bashrc
source ~/.bashrc" > airootfs/etc/skel/.bash_profile

mkdir -p airootfs/etc/ssh
echo "
PermitRootLogin yes
AuthorizedKeysFile .ssh/authorized_keys
PermitEmptyPasswords yes
ChallengeResponseAuthentication no
UsePAM yes
PrintMotd no
Subsystem sftp /usr/lib/ssh/sftp-server
" > airootfs/etc/ssh/sshd_config

export SYSTEMD='airootfs/etc/systemd/system/multi-user.target.wants'
mkdir -p ${SYSTEMD}

ln -sf /usr/lib/systemd/system/systemd-timesyncd.service ${SYSTEMD}/systemd-timesyncd.service
ln -sf /usr/lib/systemd/system/systemd-networkd.service ${SYSTEMD}/systemd-networkd.service
ln -sf /usr/lib/systemd/system/systemd-resolved.service ${SYSTEMD}/systemd-resolved.service
ln -sf /usr/lib/systemd/system/fake-hwclock.service ${SYSTEMD}/fake-hwclock.service
ln -sf /usr/lib/systemd/system/vboxservice.service ${SYSTEMD}/vboxservice.service
ln -sf /usr/lib/systemd/system/sensord.service ${SYSTEMD}/sensord.service
ln -sf /usr/lib/systemd/system/sshd.service ${SYSTEMD}/sshd.service

echo 'root:x:0:0:root:/root:/bin/bash
live:x:1000:984:live:/home/live:/bin/bash
' > airootfs/etc/passwd

echo 'root:x:0:root
power:x:98:live
wheel:x:998:live
storage:x:987:live
autologin:x:969:live
' > airootfs/etc/group

echo 'root::14871::::::
live::18740:0:99999:7:::
' > airootfs/etc/shadow

echo 'root:::root
power:!*::live
wheel:!*::live
storage:!*::live
autologin:!::live
' > airoot/etc/gshadow

######################### Archiso CLI #########################

mkdir -p airootfs/etc/systemd/system/getty@tty1.service.d/

echo "[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin live --noclear %I 38400 linux
" > airootfs/etc/systemd/system/getty@tty1.service.d/autologin.conf

######################### Archiso Packages #########################

mkdir -p work/x86_64/airootfs/etc/
cp -v pacman.conf work/x86_64/airootfs/etc/pacman.conf

mkdir -p work/x86_64/airootfs/var/lib/pacman/sync/
rsync -avh $DBPATH/ work/x86_64/airootfs/var/lib/pacman/sync/

mkdir -p work/x86_64/airootfs/var/cache/pacman/pkg/
rsync -avh $PKGPATH/ work/x86_64/airootfs/var/cache/pacman/pkg/

if [ "$PKGCUSTOM" = "true" ];then
    rsync -avh $CSTPATH/ work/x86_64/airootfs/var/cache/pacman/pkg/
fi

######################### Archiso Building #########################

mkarchiso -v ./

chown -v 1000:users out/*.iso
mv -v out/*.iso ../

echo "Arch Linux Live ISO completed"

