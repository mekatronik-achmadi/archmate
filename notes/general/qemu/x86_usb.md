# QEMU USB

## x86-Linux with BusyBox and USB rootfs

### kernel

```sh
tar xvf linux-*
cd linux-*/
make x86_64_defconfig

echo "Enabled USB Storage options"
make menuconfig
```

```text
General setup
    ((TinyLinux)) Default hostname

Device Drivers
    [*] PCI support
    SCSI device support
        -*- SCSI device support
        <*> SCSI disk support
        <*> SCSI generic support
    HID support
        USB HID support
            <*> USB HID transport layer
    [*] USB support
        <*>   Support for Host-side USB
        [*]   PCI based USB host interface
        <*>   xHCI HCD (USB 3.0) support
        <*>     Generic xHCI driver for a platform device
        <*>   EHCI HCD (USB 2.0) support
        <*>     Generic EHCI driver for a platform device
        <*>   OHCI HCD (USB 1.1) support
        <*>     Generic OHCI driver for a platform device
        <*>   UHCI HCD (most Intel and VIA) support
        <*>   USB Mass Storage support

File systems
    <*> The Extended 3 (ext3) filesystem
    -*- The Extended 4 (ext4) filesystem
    DOS/FAT/NT Filesystems
        <*> MSDOS fs support
        <*> VFAT (Windows-95) fs support
    Pseudo filesystems
        -*- Tmpfs virtual memory file system support (former shm fs)
```

```sh
make -j$(nproc) all
cd ../
```

### busybox

```sh
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

### check usb-disk device

- **WARNING**: make sure usb-disk are in /dev/sdb

  ```sh
  sudo fdisk -l
  sudo fdisk -l | grep sdb
  ```

### prepare usb-disk

```sh
sudo dd status=progress bs=1k count=2048 if=/dev/zero of=/dev/sdb
sudo parted /dev/sdb mklabel msdos
sudo parted /dev/sdb mkpart primary 0% 100%
sudo parted /dev/sdb set 1 lba on
sudo parted /dev/sdb set 1 boot on
sudo mkfs.ext4 /dev/sdb1
```

### get UUID of usb-disk

```sh
sudo blkid /dev/sdb1 -s UUID -o value
```

### rootfs

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

echo 'BusyBox populate device......'
sysctl -w kernel.hotplug=/sbin/mdev
mdev -s

echo 'Waiting Final Root (5s)......'
for i in 1 2 3 4 5;do sleep 1;done

echo 'Mounting Final Root......'
mdev -s
mkdir -p /newroot
mount -t ext4 UUID=b1fb1425-b942-4160-906e-678be17f2b13 /newroot

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

```sh
mkdir -p newroot/
sudo rsync -avh busybox-*/_install/ newroot/
sudo rm -rvf newroot/etc/init.d
```

### install BusyBox and Linux

```sh
sudo mkdir -p /mnt/img/drive/
sudo mount -o rw /dev/sdb1 /mnt/img/drive/

sudo rsync -avh newroot/ /mnt/img/drive/

sudo cp -vf linux-*/arch/x86/boot/bzImage /mnt/img/drive/vmlinuz
sudo chown -vf root:root /mnt/img/drive/vmlinuz

sudo cp -vf busybox-*/rootfs_img /mnt/img/drive/rootfs
sudo chown -vf root:root /mnt/img/drive/rootfs

sudo umount /mnt/img/drive/
```

### install Syslinux

```sh
sudo dd status=progress conv=notrunc bs=440 count=1 if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sdb

sudo mount -o rw /dev/sdb1 /mnt/img/drive/
mkdir -p /mnt/img/drive/boot/

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
    INITRD ../rootfs
    APPEND root=/dev/ram rdinit=/sbin/init
" | sudo tee /mnt/img/drive/boot/extlinux.conf

cd /mnt/img/drive/
sudo extlinux --install boot/

cd -
sudo umount /mnt/img/drive
```
