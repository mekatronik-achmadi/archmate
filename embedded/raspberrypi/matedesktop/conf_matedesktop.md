##### additional packages
- matcha-azul-gtk-theme: https://github.com/mekatronik-achmadi/archmate-pkgbuild/tree/master/theme-azul/

##### additional configurations

~~~
sudo cp -vf /usr/share/applications/onboard.desktop /etc/xdg/autostart/
~~~

~~~
sudo cp -vf rpimate.layout /usr/share/mate-panel/layouts/
gsettings set org.mate.panel default-layout 'rpimate'
mate-panel --reset
~~~

##### audio output

~~~
echo "dtparam=audio=on" >> /boot/config.txt
echo "audio_pwm_mode=2" >> /boot/config.txt
echo "hdmi_drive=1" >> /boot/config.txt
~~~

~~~
echo 'check audio-card for headphone output'
pacmd list-sinks | grep -e 'name:' -e 'index:'

echo 'set output to headphone on Rpi-3 audio card'
pactl set-default-sink alsa_output.platform-bcm2835_audio.stereo-fallback.2
pactl set-sink-volume @DEFAULT_SINK@ 100%
~~~

##### pychoacoustic tool

~~~
sudo pacman -S cython python-setuptools python-wheel python-pip python-distutils-extra
sudo pacman -S sox python-scipy python-pandas python-matplotlib
sudo pacman -S python-pyqt5 python-numpy
~~~

##### bluetooth audio (failed)

~~~
sudo pacman -S blueman bluez bluez-utils
sudo systemctl enable bluetooth

sed -i "s#console=ttyAMA0,115200 ##g" /boot/cmdline.txt
echo "dtparam=krnbt=on" >> /boot/config.txt
echo "enable_uart=0" >> /boot/config.txt

BT_AUDIO='btc_mode=1\nbtc_params8=0x4e20\nbtc_params1=0x7530'
echo -e $BT_AUDIO >> /usr/lib/firmware/updates/brcm/brcmfmac43430-sdio.txt
echo -e $BT_AUDIO >> /usr/lib/firmware/updates/brcm/brcmfmac43455-sdio.txt
~~~
