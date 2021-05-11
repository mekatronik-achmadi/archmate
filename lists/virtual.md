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
