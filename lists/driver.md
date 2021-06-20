##### install libva driver
intel-media-driver
libva-intel-driver
libva-vdpau-driver
libva-mesa-driver
libvdpau-va-gl
libva-utils
vdpauinfo

##### install vulkan mesa driver
vulkan-radeon lib32-vulkan-radeon
vulkan-icd-loader lib32-vulkan-icd-loader
lib32-vulkan-intel lib32-vulkan-mesa-layers
vulkan-tools vulkan-intel vulkan-mesa-layers

##### install additional udev
python-pyudev android-udev

--------------------------------------------------------------------------------

##### install nvidia driver

~~~
don't use kernel-5.12.patch on prepare
~~~
- https://aur.archlinux.org/packages/lib32-nvidia-390xx-utils/
- https://aur.archlinux.org/packages/nvidia-390xx-utils/
- https://aur.archlinux.org/packages/nvidia-390xx-dkms/
- https://aur.archlinux.org/packages/optimus-manager/
- https://aur.archlinux.org/packages/glmark2-git/

##### install image scanner
- https://aur.archlinux.org/packages/brscan3/
- https://aur.archlinux.org/packages/brother-mfc-j220/

##### install printer canon
- https://aur.archlinux.org/packages/cnijfilter-ip2700series/

##### install printer hp
- https://aur.archlinux.org/packages/hplip-plugin/
- https://aur.archlinux.org/packages/hpuld/
- https://aur.archlinux.org/packages/hpoj/

##### install bluetooth deprecated
- https://aur.archlinux.org/packages/bluez-hcitool/
- https://aur.archlinux.org/packages/bluez-rfcomm/

--------------------------------------------------------------------------------

##### configure nvidia optimus

~~~
sudo systemctl enable optimus-manager
sudo systemctl start optimus-manager
~~~

~~~
optimus-manager --no-confirm --switch nvidia
optimus-manager --no-confirm --switch intel
~~~

~~~
sudo sed -i "s#startup_mode=intel#startup_mode=nvidia#g" /usr/share/optimus-manager.conf
~~~
