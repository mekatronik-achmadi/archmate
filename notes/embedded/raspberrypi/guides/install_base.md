# RaspberryPi Base Installation

## Disk Install

### prepare disk

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
echo ${DEVDISK}

sudo parted ${DEVDISK} mklabel msdos
```

```sh
sudo parted ${DEVDISK} mkpart primary 0% 200
sudo parted ${DEVDISK} mkpart primary 200 100%

sudo mkfs.vfat -F 32 ${DEVDISK}1
sudo parted ${DEVDISK} set 1 boot on
#sudo parted ${DEVDISK} set 1 lba on
sudo mkfs.ext4 ${DEVDISK}2
```

### download image

```sh
wget -c http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-armv7-latest.tar.gz
```

### deploy image

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
echo ${DEVDISK}

sudo mkdir -p /mnt/mmc/{boot,root}
sudo mount ${DEVDISK}1 /mnt/mmc/boot
sudo mount ${DEVDISK}2 /mnt/mmc/root

mkdir -p armv7h/;cd armv7h/

sudo bsdtar -xpf ../ArchLinuxARM-rpi-armv7-latest.tar.gz -C /mnt/mmc/root
sudo sync

sudo mv -vf /mnt/mmc/root/boot/* /mnt/mmc/boot/
sudo sync

sudo umount /mnt/mmc/root /mnt/mmc/boot
```

--------------------------------------------------------------------------------

## Qemu run

### mount disk (host-pc)

```sh
sudo fdisk -l
export DEVDISK='/dev/sdb'
```

```sh
sudo mount ${DEVDISK}2 /mnt/mmc/root
sudo mount ${DEVDISK}1 /mnt/mmc/root/boot
```

### copy qemu-arm-static (host-pc)

```sh
sudo cp -vf /usr/bin/qemu-arm-static /mnt/mmc/root/usr/bin/
```

### test chroot into mounted sdcard (host-pc)

```sh
sudo arch-chroot /mnt/mmc/root /bin/bash
```

```sh
pacman -V
```

```sh
exit
```

--------------------------------------------------------------------------------

## Install packages

### chroot into mounted sdcard (host-pc)

```sh
sudo arch-chroot /mnt/mmc/root /bin/bash
```

### generate locale (qemu-chroot)

```sh
echo "LANG=en_US.UTF-8" > /etc/locale.conf
echo "en_US ISO-8859-1" > /etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
```

### download database (host-pc)

```sh
mkdir -p databases/;cd databases/

echo "
http://mirror.archlinuxarm.org/armv7h/core/core.db
http://mirror.archlinuxarm.org/armv7h/extra/extra.db
http://mirror.archlinuxarm.org/armv7h/community/community.db
http://mirror.archlinuxarm.org/armv7h/alarm/alarm.db
http://mirror.archlinuxarm.org/armv7h/aur/aur.db
" > ../dbase.txt
wget -c -i ../dbase.txt
cd ../

sudo mkdir -p /mnt/mmc/root/var/lib/pacman/sync/
sudo rsync -avh databases/ /mnt/mmc/root/var/lib/pacman/sync/
```

### generate upgrade packages urls (qemu-chroot)

```sh
pacman -Sup > /home/alarm/upgrade_pkgs.txt
```

### download upgrade packages (host-pc)

```sh
cp -vf /mnt/mmc/root/home/alarm/upgrade_pkgs.txt ./

mkdir -p packages/official/;cd packages/official/
wget -c -i ../../upgrade_pkgs.txt
cd ../../

sudo mkdir -p /mnt/mmc/root/var/cache/pacman/pkg/
sudo rsync -avh packages/official/ /mnt/mmc/root/var/cache/pacman/pkg/
```

### upgrade packages (qemu-chroot)

```sh
sed -i "s#= Required DatabaseOptional#= Never#g" /etc/pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" /etc/pacman.conf
sed -i "s#= Optional#= Never#g" /etc/pacman.conf

pacman -Su --noconfirm
```

### copy install packages list (host-pc)

```sh
cp -vf ../archrpi/pkg_basic.txt /mnt/mmc/root/home/alarm/basiclist.txt
cp -vf ../archrpi/pkg_more.txt /mnt/mmc/root/home/alarm/morelist.txt
cp -vf ../archrpi/pkg_server.txt /mnt/mmc/root/home/alarm/serverlist.txt
cp -vf ../archrpi/pkg_openbox.txt /mnt/mmc/root/home/alarm/openboxlist.txt
```

### generate packages urls (qemu-chroot)

```sh
pacman -Sp $(cat /home/alarm/basiclist.txt) > /home/alarm/basic_pkgs.txt
pacman -Sp $(cat /home/alarm/morelist.txt) > /home/alarm/more_pkgs.txt
pacman -Sp $(cat /home/alarm/serverlist.txt) > /home/alarm/server_pkgs.txt
pacman -Sp $(cat /home/alarm/openboxlist.txt) > /home/alarm/openbox_pkgs.txt
```