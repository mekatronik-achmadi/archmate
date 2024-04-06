# Media Packages

## Official

### install document tools

mupdf-gl mupdf-tools djview

### install graphic tools

gimp xsane-gimp
inkscape sassc
imagemagick

### install multimedia tools

audacity sox faac
openshot frei0r-plugins

### install gaming client

steam vkd3d lib32-vkd3d
steam-native-runtime

### install disk recovery tools

ddrescue ext4magic foremost testdisk

--------------------------------------------------------------------------------

## AUR

### install markdown tools

- https://aur.archlinux.org/packages/pandoc-bin/

### install disk recovery tools

- https://aur.archlinux.org/packages/extundelete/

### install screencast tools

- https://aur.archlinux.org/packages/simplescreenrecorder/
- https://aur.archlinux.org/packages/key-mon/

### install youtube downloader

- https://aur.archlinux.org/packages/yt-dlp-git/

--------------------------------------------------------------------------------

## External

### install youtube programs

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/youtube/

### install markdown tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/ghostwriter-qt5/

--------------------------------------------------------------------------------

## Configurations

### configure mupdf

```sh
sudo sed -i 's#NoDisplay=true##g' /usr/share/applications/mupdf.desktop
```

### configure steam

```sh
echo "Steam -> Settings -> Steam Play"
echo "Enable Steam Play for all"

echo "Choose Game -> Manage -> Properties"
echo "Compatibility -> Force use Steam Play"

echo "use Proton 4.11"
```

### configure audacity

```sh
echo "re-enabled headphone"
alsactl init
```

```sh
echo "
change 'sysdefault: Headphone Mic:0'
to 'sysdefault: Internal Mic:0'
"
```

### configure key-mon

```sh
key-mon --reset &
key-mon -s -m --decorated -t classic &
```

### configure youtube-dl

Format recommendations:
- vid code -> https | avc1.4D401F 803k video only 720p
- aud code -> https │ audio only opus 48k

```sh
yt-dlp -F https://www.youtube.com/watch?v=xxxxxxxxxxx
yt-dlp -f <vid>+<aud> --merge-output-format mp4 https://www.youtube.com/watch?v=xxxxxxxxxxx
yt-dlp -f 136+251 --merge-output-format mp4 https://www.youtube.com/watch?v=xxxxxxxxxxx

yt-dlp -f 251 https://www.youtube.com/watch?v=xxxxxxxxxxx
ffmpeg -i videoname.webm -vn -ab 128k -ar 44100 -y videoname.mp3
rm -vf videoname.webm
```
