## Build Qemu ARM-Linux

### prepare

```sh
wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.1.tar.xz
tar xvf linux-*
cd linux-*/

export ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabihf-
```

### start building

```sh
make vexpress_defconfig
make -j$(nproc) all
file arch/arm/boot/compressed/vmlinux
cd ../
```

### simple init rootfs

```c
#include <stdio.h>

void main()
{
    printf("Simple init ...\n");
    while(1);
}
```

```sh
${CROSS_COMPILE}gcc -static -o init main.c
echo init | cpio -o --format=newc > rootfs
```

### run test

```sh
cp -vf linux-*/arch/arm/boot/zImage ./vmlinuz
cp -vf linux-*/arch/arm/boot/dts/vexpress-v2p-ca9.dtb ./board.dtb

qemu-system-arm \
-smp 2 \
-monitor stdio \
-kernel vmlinuz \
-initrd rootfs \
-dtb board.dtb \
-M vexpress-a9 \
-cpu cortex-a9 -m 256M \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/init"
```

## Build BusyBox shell

### prepare

```sh
wget https://busybox.net/downloads/busybox-1.31.0.tar.bz2
tar xvf busybox-*
cd busybox-*/

export ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabihf-
```

### configs

```sh
make defconfig
make menuconfig
```

```text
Settings
    --- Build Options
    [*] Build static binary (no shared libs)
```

### builds

```sh
make -j$(nproc) all
make install
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
/sbin/mdev -s

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

### run test

```sh
cp -vf linux-*/arch/arm/boot/zImage ./vmlinuz
cp -vf linux-*/arch/arm/boot/dts/vexpress-v2p-ca9.dtb ./board.dtb
cp -vf busybox-*/rootfs_img ./rootfs

qemu-system-arm \
-smp 2 \
-monitor stdio \
-kernel vmlinuz \
-initrd rootfs \
-dtb board.dtb \
-M vexpress-a9 \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/sbin/init"
```

## Build Qemu x86-Linux

### x86_64 with kvm

```sh
tar xvf linux-*
cd linux-*/

make x86_64_defconfig
make -j$(nproc) all
file arch/x86/boot/compressed/vmlinux
cd ../

gcc -static -o init main.c
echo init | cpio -o --format=newc > rootfs

cp -vf linux-*/arch/x86/boot/bzImage ./vmlinuz

qemu-system-x86_64 -monitor stdio \
-smp 2 -m 256M -machine accel=kvm \
-kernel vmlinuz -initrd rootfs \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/init"
```

### i386 with kvm

```sh
tar xvf linux-*
cd linux-*/

make i386_defconfig
make -j$(nproc) all
file arch/x86/boot/compressed/vmlinux
cd ../

gcc -m32 -static -o init main.c
echo init | cpio -o --format=newc > rootfs

cp -vf linux-*/arch/x86/boot/bzImage ./vmlinuz

qemu-system-i386 -monitor stdio \
-smp 2 -m 256M -machine accel=kvm \
-kernel vmlinuz -initrd rootfs \
-display gtk,zoom-to-fit=on \
-append "root=/dev/ram rdinit=/init"
```

## Alternatives

### Some Kernel Configs

```sh
export ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabihf-

make vexpress_defconfig
make menuconfig
```

```text
General setup
    [*] Compile also drivers which will not load
    ((none)) Default hostname
    [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
    [*] Embedded system
    [*]   Support initial ramdisks compressed using gzip
    [*]   Support initial ramdisks compressed using bzip2
    [*]   Support initial ramdisks compressed using LZMA
    [*]   Support initial ramdisks compressed using XZ

System Type
    [*] MMU-based Paged Memory Management Support
        ARM system type (Allow multiple platforms to be selected)
        Multiple platform selection
            [*] ARMv6 based platforms (ARM11)
    [*] ARM Ltd. Versatile family

Kernel Features
    -*- Use the ARM EABI to compile the kernel
    [*]   Allow old ABI binaries to run with this kernel (EXPERIMENTAL)

Floating point emulation
    [*] NWFPE math emulation
    [*] VFP-format floating point maths

[*] Enable loadable module support

[*] Networking support
    <*>   Plan 9 Resource Sharing Support (9P2000)
        <*>   9P Virtio Transport

Device Drivers
    [*] PCI support
    Generic Driver Options
        [*] Maintain a devtmpfs filesystem to mount at /devs
        [*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs
    SCSI device support
        <*> SCSI device support
        <*> SCSI disk support
        <*> SCSI generic support
    Input device support
        <*>   Event interface
    Character devices
        -*- Enable TTY
        -*-   Virtual terminal
        <*> Virtio console
    < > Generic Thermal sysfs driver
    Graphics support
        <*> DRM Support for PL111 CLCD Controller
        Console display driver support
             [*] Framebuffer Console support
        [*] Bootup logo
            [*]   Standard black and white Linux logo
            [*]   Standard 16-color Linux logo
            [*]   Standard 224-color Linux logo
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
    <*> MMC/SD/SDIO card support
        <*>   Secure Digital Host Controller Interface support
        <*>   MMC/SD/SDIO over SPI
        <*>   Toshiba Type A SD/MMC Card Interface Driver
        <*>   Broadcom BCM2835 SDHOST MMC Controller support
        <*>   MediaTek SD/MMC Card Interface support
    [*] Virtio drivers
        <*>   PCI driver for virtio devices
        [*]     Support for legacy virtio draft 0.9.X and older devices (NEW)
        <*>   Virtio input driver
        <*>   Platform bus driver for memory mapped virtio devices
        [*]     Memory mapped virtio devices parameter parsing

File systems
    <*> The Extended 3 (ext3) filesystem
    -*- The Extended 4 (ext4) filesystem
    DOS/FAT/NT Filesystems
        <*> MSDOS fs support
        <*> VFAT (Windows-95) fs support
        <*> NTFS file system support
        [*]   NTFS write support
    Pseudo filesystems
        -*- Tmpfs virtual memory file system support (former shm fs)
    [*] Miscellaneous filesystems
        <*>   SquashFS 4.0 - Squashed file system support
        [*]     Squashfs XATTR support
        [*]     Include support for ZLIB compressed file systems (NEW)
        [*]     Include support for LZ4 compressed file systems
        [*]     Include support for LZO compressed file systems
        [*]     Include support for XZ compressed file systems
        [*]     Include support for ZSTD compressed file systems
        [*]     Use 4K device block size?
    [*] Network File Systems
        <*>   Plan 9 Resource Sharing Support (9P2000)
```

```sh
cp -vf .config ../kernelconfig
make -j$(nproc) all
file arch/arm/boot/compressed/vmlinux
cd ../
```

### manually mount 9P shared folder

```sh
-virtfs local,id=shared_folder_dev_0,path=test_folder,security_model=none,mount_tag=shared0
```

```sh
-fsdev local,security_model=none,id=fsdev0,path=test_folder \
-device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=shared0
```

```sh
mount -t 9p trans=virtio,version=9p2000.L,rw share0 /mnt
```

### redirect guest serial to host stdio

```sh
-serial stdio -append "console=ttyS0"
-serial stdio -append "console=ttyAMA0"
-serial stdio -append "console=ttyACM0"
```

### redirect host-usb to guest-usb

```sh
-usb -device usb-host,vendorid=0xAAAA,productid=0xBBBB
```

```sh
-usb -device usb-host,vendorid=0x0403,productid=0x6001 \
-device usb-host,vendorid=0x067b,productid=0x2303 \
-device usb-host,vendorid=0x0483,productid=0x5740
```
