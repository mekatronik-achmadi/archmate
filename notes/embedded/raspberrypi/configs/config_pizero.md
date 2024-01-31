# PiZero Configurations

## USB Connections

### PiZero Ethernet Gadget

```sh
# "PiZero as USB-Device not USB-Host"

echo "dtoverlay=dwc2" >> /boot/config.txt
sed -i "s#rootwait console#rootwait modules-load=dwc2,g_ether console#g" /boot/cmdline.txt

echo "
Description='pizero g_ether gadget'
Interface=usb0
Connection=ethernet
IP=static
SkipNoCarrier=yes
Address=('192.168.7.3/24')
Gateway='192.168.7.150'
DNS=('8.8.8.8')" > /etc/netctl/usbpizero
netctl enable usbpizero
```

```sh
# run this from other computer/USB-Host
# pizero usb g_ether must connected
export CONNAME="Wired connection 2"
sudo nmcli con | grep "$CONNAME"
sudo nmcli con mod "$CONNAME" ipv4.addresses 192.168.7.150/24
sudo nmcli con mod "$CONNAME" ipv4.gateway 192.168.7.150
sudo nmcli con mod "$CONNAME" ipv4.dns "8.8.8.8"
sudo nmcli con mod "$CONNAME" ipv4.method manual
sudo nmcli con up "$CONNAME"

ssh -Y alarm@192.168.7.3

mkdir -p sshfs/
sshfs alarm@192.168.7.3:/home/alarm/ ./sshfs/
```
