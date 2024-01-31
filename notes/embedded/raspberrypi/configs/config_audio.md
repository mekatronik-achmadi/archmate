# Audio Configurations

## Audio Output

### Enable Audio

```sh
# if using audio jack 3.5mm
echo "audio_pwm_mode=2" | sudo tee -a /boot/config.txt
echo "hdmi_drive=1" | sudo tee -a /boot/config.txt

# if using audio over HDMI
#echo "hdmi_drive=2" | sudo tee -a /boot/config.txt

# enable audio i2s feature
echo "dtparam=i2s=on" | sudo tee -a /boot/config.txt
```

```sh
# speaker test
speaker-test -t wav -c 6
```

### Bluetooth Audio

- https://aur.archlinux.org/packages/bluez-utils-compat/
- https://aur.archlinux.org/packages/pi-bluetooth/

```sh
sudo systemctl enable bluetooth
sudo sed -i "s#console=ttyAMA0,115200 ##g" /boot/cmdline.txt
echo "dtparam=krnbt=on" | sudo tee -a /boot/config.txt
echo "enable_uart=0" | sudo tee -a /boot/config.txt

sudo sed -i '/disable-bt/d' /boot/config.txt

# Bluetooth modules for Pi-3
sudo systemctl enable brcm43438
export BT_AUDIO='btc_mode=1\nbtc_params8=0x4e20\nbtc_params1=0x7530'
echo -e $BT_AUDIO | sudo tee -a /usr/lib/firmware/updates/brcm/brcmfmac43430-sdio.txt
echo -e $BT_AUDIO | sudo tee -a /usr/lib/firmware/updates/brcm/brcmfmac43455-sdio.txt

sudo reboot
```

```sh
# disable wifi to improve bluetooth
# in actual running RPi
sudo nmcli radio wifi off
sudo reboot
```

```sh
# bluetoothctl interactive
# in actual running RPi
bluetoothctl
> power on
> agent on
> scan on

# make sure headphone in pairing mode
# select non-LE name
#journalctl --unit=bluetooth -f
#pulseaudio -k;pulseaudio --start
> pair 04:52:C7:5E:BA:B5
> connect 04:52:C7:5E:BA:B5
> trust 04:52:C7:5E:BA:B5

# remove a paired devices
> paired-devices
> remove 04:52:C7:5E:BA:B5

# quit from shell
> quit
```

## Audio Input

### I2S Microphone

- https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test
- https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/tree/main/i2s_mic_module/

#### Install I2S Mic Driver

- https://aur.archlinux.org/packages/python-pyalsaaudio/
- https://github.com/mekatronik-achmadi/archlinuxmate/tree/main/notes/raspberry/drivers/i2smems/

```sh
# list audio capture
arecord -l

# record mono to a file
arecord -D plughw:1 -c2 -r 48000 -f S16_LE -t wav -V mono -v record.wav

# replay the record
aplay record.wav
```

#### Boost I2S Mic ALSA

```sh
echo "
pcm.dmic_hw {
    type hw
    card sndrpii2scard
    channels 2
    format S16_LE
}
pcm.dmic_sv {
    type softvol
    slave.pcm dmic_hw
    control {
        name I2SMic
        card sndrpii2scard
    }
    min_dB -3.0
    max_dB 30.0
}
" > $HOME/.asoundrc

# need to run once for just in short time
arecord -D dmic_sv -c2 -r 44100 -f S16_LE -t wav -V mono -v record.wav

# adjust using ALSA-Mixer
# find device: 'arecord -L'
sudo rm -f /var/lib/alsa/asound.state
amixer -D sysdefault:CARD=sndrpii2scard set I2SMic 100%
sudo alsactl store

# run again to confirm its working
arecord -D dmic_sv -c2 -r 44100 -f S16_LE -t wav -V mono -v record.wav
```

```sh
# record test
arecord -D dmic_sv -c2 -r 44100 -f S16_LE -t wav -V mono -v record.wav

# check what used device
fuser -fv /dev/snd/* /dev/dsp*

# playback PCM raw record
aplay -r 44100 -f S16_LE -c 2 out.raw
```
