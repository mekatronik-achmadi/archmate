#!/bin/bash

if [ $UID == 0 ];then
	echo -e "This script must not run as root"
	exit
fi

######################### modify build system script #########################

#cp -f /usr/bin/pacstrap /usr/bin/pacstrap_install
#cp -f /usr/bin/pacstrap /usr/bin/pacstrap_pkgurl
#sed -i 's#-Sy#-S#g' /usr/bin/pacstrap_install
#sed -i 's#-Sy#-Sp#g' /usr/bin/pacstrap_pkgurl

######## Set some variables ########

export REPOURL='http://mirror.labkom.id/archlinux'
export PKGLIST='pkg-mate-x86_64.txt'
export PKGCUSTOM='true'

######## Create temporary root ########

mkdir -p tmproot/etc/
mkdir -p tmproot/var/lib/pacman/sync/

mkdir -p databases/
echo "cleanup databases"
rm databases/*
cd databases/
wget -c $REPOURL/core/os/x86_64/core.db
wget -c $REPOURL/core/os/x86_64/core.files
wget -c $REPOURL/extra/os/x86_64/extra.db
wget -c $REPOURL/extra/os/x86_64/extra.files
wget -c $REPOURL/community/os/x86_64/community.db
wget -c $REPOURL/community/os/x86_64/community.files
wget -c $REPOURL/multilib/os/x86_64/multilib.db
wget -c $REPOURL/multilib/os/x86_64/multilib.files
cd ../

######## Config pacman.conf ########

cp -vf /usr/share/archiso/configs/releng/pacman.conf ./

sed -i "s#Architecture = auto#Architecture = x86_64#g" pacman.conf

sed -i "s#= Required DatabaseOptional#= Never#g" pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" pacman.conf
sed -i "s#= Optional#= Never#g" pacman.conf

delNum=$(grep -n '\[testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[community-testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[multilib-testing\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

delNum=$(grep -n '\[custom\]' pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf
sed -i "${delNum}d" pacman.conf

sed -i "s@\#\[multilib\]@\[multilib\]@g" pacman.conf
sed -i "s@\#Include@Include@g" pacman.conf

if [ "$PKGCUSTOM" = "true" ];then
    echo "[custom]" >> pacman.conf
    echo "Server = file:///home/custompkgs" >> pacman.conf
fi

export URLREPO="$REPOURL/\$repo/os/\$arch"
sed -i "s#Include = /etc/pacman.d/mirrorlist#Server = $URLREPO#g" pacman.conf

######## Prepare Custom Repository ########

if [ "$PKGCUSTOM" = "true" ];then
    mkdir -p packages/custom/
    cd packages/custom/
    #repo-add custom.db.tar.gz *.pkg.tar.xz
    repo-add custom.db.tar.gz *.pkg.tar.zst
    rm -f *.tar.gz.old

    cp -vf custom.db.tar.gz ../../databases/custom.db
    cp -vf custom.files.tar.gz ../../databases/custom.files
    rm -f custom.db*
    rm -f custom.files*
    cd ../../

    mkdir -p tmproot/var/cache/pacman/pkg/
    rsync -avh packages/custom/ tmproot/var/cache/pacman/pkg/
fi

######## Copy Config and Databases ########

mkdir -p tmproot/var/cache/pacman/pkg/
cp -vf pacman.conf tmproot/etc/pacman.conf
rsync -avh databases/ tmproot/var/lib/pacman/sync/

######## Generate Packages URL ########

sudo pacstrap_pkgurl -GM -C tmproot/etc/pacman.conf \
tmproot $(cat $PKGLIST) > pkgurl.txt

######## Download Packages ########

sed -i -e '1d;2d' pkgurl.txt
mkdir -p packages/official/
echo "cleanup packages"
rm packages/official/*
cd packages/official/
wget -c -i ../../pkgurl.txt
cd ../../

######## Clean Temporary files ########

rm -vf pacman.conf
#rm -vf pkgurl.txt

sudo rm -rvf tmproot/
