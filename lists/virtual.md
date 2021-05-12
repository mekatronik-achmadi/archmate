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
- https://aur.archlinux.org/packages/genymotion/
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

##### configure qtemu

~~~
echo "Max Hotpluggable >= CPU Count"
echo "GPU Type: Virtio VGA Card"
echo "Accelerator: KVM"
~~~

##### configure genymotion

~~~
sudo rm -f /usr/share/applications/genymotion-player.desktop

echo 'Android API cache'
ls -l ~/.Genymobile/Genymotion/ova/
~~~

~~~
echo 'ARM Translation'
xdg-open https://github.com/m9rco/Genymotion_ARM_Translation

export GENYARM=https://raw.githubusercontent.com/m9rco/Genymotion_ARM_Translation
wget $GENYARM/master/package/Genymotion-ARM-Translation_for_8.0.zip
echo 'Drop File to Virtual Android's screen'
echo 'OK to Flash file'
echo 'Reboot Virtual Android'
~~~

##### configure android-x86

~~~
sudo sed -i "s#\$NET_QEMULINE \$DATA_QEMULINE#\
-net nic -net user,hostfwd=tcp::4444-:5555 \$DATA_QEMULINE#g" \
/usr/bin/qemu-android

mkdir -p ~/.config/android-x86/
cp -f /usr/share/android-x86/config ~/.config/android-x86/
~~~

~~~
Settings -> Network & internet -> Wi-Fi -> VirtWifi
Settings -> Android-x86 Options -> Enable native bridge

FULL = CTRL+ALT+F
BACK = CTRL+ALT+BACKSPACE
HOME = WINDOWS
~~~

~~~
echo 'VirtWifi must connected'
adb disconnect
adb connect localhost:4444
adb install /usr/share/gnirehtet/java/gnirehtet.apk
j_gnirehtet

export REMOTEDIR=/storage/self/primary/Download
adb push file.mp3 $REMOTEDIR/Download/
adb -e shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE \
-d file://$REMOTEDIR/file.mp3
~~~

~~~
echo 'reset device'
rm -f ~/.config/android-x86/data.img
~~~
