# General Notes

## MATE Desktop Guidelines

### Avoided Toolkit/Libraries

- Libadwaita
- Pipewire
- Wayland
- GNOME-4
- WxGTK-2
- GTK-4
- Qt-4
- KDE
- LXQt
- Xfce
- Snap
- Conda
- PyTest
- Flatpak
- Linting
- Python-2
- Mono/NET
- Nativefier

### Usage of GNOME-3

- for infrastructures (e.g gvfs, glib2, etc)
- for artworks (e.g gnome-themes-extra, etc)
- for tools (e.g dconf, glade, brasero, etc)

### Usage of Microsoft

- Visual Studio Code

---------------------------------------------------------------------------------------------------

## Bash general

### bash execute command string

```sh
bash -c "command_string"
bash -c "command_string1 && command_string2"
bash -c "echo -e \"string \\\"quoted_string\\\";\" >> /filepath"
```

### get basic home files

```sh
rsync -a /etc/skel/ $HOME/
```

### custom prompt

```sh
PS1='\n\[\033(0\]l\[\033(B\][$(pwd)]\n\[\033(0\]m\[\033(B\]\[\033(0\]q\[\033(B\](\u@\h):\$ '
sudo nano /etc/skel/.bashrc
cp -vf /etc/skel/.bashrc ~/
```

### show password feedback for sudo

```sh
echo -e "Defaults pwfeedback" >> /etc/sudoers
```

### get user homedir path

```sh
read username
homedir=$( getent passwd $username | cut -d: -f6 )
echo -e $homedir
```

### environment variables

```sh
set
printenv
printenv HOME
echo -e $HOME
source input_file
export VARIABLE="value"
env VARIABLE="value" <command>
cat /etc/profile
ls /etc/profile.d/
```

### cat file content line by line

```sh
IFS=$'\n'
for i in `cat file`;do echo $i;done > result.txt
for i in $(cat file);do echo $i;done > result.txt
for i in (<file);do echo $i;done > result.txt
```

### fix time stamp problems

```sh
touch <file_name>
```

### tmux commands

```sh
#Session => Window => Pane
```

```text
Crtl+B %    [split pane vertically]
Crtl+B "    [split pane horizontally]
Crtl+B <Arrow>    [select active pane]
Crtl+B z    [toggle pane fullscreen]
Crtl+B c    [new window]
Crtl+B <Number>    [select active window]
exit        [exit tmux or window or pane]
```

```sh
tmux split-window -v -c $PWD
tmux split-window -h -c $PWD
```

---------------------------------------------------------------------------------------------------

## Serial Port Shell

### create virtual serial communication

**NOTE:** make sure the /dev/pts/ number is correct

```sh
socat -d -d pty,raw,echo=0 pty,raw,echo=0
sudo ln -sf /dev/pts/2 /dev/ttyV0
sudo ln -sf /dev/pts/3 /dev/ttyV1
picocom -b 9600 /dev/ttyV0
picocom -b 9600 /dev/ttyV1
```

### intercep serial port

```sh
sudo interceptty -s 'ispeed 38400 ospeed 38400' /dev/ttyACM0 /dev/coba
```

---------------------------------------------------------------------------------------------------

## Xorg configurations

### xorg module checking

```sh
cat /var/log/Xorg.0.log | grep -i <module_name>
ls /usr/lib/xorg/modules/extensions/ | grep -i <module_name>
```

### xorg manually settings

```sh
xrandr
cvt 1360 768
gft 1360 768 60
xrandr --newmode "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
xrandr --addmode VGA1 "1360x768_60.00"
xrandr --output VGA1 --mode "1360x768_60.00"
```

```sh
echo 'Section "Monitor"
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
EndSection' | sudo tee /usr/share/X11/xorg.conf.d/10-monitor.conf
```

### gpu utilization script

```sh
#!/bin/bash

echo -n "GPU: "
nvidia-smi -q -d UTILIZATION | grep Gpu | cut -d: -f2

echo -n "MEM: "
nvidia-smi -q -d MEMORY | grep Used | head -n1 | cut -d: -f2
```

---------------------------------------------------------------------------------------------------

## Network Configurations

### ping root access only fix

```sh
sudo chmod a+x $(which ping)
```

### ping multiple targets

```sh
fping -s -g 10.199.6.60 10.199.6.70 -r 1
fping -a -q -g 10.199.6.0/24
```

### bypass blockade using dns

```sh
echo 'nameserver 8.8.8.8' | sudo tee /etc/resolv.conf

# to restore
#sudo systemctl restart NetworkManager
```

```
Advance Network Configuration -> (Connection Name) -> Edit Connection
IPv4 Settings -> DNS Servers -> 8.8.8.8 -> Save
```

### samba sharing configuration

#### config files

```sh
sudo pacman -S samba smbclient

echo "
[global]
    admin users = $USER
    workgroup = WORKGROUP
    server string = %h server (Samba, Arch)
    unix charset = UTF-8
    server min protocol = NT1
    ntlm auth = yes
    client min protocol = NT1
    client max protocol = SMB3
    case sensitive = no
    bind interfaces only = yes

[Public]
    path = $HOME/Public
    available = yes
    valid users = $USER
    read only = no
    browseable = yes
    public = yes
    writable = yes

[shared_folder_name]
    path = $HOME/shared_folder_name
    available = yes
    valid users = $USER
    read only = no
    browseable = yes
    public = yes
    writable = yes
" | sudo tee /etc/samba/smb.conf

sudo smbpasswd -a $USER

sudo systemctl enable smb nmb
sudo systemctl start smb nmb

testparm
```

#### mount samba directory

```sh
sudo mkdir /mnt/smb/
sudo mount.cifs //10.124.20.205/software/ /mnt/smb/
```

### downloader programs

#### aria2c with user agent

```sh
aria2c -UChrome/28.0.1500.52 <URL>
```

#### uget+aria2 arguments

```sh
--enable-rpc=true -D --disable-ipv6 --check-certificate=false -UChrome/28.0.1500.52
--enable-rpc=true -D --disable-ipv6 --check-certificate=false -UChrome/28.0.1500.52 --all-proxy="http://server:port" --all-proxy-user="user@name" --all-proxy-passwd="password"
```

#### download a website using wget

```sh
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
```

#### wget using proxy

```sh
echo "
https_proxy = https://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
http_proxy = http://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
ftp_proxy = ftp://achmadi10%40mhs.ep.its.ac.id:yourpassword@proxy.its.ac.id:8080
" > /etc/wgetrc
```

### wireless hotspot

#### create wireless hotspot

```text
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
```

```sh
sudo sed -i 's#mode=infrastructure#mode=ap#g' /etc/NetworkManager/system-connections/anywifiname
```

#### create wireless access point

```sh
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
```

```sh
sudo systemctl start create_ap
sudo systemctl enable create_ap
```

### bluetooth

#### cli pairing

```sh
bluetoothctl
agent on
default-agent
scan on
pair 00:27:15:08:2D:28
```

```sh
echo "on client/local"
sudo nmcli dev set vboxnet0 managed yes
ssh root@192.168.56.101
ssh sshuser@192.168.56.101 #enter password
```

```sh
echo "sshfs root on client/local"
sudo sshfs root@192.168.56.101:/ /mnt
sudo umount /mnt
```

```sh
echo "sshfs non-root on client/local"
mkdir sshmnt/
sshfs sshuser@192.168.56.101:/home/sshuser sshmnt/ #enter password
fusermount -u sshmnt/
```

---------------------------------------------------------------------------------------------------

## Python

### python virtualenv

#### install virtualenv

```sh
sudo pacman -S python-pipenv python-virtualenv
```

#### create virtualenv

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv infrapyenv --system-site-packages
source $HOME/PyEnv/infrapyenv/bin/activate
```

#### install additional

```sh
pip install pisces pathos cx_Oracle tsfresh obspy PyWavelets bokeh xyzservices
```

#### deactivate

```sh
deactivate
```

### jupyter notebook

#### install kernel specs

```sh
source $HOME/PyEnv/infrapyenv/bin/activate
ipython kernel install --user --name=infrapyenv
```

#### run inside environment

```sh
jupyter-notebook --no-browser
```

---------------------------------------------------------------------------------------------------

## Android Tools

### adb

#### basic setup

```txt
Settings -> Developer options
```

```sh
adb devices
adb shell
```

#### using Wifi

```sh
echo "connect on USB First"
adb tcpip 5555

echo "ping device wlan ip"
ping <device_ip_address>

echo "switch to wifi"
adb connect <device_ip_address>:5555

echo "disconnect USB and check"
adb devices

echo "back to usb"
adb kill-server
adb usb
```

#### restart

```sh
adb kill-server
adb start-server

adb connect <device_ip_address>:5555
adb devices
```

### scrcpy

```sh
echo "via USB"
scrcpy -w -S --disable-screensaver --no-audio

echo "via WiFi"
scrcpy -w -S -b2M -m800 --disable-screensaver --no-audio

echo "device/port selection"
scrcpy -w -S --disable-screensaver --no-audio [-d/-e] <device>
scrcpy -w -S --disable-screensaver --no-audio --tcpip[=ip[:port]]
```

--------------------------------------------------------------------------------------------------

## Qtcreator

```sh
echo "Help->About Plugins->C++"
echo "check: ClangCodeModel"

echo "Edit->Preferences->Text Editor->Font & Colors"
echo "Family: LiterationMono Nerd Font"
echo "Size: 8"

echo "Edit->Preferences->C++->Code Model"
echo "check: Interpret ambiguous headers as C headers"
echo "check: Ignore precompiled headers"

echo "Edit->Preferences->C++->Clangd"
echo "uncheck: Use clangd"

echo "Edit->Preferences->Analyzer"
echo "uncheck: Analyze open files"

echo "Edit->Preferences->FakeVim"
echo "uncheck: Use FakeVim"
```

## Arduino

### setup

```sh
cd $HOME
mkdir -p ~/.local/arduino-cli/bin/

cd ~/.local/arduino-cli/
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | bash

export PATH=$PATH:~/.local/arduino-cli/bin
arduino-cli version
```

### example

```sh
export PATH=$PATH:~/.local/arduino-cli/bin

arduino-cli config init

arduino-cli sketch new LED
cd LED/

arduino-cli core update-index
arduino-cli core search nano
arduino-cli core install arduino:avr
arduino-cli core list

arduino-cli lib search DHT11 | grep DHT11
arduino-cli lib install "DHT11"

# generate compilation database
# in Vim -> :set ft=cpp
arduino-cli compile \
--build-path ./build \
--only-compilation-database \
--fqbn arduino:avr:nano

arduino-cli compile \
--build-path ./build \
--export-binaries \
--fqbn arduino:avr:nano

arduino-cli board list
arduino-cli upload --fqbn arduino:avr:nano --port /dev/ttyUSB0
```

### vscode

```sh
code --list-extensions

code --force --install-extension cschlosser.doxdocgen
code --force --install-extension vsciot-vscode.vscode-arduino
code --force --install-extension ms-vscode.vscode-serial-monitor
code --force --install-extension llvm-vs-code-extensions.vscode-clangd
```

Optional settings to:
- Windows: **%APPDATA%\Roaming\VSCodium\User\settings.json**
- Linux: **~/.config/Code/User/settings.json**

```json
"arduino.path": "~/.local/arduino-cli/bin",
"arduino.commandPath": "arduino-cli",
"arduino.useArduinoCli": true,
"arduino.enableUSBDetection": true,
"arduino.logLevel": "verbose",
```
