#!/bin/bash

BAKCONF=$PWD/pacman_bak.conf
if [ -f "$BAKCONF" ]; then
    echo "Backup file exist"
else
    echo "Backup original file"
    cp /etc/pacman.conf $BAKCONF
fi


echo 'Modifying config file:'
echo "$PWD/pacman.conf"
cp -f $BAKCONF $PWD/pacman.conf

export REPOURL='http://mirror.labkom.id/archlinux'
export PKGCUSTOM='false'

sed -i "s#Architecture = auto#Architecture = x86_64#g" $PWD/pacman.conf

sed -i "s#= Required DatabaseOptional#= Never#g" $PWD/pacman.conf
sed -i "s#= Optional TrustAll#= Never#g" $PWD/pacman.conf
sed -i "s#= Optional#= Never#g" $PWD/pacman.conf

delNum=$(grep -n '\[testing\]' $PWD/pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf

delNum=$(grep -n '\[community-testing\]' $PWD/pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf

delNum=$(grep -n '\[multilib-testing\]' $PWD/pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf

delNum=$(grep -n '\[custom\]' $PWD/pacman.conf | head -n 1 | cut -d: -f1)
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf
sed -i "${delNum}d" $PWD/pacman.conf

sed -i "s@\#\[multilib\]@\[multilib\]@g" $PWD/pacman.conf
sed -i "s@\#Include@Include@g" $PWD/pacman.conf

if [ "$PKGCUSTOM" = "true" ];then
    echo "[custom]" >> $PWD/pacman.conf
    echo "Server = file:///home/custompkgs" >> $PWD/pacman.conf
fi

export URLREPO="$REPOURL/\$repo/os/\$arch"
sed -i "s#Include = /etc/pacman.d/mirrorlist#Server = $URLREPO#g" $PWD/pacman.conf

echo 'Modifying complete'
