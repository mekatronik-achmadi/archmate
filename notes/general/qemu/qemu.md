# QEMU General

## prepare virtual disk

```sh
qemu-img create vdisk.img 12G
dd status=progress if=/dev/zero of=vdisk.img bs=1G count=12

sudo parted vdisk.img mklabel msdos
sudo parted vdisk.img mkpart primary 0% 100%
sudo parted vdisk.img set 1 lba on
sudo parted vdisk.img set 1 boot on

sudo losetup --partscan --find --show vdisk.img
sudo mkfs.ext4 /dev/loop0p1
sudo losetup -d /dev/loop0
```

## test mount the disk

```sh
sudo mkdir -p /mnt/vdisk/root
sudo mount -o rw /dev/loop0p1 /mnt/vdisk/root/
sudo umount /mnt/vdisk/root/
```

## run test

```sh
qemu-system-x86_64 -m 1024M \
-smp 2 -monitor stdio -enable-kvm \
-drive file=vdisk.img,format=raw,if=virtio \
-display gtk,zoom-to-fit=on
```

## boot from ISO image

```sh
qemu-system-x86_64 -m 2048M \
-smp 2 -monitor stdio -enable-kvm \
-boot d -cdrom achmadi-cli-x86_64.iso \
-drive file=vdisk.img,format=raw,if=virtio \
-display gtk,zoom-to-fit=on
```

## boot from USB Disk

```sh
qemu-system-x86_64 -m 2048M \
-smp 2 -monitor stdio -enable-kvm \
-usb /dev/sdb \
-drive file=vdisk.img,format=raw,if=virtio \
-display gtk,zoom-to-fit=on
```

## using a shared folder

```sh
qemu-system-x86_64 -m 2048M \
-smp 2 -monitor stdio -enable-kvm \
-drive file=vdisk.img,format=raw,if=virtio \
-fsdev local,security_model=none,id=fsdev0,path=shared_folder \
-device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=shared0 \
-display gtk,zoom-to-fit=on
```

```sh
echo 'mount shared0 folder'
sudo mount -t 9p -o rw,trans=virtio,version=9p2000.L shared0 /mnt
```
