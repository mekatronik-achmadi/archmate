# Free Yugioh Simulator

## Contents
- [EdoPro](#edopro)
- [Omega](#omega)
- [Master-Duel](#master-duel)
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
- https://www.deviantart.com/thong3/art/EDOPRO-HD-BIG-UPDATE-v10-7-ALL-IN-ONE-1011513809
- https://drive.google.com/drive/folders/17KjpvifyiLf-tCB5zpWC7TQu3AqJgK_V

If requires seperate disk for cards resources:

```sh
ln -svf /home/development/Packages/YgoAsset/edopro/pics /opt/edopro/pics
```

### Customizations
- /opt/edopro/textures/bg
- /opt/edopro/textures/bg_deck
- /opt/edopro/textures/bg_menu
- /opt/edopro/textures/cover
- /opt/edopro/textures/cover2

**Note:** the game prioritize PNG images over JPG images, so remove the PNG first

### Decks
- /opt/edopro/deck/*.ydk

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

If requires seperate disk for game resources before downloading on Linux:

```sh
ln -svf "/home/development/Packages/YgoAsset/ygomega/Files" \
"/opt/ygomega/YGO Omega_Data/Files"
```

### Customizations
- Linux:
    + /opt/ygomega/YGO Omega_Data/Files/Playmat
    + /opt/ygomega/YGO Omega_Data/Files/Sleeves
- Android:
    + Android/data/com.DuelistsUnite.YGOOmega/files/Playmat
    + Android/data/com.DuelistsUnite.YGOOmega/files/Sleeves

### Decks
- Linux:
    + /opt/ygomega/YGO Omega_Data/Files/Exports
    + /opt/ygomega/YGO Omega_Data/Files/Imports
- Android:
    + Android/data/com.DuelistsUnite.YGOOmega/files/Exports
    + Android/data/com.DuelistsUnite.YGOOmega/files/Imports

## Master-Duel

Features:
- Unity/3D: Yes
- All Free: No
- Offline: No

Website: https://www.konami.com/yugioh/masterduel/

Install:
- [Steam](https://store.steampowered.com/app/1449850/YuGiOh_Master_Duel/)
- [PlayStore](https://play.google.com/store/apps/details?id=jp.konami.masterduel)

## Meta
- [Master Duel Meta](https://www.masterduelmeta.com/)
- [Game8](https://game8.co/games/Yu-Gi-Oh-Master-Duel/)
- [YgoProDeck](https://ygoprodeck.com/)

## Archetypes

### Anime

DM:
- BlueEyes     : Main, Fusion, Synchro, Xyz
- HarpieLady   : Synchro, Xyz, Link
- TheMagicians : Main, Fusion, Xyz

GX:
- CyberDragon  : Fusion, Xyz, Link

5DS:
- TechGenus    : Synchro, Link

VRAINS:
- CodeFirewall : Link
- Salamangreat : Link

### Non-Anime

Non-Extra:
- Kaiju        : Main
- Labrynth     : Main

Ritual:
- Vendread     : Ritual, Link
- Voiceless    : Ritual

Pendulum:
- Qliphort     : Pendulum, Link

