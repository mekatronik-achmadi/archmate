#!/usr/bin/bash

qemu-system-x86_64 -enable-kvm \
-display gtk,grab-on-hover=on,\
zoom-to-fit=on,show-menubar=off \
-m 2048M -cpu host -smp 2 \
-vga virtio -monitor stdio \
-machine type=q35,accel=kvm \
-nic user,model=virtio-net-pci \
-global isa-fdc.fdtypeA=none \
-boot d -cdrom ${1}

################################################################################

#### create virtual disk in host
#qemu-img create vdisk.img 12G
#dd status=progress if=/dev/zero of=vdisk.img bs=1G count=12
#parted vdisk.img mklabel msdos

#### using virtual disk
#-drive file=../vdisk.img,format=raw,if=virtio \

################################################################################

#### add host shared folder
#-device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=shared0 \
#-fsdev local,security_model=none,id=fsdev0,path=../../ArchMate-x86_64/mate_012024/ \

#### mount host shared folder inside guest
#sudo mount -t 9p -o trans=virtio,version=9p2000.L,rw,uid=$USER shared0 /mnt

echo -e "\n"
