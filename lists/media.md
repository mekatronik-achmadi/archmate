# Media Packages

## Official

### install graphic tools

gimp xsane-gimp
imagemagick
inkscape

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

--------------------------------------------------------------------------------

## External

### install youtube programs

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/youtube/

### install markdown tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/ghostwriter-qt5/

--------------------------------------------------------------------------------

## Configurations

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

