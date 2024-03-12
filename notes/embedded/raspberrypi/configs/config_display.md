# RaspberryPi Display Configurations

## HDMI Configurations

### HDMI LCD 1024x600 Waveshare

```sh
echo "
max_usb_current=1
hdmi_drive=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0" >> /boot/config.txt
```

## SPI/DSI Configurations

### Waveshare 3.5 LCD

- https://github.com/waveshare/LCD-show/
- https://whitedome.com.au/download/Overlays/
- https://github.com/swkim01/waveshare-dtoverlays/

```sh
# in actual running rpi unit
wget -c https://raw.githubusercontent.com/swkim01/waveshare-dtoverlays/master/waveshare35a.dts
dtc -@ -Hepapr -I dts -O dtb -o waveshare35a.dtbo waveshare35a.dts
```

```sh
cp -f /home/alarm/waveshare35a.dtbo /boot/overlays/

echo "
dtparam=spi=on
dtoverlay=waveshare35a:rotate=180,swapxy=1" >> /boot/config.txt

# for LCD Waveshare 35 (C) High-Speed SPI
echo "
dtparam=spi=on
dtoverlay=waveshare35a:rotate=0,swapxy=1,speed=80000000" >> /boot/config.txt

# ' fbcon=map:10' confusing
sed -i '$s/$/ fbcon=font:ProFont6x11/' /boot/cmdline.txt

# redirect xorg framebuffer output
# dont use this for Pi-4 without any HDMI out
#sed -i "s#/dev/fb0#/dev/fb1#g" /etc/X11/xorg.conf.d/99-fbdev.conf
```

### Waveshare 3.5 Touchscreen

```sh
#startx /usr/bin/xinput_calibrator | tee calib.log
#bat calib.log

# invert Y
echo 'Section "InputClass"
    Identifier          "libinput touchscreen"
    MatchIsTouchScreen  "on"
    MatchDevicePath     "/dev/input/event*"
    Driver              "libinput"
    Option "TransformationMatrix" "1 0 0 0 -1 1 0 0 1"
EndSection' > /etc/X11/xorg.conf.d/99-calibration.conf
```
