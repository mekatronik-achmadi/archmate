### Disk Install

##### prepare disk

~~~
sudo fdisk -l

export DEVDISK='/dev/sdb'

sudo parted ${DEVDISK} mklabel msdos

yes | sudo parted ${DEVDISK} mkpart primary 0% 200
yes | sudo parted ${DEVDISK} mkpart primary 200 100%
yes | sudo parted ${DEVDISK} set 1 lba on
yes | sudo parted ${DEVDISK} set 1 boot on

yes | sudo mkfs.vfat ${DEVDISK}1
yes | sudo mkfs.ext4 ${DEVDISK}2

mkdir -p /mnt/{boot,root}
sudo mount ${DEVDISK}1 /mnt/boot
sudo mount ${DEVDISK}2 /mnt/root
~~~

##### download image

~~~
wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz
~~~

##### deploy image

~~~
sudo bsdtar -xpf ArchLinuxARM-rpi-2-latest.tar.gz -C /mnt/root
sudo sync

sudo mv -vf /mnt/root/boot/* /mnt/boot/
sudo sync

sudo umount /mnt/root /mnt/boot
~~~

--------------------------------------------------------------------------------

### Qemu run

##### mount disk

~~~
sudo fdisk -l

export DEVDISK='/dev/sdb'
sudo mount ${DEVDISK}2 /mnt/root
sudo mount ${DEVDISK}1 /mnt/root/boot
~~~

##### copy qemu-arm-static

~~~
sudo cp -vf /usr/bin/qemu-arm-static /mnt/root/usr/bin/
~~~

##### arch-chrooting

~~~
sudo arch-chroot /mnt/root /bin/bash

uname -a

exit
~~~

--------------------------------------------------------------------------------

### Install packages

##### initialize pacman (qemu-chroot)

~~~
pacman-key --init
pacman-key --populate archlinuxarm
~~~

##### prepare database

~~~
mkdir -p databases/;cd databases/
echo "
http://mirror.archlinuxarm.org/armv7h/core/core.db
http://mirror.archlinuxarm.org/armv7h/core/core.files
http://mirror.archlinuxarm.org/armv7h/extra/extra.db
http://mirror.archlinuxarm.org/armv7h/extra/extra.files
http://mirror.archlinuxarm.org/armv7h/community/community.db
http://mirror.archlinuxarm.org/armv7h/community/community.files
http://mirror.archlinuxarm.org/armv7h/alarm/alarm.db
http://mirror.archlinuxarm.org/armv7h/alarm/alarm.files
http://mirror.archlinuxarm.org/armv7h/aur/aur.db
http://mirror.archlinuxarm.org/armv7h/aur/aur.files
" > ../dbase.txt
wget -i ../dbase.txt
cd ../
~~~

~~~
sudo rsync -avh databases/ /mnt/root/var/lib/pacman/sync/
~~~

##### generate upgrade packages urls (qemu-chroot)

~~~
pacman -Sup > /home/alarm/upgrade_pkgs.txt
~~~

##### prepare upgrade packages

~~~
cp -vf /mnt/root/home/alarm/upgrade_pkgs.txt ./
mkdir -p packages/official/;cd packages/official/
wget -i ../../upgrade_pkgs.txt
cd ../../
~~~

~~~
sudo rsync -avh packages/official/ /mnt/root/var/cache/pacman/pkg/
~~~

##### upgrade packages (qemu-chroot)

~~~
pacman -Su --noconfirm
~~~

##### copy install packages list

~~~
cp -vf pkg_*.txt /mnt/root/home/alarm/pkglist.txt
~~~

##### generate install packages urls (qemu-chroot)

~~~
pacman -Sp $(cat /home/alarm/pkglist.txt) > /home/alarm/install_pkgs.txt
~~~

##### prepare install packages

~~~
cp -vf /mnt/root/home/alarm/install_pkgs.txt ./
mkdir -p packages/official/;cd packages/official/
wget -i ../../install_pkgs.txt
cd ../../
~~~

~~~
sudo rsync -avh packages/official/ /mnt/root/var/cache/pacman/pkg/
~~~

##### install packages (qemu-chroot)

~~~
pacman -S --noconfirm $(cat /home/alarm/pkglist.txt)
~~~

--------------------------------------------------------------------------------

### Global Configuration

##### set hostname (qemu-chroot)

~~~
echo "alarmrpi" > /etc/hostname
~~~

##### disable audit messages (qemu-chroot)

~~~
sed -i '$s/$/ audit=0/' /boot/cmdline.txt
~~~

##### generate locale (qemu-chroot)

~~~
echo "LANG=en_US.UTF-8" > /etc/locale.conf
echo "en_US ISO-8859-1" >> /etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
~~~

##### sudoers no password (qemu-chroot)

~~~
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
~~~

##### disable passwords (qemu-chroot)

~~~
passwd -d root
passwd -d alarm
~~~

##### console font (qemu-chroot)

~~~
echo "FONT=ter-112n
FONT_MAP=8859-2
" > /etc/vconsole.conf
~~~

##### enable ssh server (qemu-chroot)

~~~
systemctl enable sshd.service
~~~

### CLI Configuration

##### cli autologin (qemu-chroot)

~~~
mkdir -p /etc/systemd/system/getty@tty1.service.d/

echo "[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin alarm --noclear %I 38400 linux
" > /etc/systemd/system/getty@tty1.service.d/autologin.conf
~~~

### MATE Configuration

##### lightdm autologin

~~~
systemctl enable lightdm

groupadd -r autologin
gpasswd -a alarm autologin

echo -e "[Seat:*]
pam-service=lightdm
pam-autologin-service=lightdm-autologin
allow-guest=false
session-wrapper=/etc/lightdm/Xsession
greeter-session=lightdm-gtk-greeter
autologin-user-timeout=0
autologin-session=mate" > /etc/lightdm/lightdm.conf

echo -e "autologin-user=alarm" >> /etc/lightdm/lightdm.conf
~~~

--------------------------------------------------------------------------------

### Finish

##### clean-up package cache (qemu-chroot)

~~~
rm -vf /home/alarm/{install_pkgs.txt,pkglist.txt,upgrade_pkgs.txt}
rm -vf /var/cache/pacman/pkg/*
~~~

##### umount disk

~~~
exit

sudo umount /mnt/root/boot/
sudo umount /mnt/root/
~~~

##### clear url list files

~~~
rm -vf dbase.txt install_pkgs.txt upgrade_pkgs.txt
~~~
