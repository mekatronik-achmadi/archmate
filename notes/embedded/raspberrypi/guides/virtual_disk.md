# Virtual Disk

## Disk Install

### prepare vdisk

```sh
qemu-img create rpi.img 4G
dd status=progress if=/dev/zero of=rpi.img bs=1G count=4

sudo parted rpi.img mklabel msdos

yes | sudo parted rpi.img mkpart primary 0% 200
yes | sudo parted rpi.img mkpart primary 200 100%

sudo losetup --partscan --find --show rpi.img
yes | sudo mkfs.vfat -F 32 /dev/loop0p1
yes | sudo parted rpi.img set 1 boot on
yes | sudo parted rpi.img set 1 lba on
yes | sudo mkfs.ext4 /dev/loop0p2
sudo losetup -d /dev/loop0
```

### download image

```sh
wget -c http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-armv7-latest.tar.gz
```

### deploy image

```sh
sudo mkdir -p /mnt/img/{boot,root}

sudo losetup --partscan --find --show rpi.img

sudo mount -o rw /dev/loop0p1 /mnt/img/boot/
sudo mount -o rw /dev/loop0p2 /mnt/img/root/
```

```sh
sudo bsdtar -xpf ArchLinuxARM-rpi-armv7-latest.tar.gz -C /mnt/img/root
sudo sync

sudo mv -vf /mnt/img/root/boot/* /mnt/img/boot/
sudo sync

sudo umount /mnt/img/root /mnt/img/boot

sudo losetup -d /dev/loop0
```

### qemu chrooting

```sh
sudo losetup --partscan --find --show rpi.img

sudo mount -o rw /dev/loop0p2 /mnt/img/root/
sudo mount -o rw /dev/loop0p1 /mnt/img/root/boot/
```

```sh
sudo cp -vf /usr/bin/qemu-arm-static /mnt/img/root/usr/bin/

sudo arch-chroot /mnt/img/root /bin/bash
uname -a
exit
```

```sh
sudo umount /mnt/img/root/boot/
sudo umount /mnt/img/root/

sudo losetup -d /dev/loop0
```

## RootFS Backup

### prepare vdisk

```sh
qemu-img create rpi.img 4G
dd status=progress if=/dev/zero of=rpi.img bs=1G count=4

sudo parted rpi.img mklabel msdos

yes | sudo parted rpi.img mkpart primary 0% 200
yes | sudo parted rpi.img mkpart primary 200 100%

sudo losetup --partscan --find --show rpi.img
yes | sudo mkfs.vfat -F 32 /dev/loop0p1
yes | sudo parted rpi.img set 1 boot on
yes | sudo parted rpi.img set 1 lba on
yes | sudo mkfs.ext4 /dev/loop0p2
sudo losetup -d /dev/loop0
```

### copy rootfs

```sh
sudo mkdir -p /mnt/img/{boot,root}

sudo losetup --partscan --find --show rpi.img

sudo mount -o rw /dev/loop0p1 /mnt/img/boot/
sudo mount -o rw /dev/loop0p2 /mnt/img/root/
```

```sh
sudo mkdir -p /mnt/mmc/{boot,root}

sudo mount /dev/sdb1 /mnt/mmc/boot/
sudo mount /dev/sdb2 /mnt/mmc/root/
```

```sh
sudo rsync -avh /mnt/mmc/boot/ /mnt/img/boot/
sudo rsync -avh /mnt/mmc/root/ /mnt/img/root/

#sudo rsync -avh /mnt/img/boot/ /mnt/mmc/boot/
#sudo rsync -avh /mnt/img/root/ /mnt/mmc/root/
```

```sh
sudo umount /mnt/img/root /mnt/img/boot
sudo umount /mnt/mmc/root /mnt/mmc/boot

sudo losetup -d /dev/loop0
```

