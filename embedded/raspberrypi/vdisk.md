### Qemu Install

##### prepare vdisk

~~~
qemu-img create rpi.img 4G
dd status=progress if=/dev/zero of=rpi.img bs=1G count=4

sudo parted rpi.img mklabel msdos

yes | sudo parted rpi.img mkpart primary 0% 200
yes | sudo parted rpi.img mkpart primary 200 100%
yes | sudo parted rpi.img set 1 lba on
yes | sudo parted rpi.img set 1 boot on

sudo losetup --partscan --find --show rpi.img
sudo mkfs.vfat /dev/loop0p1
sudo mkfs.ext4 /dev/loop0p2
sudo losetup -d /dev/loop0
~~~

##### download image

~~~
wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz
~~~

##### deploy image

~~~
sudo mkdir -p /mnt/boot
sudo mkdir -p /mnt/root

sudo losetup --partscan --find --show rpi.img

sudo mount -o rw /dev/loop0p1 /mnt/boot/
sudo mount -o rw /dev/loop0p2 /mnt/root/
~~~

~~~
sudo bsdtar -xpf ArchLinuxARM-rpi-2-latest.tar.gz -C /mnt/root
sudo sync

sudo mv -vf /mnt/root/boot/* /mnt/boot/
sudo sync

sudo umount /mnt/root /mnt/boot

sudo losetup -d /dev/loop0
~~~

##### qemu chrooting

~~~
sudo losetup --partscan --find --show rpi.img

sudo mount -o rw /dev/loop0p2 /mnt/root/
sudo mount -o rw /dev/loop0p1 /mnt/root/boot/
~~~

~~~
sudo cp -vf /usr/bin/qemu-arm-static /mnt/root/usr/bin/

sudo arch-chroot /mnt/root /bin/bash
uname -a
exit
~~~

~~~
sudo umount /mnt/root/boot/
sudo umount /mnt/root/

sudo losetup -d /dev/loop0
~~~
