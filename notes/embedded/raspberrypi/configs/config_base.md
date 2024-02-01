# RaspberryPi Basic Configurations

## Additional Configuration

### login ssh

```sh
rm -r ~/.ssh/

# ssh with X11 forwarding
ssh -X alarm@10.124.4.150

hwclock --show --verbose;date
sudo date -s "9 JUL 2021 07:00:00"

python /home/alarm/tkfree.py

exit
```

### wifi connection

```sh
sudo nmcli radio wifi on

sudo nmcli dev wifi
sudo iwlist wlan0 scan | grep SSID

sudo nmcli --ask dev wifi connect CobaMQTT
sudo nmcli dev wifi connect CobaMQTT password "cobamqtt"

sudo nmcli con
sudo nmcli con show CobaMQTT
sudo nmcli con delete CobaMQTT
```

```sh
# alternative front-end
sudo nmtui
```

### run gui programs

```sh
echo "startx /usr/bin/python /home/alarm/tkfree.py" >> ~/.bashrc
```

```sh
echo '
if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    echo "SSH Login Success"
else
    startx /usr/bin/python /home/alarm/tkfree.py &> /dev/null
    #startx /usr/bin/python /home/alarm/tkfree.py -- -logverbose 6 &> ~/xorg.log
fi
' >> /home/alarm/.bashrc
```

## VNC

### server settings

#### remote virtual monitor without physical display

```sh
vncpasswd

mkdir -p ~/.vnc/
echo 'session=openbox
geometry=1024x768
alwaysshared
' | tee ~/.vnc/config
echo ':1=alarm' | sudo tee /etc/tigervnc/vncserver.users

sudo systemctl enable vncserver@:1
sudo systemctl start vncserver@:1
```

#### remote virtual monitor on direct display (non-root)

```sh
vncpasswd

x0vncserver -rfbauth ~/.vnc/passwd
#x0vncserver -geometry 1280x1024+0+0 -rfbauth ~/.vnc/passwd
```

#### remote virtual monitor on direct display (root)

```sh
vncpasswd

echo "[Unit]
Description=Remote desktop service (VNC) for :0 display
Requires=display-manager.service
After=network-online.target
After=display-manager.service

[Service]
Type=simple
Environment=HOME=/root
Environment=XAUTHORITY=/var/run/lightdm/root/:0
ExecStart=x0vncserver -display :0 -rfbauth /home/alarm/.vnc/passwd
Restart=on-failure
RestartSec=500ms

[Install]
WantedBy=multi-user.target
" | sudo tee /etc/systemd/system/x0vncserver.service

sudo systemctl enable x0vncserver
sudo systemctl start x0vncserver
```

### client access

```sh
# Port 5900 -> :0
# Port 5901 -> :1
# Menu/Fullscreen -> F8

vncviewer <ip_number>:<display_number>

vncviewer 10.124.2.141:0
vncviewer 10.124.2.141:1
```

