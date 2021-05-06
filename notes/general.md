### bash execute command string

~~~
bash -c "command_string"
bash -c "command_string1 && command_string2"
bash -c "echo -e \"string \\\"quoted_string\\\";\" >> /filepath"
~~~

### custom prompt

~~~
PS1='\n\[\033(0\]l\[\033(B\][$(pwd)]\n\[\033(0\]m\[\033(B\]\[\033(0\]q\[\033(B\](\u@\h):\$ '
sudo nano /etc/skel/.bashrc
cp -vf /etc/skel/.bashrc ~/
~~~

### show password feedback for sudo

~~~
echo -e "Defaults pwfeedback" >> /etc/sudoers
~~~

### get user homedir path

~~~
read username
homedir=$( getent passwd $username | cut -d: -f6 )
echo -e $homedir
~~~

### environment variables

~~~
set
printenv
printenv HOME
echo -e $HOME
source input_file
export VARIABLE="value"
env VARIABLE="value" <command>
cat /etc/profile
ls /etc/profile.d/
~~~

### cat file content line by line

~~~
IFS=$'\n'
for i in `cat file`;do echo $i;done > result.txt
for i in $(cat file);do echo $i;done > result.txt
for i in (<file);do echo $i;done > result.txt
~~~

### custom keyboard map

~~~
# Unicode to Hex: U+xxxx -> 0x100xxxx
# example: Arabic Unicode: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode
# example: Arabic Maddah Above: U+0653
# example: add 0x1000653 to map /usr/share/X11/xkb/symbols/ara
~~~

~~~
locale -av
setxkbmap -layout us
setxkbmap -layout ara
setxkbmap -layout ara -variant buckwalter
~~~

### get fonts list

~~~
fc-list -f '%{file}\n' :lang=ar
fc-list | grep -i <pattern>
fc-match <alias>
~~~

### fix time stamp problems

~~~
touch <file_name>
~~~

### tmux commands

~~~
#Session => Window => Pane
~~~

~~~
Crtl+B %	[split pane vertically]
Crtl+B "	[split pane horizontally]
Crtl+B <Arrow>	[select active pane]
Crtl+B z	[toggle pane fullscreen]
Crtl+B c	[new window]
Crtl+B <Number>	[select active window]
exit		[exit tmux or window or pane]
~~~

### virtual serial port

~~~
socat -d -d PTY PTY
socat -d -d PTY,link=/dev/ttyS2 PTY,link=/dev/ttyS2
socat -d -d pty,raw,echo=0 pty,raw,echo=0
socat -d -d /dev/YOURPORT,raw,echo=0,bHEREBAUDRATE /dev/YOURPORT,raw,echo=0,bHEREBAUDRATE
socat -d -d tcp-l:5760 /dev/YOURPORT,raw,echo=0,bHEREBAUDRATE
lsof -c socat
~~~

### create virtual serial communication

~~~
socat -d -d pty,raw,echo=0 pty,raw,echo=0
sudo ln -sf /dev/pts/2 /dev/ttyV2
sudo ln -sf /dev/pts/3 /dev/ttyV3
minicom -b 9600 -D /dev/ttyVUSB2
minicom -b 9600 -D /dev/ttyVUSB3
~~~

### intercep serial port

~~~
sudo interceptty -s 'ispeed 38400 ospeed 38400' /dev/ttyACM0 /dev/coba
~~~

### library checking

~~~
ls /usr/lib/libNAME.so
ld --verbose -lNAME
ldd ./appname | grep NAME
~~~

### xorg module checking

~~~
less /var/log/Xorg.0.log | grep -i <module_name>
ls /usr/lib/xorg/modules/extensions/ | grep -i <module_name>
~~~

### xorg display resolution

~~~
xrandr
cvt 1360 768
gft 1360 768 60
xrandr --newmode "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
xrandr --addmode VGA1 "1360x768_60.00"
xrandr --output VGA1 --mode "1360x768_60.00"
cp 10-monitor.conf /usr/share/X11/xorg.conf.d/
~~~

### xorg example 10-monitor.conf

~~~
Section "Monitor"
    Identifier "VGA1"
    Modeline "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
    Option "PreferredMode" "1360x768_60.00"
EndSection

Section "Screen"
    Identifier "Screen0"
    Monitor "VGA1"
    DefaultDepth 24
    SubSection "Display"
        Modes "1360x768_60.00"
    EndSubSection
EndSection

Section "Device"
    Identifier "Device0"
    Driver "intel"
EndSection
~~~

### mount and install GRUB (BIOS)

~~~
sudo mount /dev/sdaX /mnt
sudo arch-chroot /mnt
sudo grub-install --recheck --target=i386-pc /dev/sda
exit
~~~

### mount and install GRUB (UEFI)

~~~
sudo mount /dev/sdaX /mnt
sudo mkdir -p /mnt/boot/efi
sudo mount /dev/sda1 /boot/efi
sudo arch-chroot /mnt
sudo grub-install --recheck --target=x86_64-efi --efi-directory=/boot/efi /dev/sda
sudo grub-install --recheck --target=x86_64-efi --efi-directory=/boot/efi
sudo grub-install --recheck --target=x86_64-efi --bootloader-id=grub_uefi
exit
~~~

### grub default setting

~~~
sudo sed -i 's#GRUB_DEFAULT=0#GRUB_DEFAULT=1#g' /etc/default/grub
sudo sed -i 's#GRUB_TIMEOUT=5#GRUB_TIMEOUT=10#g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
~~~

### check CUPS service

~~~
netstat -apln | grep 127.0.0.1:631
~~~

### shell autologin

~~~
install -d /etc/systemd/system/getty@tty1.service.d/
~~~

~~~
echo -e "
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin live --noclear %I 38400 linux
" > /etc/systemd/system/getty@tty1.service.d/autologin.conf
~~~

### start network on boot

~~~
ip link
systemctl enable dhcpcd@eno1.service
~~~

### resolv internet fix

~~~
sudo rm -vf /etc/resolv.conf
sudo touch /etc/resolv.conf
~~~

### ping root access only fix

~~~
sudo chmod a+x $(which ping)
~~~

### ping multiple targets

~~~
fping -s -g 10.199.6.60 10.199.6.70 -r 1
fping -a -q -g 10.199.6.0/24
~~~

### samba sharing configuration

~~~
echo "
[<shared_folder_name>]
path = /home/<user_name>/<shared_folder_name>
available = yes
valid users = <user_name>
read only = no
browseable = yes
public = yes
writable = yes
" > /etc/samba/smb.conf
~~~

### WORKGROUP sharing samba

~~~
ifconfig eth0 up 192.168.56.5
smbpasswd -a <user_name>
mkdir /home/<user_name>/<shared_folder_name>
service smbd restart
systemctl restart smbd
testparm
~~~

### mount samba directory

~~~
sudo mkdir /mnt/smb/
sudo mount.cifs //10.124.20.205/software/ /mnt/smb/
~~~

### download using aria2c

~~~
aria2c -UChrome/28.0.1500.52 <URL>
~~~

### uget+aria2 arguments

~~~
--enable-rpc=true -D --disable-ipv6 --check-certificate=false -UChrome/28.0.1500.52
--enable-rpc=true -D --disable-ipv6 --check-certificate=false -UChrome/28.0.1500.52 --all-proxy="http://server:port" --all-proxy-user="user@name" --all-proxy-passwd="password"
~~~

### download a website using wget

~~~
wget \
--recursive \
--convert-links \
--adjust-extension \
--page-requisites \
--no-parent \
--no-clobber \
--restrict-file-names=windows \
--domains=website.com \
http://www.website.com/
~~~

### wget using proxy

~~~
echo "
https_proxy = https://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
http_proxy = http://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
ftp_proxy = ftp://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
" > /etc/wgetrc
~~~

### create wireless hotspot

~~~
1. Network Icon -> Edit Connections
2. Add -> Wi-Fi
3. Wi-Fi tab:
	- connection_name: anywifiname
	- SSID_name: anywifiname
	- mode: Client
	- device mac: wlo1 (ma:ca:dd:re:ss)
4. IPv4 Settings tab:
	- method: Shared to other computers
5. Save
~~~

~~~
sudo sed -i 's#mode=infrastructure#mode=ap#g' /etc/NetworkManager/system-connections/anywifiname
~~~

### create wireless access point

~~~
create_ap wlan0 eth0 MyAccessPoint [MyPassPhrase]
create_ap -n wlan0 MyAccessPoint [MyPassPhrase]
create_ap -m bridge wlan0 eth0 MyAccessPoint [MyPassPhrase]
create_ap -m bridge wlan0 br0 MyAccessPoint [MyPassPhrase]
create_ap wlan0 wlan0 MyAccessPoint [MyPassPhrase]
create_ap --driver rtl871xdrv wlan0 eth0 MyAccessPoint [MyPassPhrase]
echo -e "MyAccessPoint" | create_ap wlan0 eth0
echo -e "MyAccessPoint\nMyPassPhrase" | create_ap wlan0 eth0
create_ap --ieee80211n --ht_capab '[HT40+]' wlan0 eth0 MyAccessPoint [MyPassPhrase]
create_ap --isolate-clients wlan0 eth0 MyAccessPoint [MyPassPhrase]
~~~

~~~
sudo systemctl start create_ap
sudo systemctl enable create_ap
~~~

### pair bluetooth via terminal

~~~
bluetoothctl
agent on
default-agent
scan on
pair 00:27:15:08:2D:28
~~~

### start mate-desktop without lightdm

~~~
echo -e "exec mate-session" >> ~/.xinitrc
startx
~~~

~~~
xinit /usr/bin/mate-session
startx /usr/bin/mate-session
~~~

### virtualbox commandline

~~~
VBoxManage setextradata vmname GUI/Seamless on
VBoxManage startvm vmname
VBoxManage controlvm vmname screenshotpng filename.png
~~~

### setup ssh connection

~~~
echo "on server/remote"
sudo sed -i "s#UsePAM yes#UsePAM no#g" /etc/ssh/sshd_config
sudo sed -i "s#PermitEmptyPasswords no#PermitEmptyPasswords yes#g"  /etc/ssh/sshd_config
echo sed -i "s#PasswordAuthentication no#PasswordAuthentication yes#g" /etc/ssh/sshd_config
sudo sed -i "s#ResponseAuthentication yes#ResponseAuthentication no#g" /etc/ssh/sshd_config
sudo achmadi_userman sshuser
sudo passwd sshuser #create password
~~~

~~~
echo "on client/local"
sudo nmcli dev set vboxnet0 managed yes
ssh root@192.168.56.101
ssh sshuser@192.168.56.101 #enter password
~~~

~~~
echo "sshfs root on client/local"
sudo sshfs root@192.168.56.101:/ /mnt
sudo umount /mnt
~~~

~~~
echo "sshfs non-root on client/local"
mkdir sshmnt/
sshfs sshuser@192.168.56.101:/home/sshuser sshmnt/ #enter password
fusermount -u sshmnt/
~~~

### python installation

~~~
sudo pip install package_name
sudo pip install package_file.whl
pip install --user package_name
pip install --user package_file.whl
python -m site
python -c "import site; print(site.getsitepackages())"
~~~

### disassembly kernel

~~~
mkdir vmlinuz
cd vmlinuz/
cp /boot/vmlinuz-linux ./
ln -svf /usr/lib/modules/4.20.13-arch1-1-ARCH/build/scripts/extract-vmlinux ./extract-kernel
./extract-kernel vmlinuz-linux > kernel-linux
objdump -D kernel-linux | less
less /proc/kallsyms
~~~

~~~
mkdir initramfs
cd initramfs/
cp /boot/initramfs-linux.img ./
lsinitcpio initramfs-linux.img | less
lsinitcpio -a initramfs-linux.img
mkdir content
cd content/
lsinitcpio -x ../initramfs-linux.img
sudo arch-chroot ./ /bin/sh
~~~
