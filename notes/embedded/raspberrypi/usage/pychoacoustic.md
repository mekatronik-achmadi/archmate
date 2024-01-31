# Pychoacoustic

## additional configurations

```sh
echo "dtparam=audio=on" >> /boot/config.txt
echo "audio_pwm_mode=2" >> /boot/config.txt
echo "hdmi_drive=1" >> /boot/config.txt
```

```sh
echo 'check audio-card for headphone output'
pacmd list-sinks | grep -e 'name:' -e 'index:'

echo 'set output to headphone on Rpi-3 audio card'
pactl set-default-sink alsa_output.platform-bcm2835_audio.stereo-fallback.2
pactl set-sink-volume @DEFAULT_SINK@ 100%
```

## pychoacoustic tool

```sh
sudo cp -vf /usr/share/applications/onboard.desktop /etc/xdg/autostart/
```
