# QEMU x86

## x86-Linux with BusyBox and Shared-Folder

### kernel

```sh
tar xvf linux-*
cd linux-*/
make i386_defconfig

echo "Enabled 9P PCI Virtio options"
make menuconfig
```

```text
General setup
    ((TinyLinux)) Default hostname

[*] Networking support
    <*>   Plan 9 Resource Sharing Support (9P2000)
        <*>   9P Virtio Transport

Device Drivers
    [*] PCI support
        [*] PCI controller drivers
    [*] Virtio drivers
        <*>   PCI driver for virtio devices
        [*]     Support for legacy virtio draft 0.9.X and older devices (NEW)
        <*>   Virtio input driver
        <*>   Platform bus driver for memory mapped virtio devices
        [*]     Memory mapped virtio devices parameter parsing

File systems
    [*] Network File Systems
        <*>   Plan 9 Resource Sharing Support (9P2000)
```

```sh
make -j$(nproc) all
cd ../
```

### busybox

```sh
export CFLAGS=-m32
export LDFLAGS=-m32
export CXXFLAGS=-m32

tar xvf busybox-*
cd busybox-*/
make defconfig

echo "Enabled BusyBox as static binary"
make menuconfig
```

```text
Settings
    --- Build Options
    [*] Build static binary (no shared libs)
```

```sh
make -j$(nproc) all
make install
```

### rootfs automount shared-folder

```sh
cd _install
sudo su

mkdir -p {proc,sys,dev,mnt,etc/init.d}
rm -f linuxrc

echo '#!/bin/sh' > etc/init.d/rcS
echo "
dmesg -n 1

echo 'BusyBox mount proc and sysfs......'
mount -t proc none /proc
mount -t sysfs none /sys
/sbin/mdev -s

echo 'BusyBox mount shared0......'
mount -t 9p -o rw,trans=virtio,version=9p2000.L shared0 /mnt

echo 'BusyBox init Done ......'
clear

cat << !
 _____ _               _     _
|_   _(_)_ __  _   _  | |   (_)_ __  _   ___  __
  | | | | '_ \| | | | | |   | | '_ \| | | \ \/ /
  | | | | | | | |_| | | |___| | | | | |_| |>  <
  |_| |_|_| |_|\__, | |_____|_|_| |_|\__,_/_/\_\_
               |___/

         Welcome to Tiny Linux
!

setsid cttyhack sh
exec /bin/sh
" >> etc/init.d/rcS
chmod a+x etc/init.d/rcS

exit

sudo chown -Rvf root:root *
find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../rootfs_img

cd ../../
```

### run test with kvm

```sh
mkdir -p test_folder/
echo "coba" | tee test_folder/test.txt
```

```sh
cp -vf linux-*/arch/x86/boot/bzImage ./vmlinuz
cp -vf busybox-*/rootfs_img ./rootfs

qemu-system-i386 -monitor stdio -smp 2 \
-m 256M -kernel vmlinuz -initrd rootfs -machine accel=kvm \
-append "root=/dev/ram rdinit=/sbin/init" -display gtk,zoom-to-fit=on \
-virtfs local,id=shared_folder_dev_0,path=test_folder,security_model=none,mount_tag=shared0
```

```sh
qemu-system-i386 -monitor stdio \
-smp 2 -m 256M -machine accel=kvm \
-kernel vmlinuz -initrd rootfs \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/sbin/init" \
-fsdev local,security_model=none,id=fsdev0,path=test_folder \
-device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=shared0
```

## x86-Linux with BusyBox, Shared-Folder, Root-Image, and Syslinux

### create Root-Image

```sh
qemu-img create root.img 512M
dd status=progress if=/dev/zero of=root.img bs=1M count=512

sudo parted root.img mklabel msdos
sudo parted root.img mkpart primary 0% 100%
sudo parted root.img set 1 lba on
sudo parted root.img set 1 boot on

sudo losetup --partscan --find --show root.img
sudo mkfs.ext4 /dev/loop0p1
```

### install BusyBox and Linux

```sh
sudo mkdir -p /mnt/img/drive/
sudo mount -o rw /dev/loop0p1 /mnt/img/drive/

sudo chown -Rvf root:root busybox-*/_install/*
sudo rsync -avh busybox-*/_install/ /mnt/img/drive/

sudo cp -vf linux-*/arch/x86/boot/bzImage /mnt/img/drive/vmlinuz
sudo chown -vf root:root /mnt/img/drive/vmlinuz
```

### install Syslinux

```sh
sudo umount /mnt/img/drive
sudo dd status=progress conv=notrunc bs=440 count=1 if=/usr/lib/syslinux/bios/mbr.bin of=/dev/loop0
sudo losetup -d /dev/loop0
```

```sh
sudo mount -t ext4 -o loop -o offset=$((512*2048)) -o rw root.img /mnt/img/drive/
sudo mkdir -p /mnt/img/drive/boot/

sudo cp -vf /usr/lib/syslinux/bios/menu.c32 /mnt/img/drive/boot/
sudo cp -vf /usr/lib/syslinux/bios/libutil.c32 /mnt/img/drive/boot/

echo "UI menu.c32
PROMPT 1
TIMEOUT 50
DEFAULT TinyLinux

MENU TITLE Tiny-Linux Boot Menu

LABEL TinyLinux
    MENU LABLE Mini-Linux
    LINUX ../vmlinuz
    APPEND root=/dev/sda1 rw
" | sudo tee /mnt/img/drive/boot/extlinux.conf

cd /mnt/img/drive/
sudo extlinux --install boot/
```

```sh
cd -
sudo umount /mnt/img/drive
```

### run test with kvm

```sh
qemu-system-i386 -monitor stdio \
-smp 2 -m 256M -machine accel=kvm \
-drive file=root.img,format=raw \
-display gtk,zoom-to-fit=on \
-virtfs local,id=shared_folder_dev_0,path=test_folder,security_model=none,mount_tag=shared0
```

## x86-Linux with BusyBox switch to Root-Image

### BusyBox for temporary rootfs

```sh
cd busybox-*/_install/
sudo su

mkdir -p {proc,sys,dev,mnt,etc/init.d}
rm -f linuxrc

echo '#!/bin/sh' > etc/init.d/rcS
echo "
dmesg -n 1

echo 'BusyBox mount proc and sysfs......'
mount -t proc none /proc
mount -t sysfs none /sys

echo 'BusyBox populate device......'
sysctl -w kernel.hotplug=/sbin/mdev
mdev -s

echo 'Mounting Final Root......'
mdev -s
mkdir -p /newroot
mount -t ext4 /dev/sda1 /newroot

echo 'Prepare Final Root......'
mount -t proc none /newroot/proc
mount -t sysfs none /newroot/sys
umount /proc /sys
chroot /newroot sysctl -w kernel.hotplug=/sbin/mdev
chroot /newroot mdev -s

echo 'Busybox init Done......'
clear

cat << !
 _____ _               _     _
|_   _(_)_ __  _   _  | |   (_)_ __  _   ___  __
  | | | | '_ \| | | | | |   | | '_ \| | | \ \/ /
  | | | | | | | |_| | | |___| | | | | |_| |>  <
  |_| |_|_| |_|\__, | |_____|_|_| |_|\__,_/_/\_\_
               |___/

         Welcome to Tiny Linux
!

chroot /newroot setsid cttyhack sh
chroot /newroot /bin/ash
" >> etc/init.d/rcS
chmod a+x etc/init.d/rcS

exit

sudo chown -Rvf root:root *
find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../rootfs_img

cd ../../
```

### create root image

```sh
qemu-img create root.img 512M
dd status=progress if=/dev/zero of=root.img bs=1M count=512

sudo parted root.img mklabel msdos
sudo parted root.img mkpart primary 0% 100%
sudo parted root.img set 1 lba on
sudo parted root.img set 1 boot on

sudo losetup --partscan --find --show root.img
sudo mkfs.ext4 /dev/loop0p1
```

```sh
mkdir -p newroot/
sudo rsync -avh busybox-*/_install/ newroot/
sudo rm -rvf newroot/etc/init.d
```

```sh
sudo mkdir -p /mnt/img/drive/
sudo mount -o rw /dev/loop0p1 /mnt/img/drive/

sudo chown -Rvf root:root busybox-*/_install/*
sudo rsync -avh newroot/ /mnt/img/drive/

sudo umount /mnt/img/drive
sudo losetup -d /dev/loop0
```

### run test with kvm

```sh
cp -vf linux-*/arch/x86/boot/bzImage ./vmlinuz
cp -vf busybox-*/rootfs_img ./rootfs

qemu-system-x86_64 -monitor stdio \
-drive file=root.img,format=raw \
-smp 2 -m 256M -machine accel=kvm \
-kernel vmlinuz -initrd rootfs \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/sbin/init"
```
