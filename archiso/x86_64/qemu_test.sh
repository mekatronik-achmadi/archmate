#!/usr/bin/bash

#qemu-img create vdisk.img 12G
#dd status=progress if=/dev/zero of=vdisk.img bs=1G count=12
#sudo parted vdisk.img mklabel msdos

qemu-system-x86_64 -m 1536M \
-smp 2 -monitor stdio -enable-kvm \
-display gtk,zoom-to-fit=on \
-nic user,model=virtio-net-pci \
-boot d -cdrom ./archlinux-mate-x86_64.iso #\
#-drive file=vdisk.img,format=raw,if=virtio \
#-fsdev local,security_model=none,id=fsdev0,path=shared_folder \
#-device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=shared0 \

# sudo mount -t 9p -o trans=virtio,version=9p2000.L,rw share0 /mnt

echo -e "\n"
