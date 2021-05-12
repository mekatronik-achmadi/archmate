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
wget https://raw.githubusercontent.com/m9rco/Genymotion_ARM_Translation/master/package/Genymotion-ARM-Translation_for_8.0.zip

unsquashfs -q -f -d $HOME/.config/android-x86/ /usr/share/android-x86/system.sfs
sudo mount $HOME/.config/android-x86/system.img /mnt/

unzip Genymotion-ARM-Translation_for_8.0.zip
sudo cp -rf system/* /mnt/;rm -r ./system/

sudo sed -i '/^ro.product.cpu.abilist=x86_64,x86/ s/$/,armeabi-v7a,armeabi/' /mnt/build.prop
sudo sed -i '/^ro.product.cpu.abilist32=x86/ s/$/,armeabi-v7a,armeabi/' /mnt/build.prop

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
