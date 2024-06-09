# Free Yugioh Simulator

## Contents
- [EdoPro](#edopro)
- [Omega](#omega)
- [Master-Duel](#master-duel)
- [Archetypes](#archetypes)
- [Meta](#meta)

## EdoPro

### Features
- Unity/3D: No
- All Free: Yes
- Offline: Yes

### Links
- Website: https://projectignis.github.io/
- Project: https://github.com/ProjectIgnis
- Discord: https://discord.com/invite/ygopro-percy

### Install
- [Download](https://projectignis.github.io/download.html)
- [Github](https://github.com/ProjectIgnis/edopro-assets/releases)
- ArchLinux:
    + [AUR](https://aur.archlinux.org/packages/edopro-bin)
    + [Custom](https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/yugioh/edopro/)

### Resources

Paths:
- ArchLinux: /opt/edopro/
- Android: Android/data/io.github.edo9300.edopro/files/

**NOTE:**
- For Android, set game path in Internal storage without copying assets
- If repositories clone failed, delete files in repositories folder to re-clone

All Card Pics:
- High Definition:
    + [DeviantArt](https://www.deviantart.com/thong3/art/EDOPRO-HD-BIG-UPDATE-v10-7-ALL-IN-ONE-1011513809)
    + [G-Drive](https://drive.google.com/drive/folders/17KjpvifyiLf-tCB5zpWC7TQu3AqJgK_V)
- Standard:
    + [G-Drive](https://drive.google.com/file/d/1UdA2UKRk2CjKYwDaWHwJmQj0mjngDjP1)

If requires seperate disk for card pics resources (ArchLinux):

```sh
ln -svf /home/development/Packages/YgoAsset/edopro/pics /opt/edopro/pics
```

### Customizations

Customable Files:
- textures/bg.png
- textures/bg_deck.png
- textures/bg_menu.png
- textures/cover.png
- textures/cover2.png

### Decks
- deck/*.ydk

## Omega

### Features
- Unity/3D: Yes
- All Free: Yes
- Offline: Yes

### Links
- Website: https://omega.duelistsunite.org/
- Project: https://github.com/duelists-unite
- Discord: https://discord.com/invite/duelistsunite

### Install
- [Download](https://omega.duelistsunite.org/)
- [Github](https://github.com/duelists-unite/omega-releases/releases/)
- ArchLinux:
    + [Custom](https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/unused/yugioh/ygomega/)

### Resources

Paths:
- ArchLinux: /opt/ygomega/
- Android: Android/data/com.DuelistsUnite.YGOOmega/files

If requires seperate disk for game resources before downloading on ArchLinux:

```sh
ln -svf "/home/development/Packages/YgoAsset/ygomega/Files" \
"/opt/ygomega/YGO Omega_Data/Files"
```

### Customizations

Customable Files:
- Playmat/*.jpg
- Sleeves/*.jpg

### Decks

Exports:
    + Exports/*.zip
    + Exports/*.ydk
    * Exports/*.csv

Imports:
    + Imports/*.ydk
    + Imports/*.csv

## Master-Duel

Features:
- Unity/3D: Yes
- All Free: No
- Offline: No

Website: https://www.konami.com/yugioh/masterduel/

Install:
- [Steam](https://store.steampowered.com/app/1449850/YuGiOh_Master_Duel/)
- [PlayStore](https://play.google.com/store/apps/details?id=jp.konami.masterduel)

## Archetypes

### Anime

DM:
- BlueEyes     : Main, Fusion, Synchro, Xyz
- Harpies      : Synchro, Xyz, Link
- TheMagicians : Main, Fusion, Xyz

GX:
- CyberDragon  : Fusion, Xyz, Link

5DS:
- TechGenus    : Synchro, Link

VRAINS:
- CodeFirewall : Link
- Salamangreat : Link
- Marincess    : Link

### Non-Anime

Ritual:
- Vendread     : Ritual, Link
- Voiceless    : Ritual

Extra:
- Danger       : Main, Xyz, Link

Non-Extra:
- Kaiju        : Main
- Labrynth     : Main

Other:
- Qli          : Pendulum, Link
- Paleozoic    : Trap, Xyz, Link
- Female       : Catalog

## Meta
- [Master Duel Meta](https://www.masterduelmeta.com/)
- [Game8](https://game8.co/games/Yu-Gi-Oh-Master-Duel/)
- [YgoProDeck](https://ygoprodeck.com/)
- [Female](https://www.deviantart.com/primesui/journal/Tier-List-Yu-Gi-Oh-Female-Archetypes-815726528)

