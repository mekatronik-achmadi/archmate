# New Packages

## Modify build system script

```sh
sudo cp -f /usr/bin/pacstrap /usr/bin/pacstrap_install
sudo cp -f /usr/bin/pacstrap /usr/bin/pacstrap_pkgurl

sudo sed -i 's#-Sy#-S#g' /usr/bin/pacstrap_install
sudo sed -i 's#-Sy#-Sp#g' /usr/bin/pacstrap_pkgurl
```

## Set some variables

```sh
echo $REPOURL
export ISOVER='mate_012024'
export PKGLIST='pkg-mate-x86_64.txt'
export PKGCUSTOM='true'
```

## Create folder structures

```sh
mkdir -p $ISOVER/;cd $ISOVER/

mkdir -p databases/
mkdir -p packages/{custom,official}/
mkdir -p sources/custom/

mkdir -p tmproot/etc/
mkdir -p tmproot/var/lib/pacman/sync/
mkdir -p tmproot/var/cache/pacman/pkg/
```

## Download Databases

```sh
cd databases/

wget -c $REPOURL/core/os/x86_64/core.db
wget -c $REPOURL/extra/os/x86_64/extra.db
wget -c $REPOURL/multilib/os/x86_64/multilib.db
cd ../
```

## Config pacman.conf

```sh
export URLREPO="$REPOURL/\$repo/os/\$arch"
echo "[options]
HoldPkg           = pacman glibc
Architecture      = x86_64
SigLevel          = Never
LocalFileSigLevel = Never
ParallelDownloads = 5

[core]
Server = $URLREPO

[extra]
Server = $URLREPO

[multilib]
Server = $URLREPO
" | tee pacman.conf

if [ "$PKGCUSTOM" = "true" ];then
    echo "[custom]" | tee -a pacman.conf
    echo "Server = file:///home/custompkgs" | tee -a pacman.conf
fi
```

## Copy Config, Databases, and Packages

```sh
cp -vf pacman.conf tmproot/etc/pacman.conf
rsync -avh databases/ tmproot/var/lib/pacman/sync/
rsync -avh packages/official/ tmproot/var/cache/pacman/pkg/
```

## Copy Custom Packages

```sh
./custompkg.sh
rsync -avh databases/ tmproot/var/lib/pacman/sync/
rsync -avh packages/custom/ tmproot/var/cache/pacman/pkg/
```

## Generate Packages URL

```sh
sudo pacstrap_pkgurl -GM -C tmproot/etc/pacman.conf \
tmproot $(cat $PKGLIST) > pkgurl.txt
```

## Download Packages

```sh
sed -i -e '1d;2d' pkgurl.txt
cd packages/official/
wget -c -i ../../pkgurl.txt
cd ../../
```

## Check Undownloaded Packages

```sh
cp -vf pacman.conf tmproot/etc/pacman.conf
rsync -avh databases/ tmproot/var/lib/pacman/sync/
rsync -avh packages/official/ tmproot/var/cache/pacman/pkg/
if [ "$PKGCUSTOM" = "true" ];then
    rsync -avh packages/custom/ tmproot/var/cache/pacman/pkg/
fi

sudo pacstrap_pkgurl -GM -C tmproot/etc/pacman.conf \
tmproot $(cat $PKGLIST) | grep 'http:\|https:' | tee pkgurl_remained.txt
```

## Clean Temporary files

```sh
rm -vf pacman.conf
rm -vf pkg*.txt
sudo rm -rvf tmproot/
```
