##### install qemu
virt-manager virt-viewer
qemu qemu-arch-extra
qemu-guest-agent

##### install virtualbox host
virtualbox virtualbox-host-dkms
virtualbox-guest-iso vde2

--------------------------------------------------------------------------------

##### install iso2usb writer
- https://aur.archlinux.org/packages/kindd/
- https://aur.archlinux.org/packages/ventoy-bin/

##### install virtualbox extension pack
- https://aur.archlinux.org/packages/virtualbox-ext-oracle/

##### install qemu chroot
- https://aur.archlinux.org/packages/binfmt-qemu-static/
- https://aur.archlinux.org/packages/qemu-user-static-bin/

##### install virtual android
- https://aur.archlinux.org/packages/qemu-android-x86/

--------------------------------------------------------------------------------

##### configure virtualbox host

~~~
echo 'vboxdrv
vboxnetadp
vboxnetflt
vboxpci' | sudo tee /etc/modules-load.d/virtualbox.conf

#dkms autoinstall
sudo groupadd vboxusers
sudo gpasswd -a $USER vboxusers
~~~

##### configure qemu libvirt

~~~
sudo groupadd -rf kvm
sudo groupadd -rf libvirt
sudo gpasswd -a $USER kvm
sudo gpasswd -a $USER libvirt
echo " kvm_intel" | sudo tee /etc/modules-load.d/kvm.conf
sudo systemctl enable libvirtd
~~~

~~~
grep -E "(vmx|svm)" --color=always /proc/cpuinfo
virsh -c qemu:///system list
virsh -c qemu:///session list
~~~

##### configure qemu android-x86

~~~
#wget https://github.com/redchenjs/aur-packages/releases/download/anbox-image/houdini_y.sfs
#wget https://github.com/redchenjs/aur-packages/releases/download/anbox-image/houdini_z.sfs

unsquashfs -q -f -d $HOME/.config/android-x86/ /usr/share/android-x86/system.sfs
sudo mount $HOME/.config/android-x86/system.img /mnt/

#mkdir -p houdini_y;rm -rf ./houdini_y/*;unsquashfs -q -f -d ./houdini_y ./houdini_y.sfs
#sudo mkdir -p /mnt/lib/arm/;sudo cp -r ./houdini_y/* /mnt/lib/arm/;rm -r ./houdini_y/
#sudo mv /mnt/lib/arm/libhoudini.so /mnt/lib/libhoudini.so

mkdir -p houdini_z;rm -rf ./houdini_z/*;unsquashfs -q -f -d ./houdini_z ./houdini_z.sfs
sudo mkdir -p /mnt/lib64/arm64/;sudo cp -r ./houdini_z/* /mnt/lib64/arm64/;rm -r ./houdini_z/
sudo mv /mnt/lib64/arm64/libhoudini.so /mnt/lib64/libhoudini.so

sudo mkdir -p /mnt/etc/binfmt_misc/
#echo ':arm_exe:M::\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28::/system/lib/arm/houdini:P' | sudo tee -a /mnt/etc/binfmt_misc/arm_exe
#echo ':arm_dyn:M::\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x28::/system/lib/arm/houdini:P' | sudo tee -a /mnt/etc/binfmt_misc/arm_dyn
echo ':arm64_exe:M::\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7::/system/lib64/arm64/houdini64:P' | sudo tee -a /mnt/etc/binfmt_misc/arm64_exe
echo ':arm64_dyn:M::\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\xb7::/system/lib64/arm64/houdini64:P' | sudo tee -a /mnt/etc/binfmt_misc/arm64_dyn

#sudo sed -i '/^ro.product.cpu.abilist32=x86/ s/$/,armeabi-v7a,armeabi/' /mnt/build.prop
sudo sed -i '/^ro.product.cpu.abilist=x86_64,x86,armeabi-v7a,armeabi/ s/$/,arm64-v8a/' /mnt/build.prop
sudo sed -i '/^ro.product.cpu.abilist64=x86_64/ s/$/,arm64-v8a/' /mnt/build.prop

echo 'persist.sys.nativebridge=1' | sudo tee -a /mnt/build.prop
sudo sed -i 's/ro.dalvik.vm.native.bridge=0/ro.dalvik.vm.native.bridge=libhoudini.so/' /mnt/build.prop

sudo umount /mnt

sudo sed -i "s#\$NET_QEMULINE \$DATA_QEMULINE#-net nic -net user,hostfwd=tcp::4444-:5555 \$DATA_QEMULINE#g" /usr/bin/qemu-android
sudo sed -i "s#file=\$SYSTEMIMG#file=$HOME/.config/android-x86/system.img#g" /usr/bin/qemu-android

sudo rm -f /usr/share/applications/qemu-android.desktop
mkdir -p $HOME/.config/android-x86/
cp -f /usr/share/android-x86/config $HOME/.config/android-x86/
~~~

~~~
qemu-android
echo 'FULL = CTRL+ALT+F
HOME = WINDOWS
BACK = CTRL+ALT+BKSPACE'
~~~

~~~
echo 'Settings -> Network & internet -> Wi-Fi -> VirtWifi'
adb disconnect
adb connect localhost:4444

adb push file.mp3 /storage/self/primary/Download/
adb shell
exit

adb install file.apk
adb install --abi armeabi-v7a file.apk
~~~

~~~
echo 'reset device'
rm -f ~/.config/android-x86/data.img
qemu-android
~~~
