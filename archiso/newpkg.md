#### Set some variables

#### modify build system script

~~~
sudo cp -f /usr/bin/pacstrap /usr/bin/pacstrap_install
sudo cp -f /usr/bin/pacstrap /usr/bin/pacstrap_pkgurl

sudo sed -i 's#-Sy#-S#g' /usr/bin/pacstrap_install
sudo sed -i 's#-Sy#-Sp#g' /usr/bin/pacstrap_pkgurl
~~~

~~~
export REPOURL='http://mirror.labkom.id/archlinux'
export PKGLIST='pkg-cli-x86_64.txt'
export PKGCUSTOM='true'
~~~

#### Create temporary root

~~~
mkdir -p tmproot/etc/
mkdir -p tmproot/var/lib/pacman/sync/
~~~

#### Download Databases

~~~
mkdir -p databases/
echo "cleanup databases"
rm databases/*
cd databases/
~~~

~~~
wget -c $REPOURL/core/os/x86_64/core.db
wget -c $REPOURL/core/os/x86_64/core.files
wget -c $REPOURL/extra/os/x86_64/extra.db
wget -c $REPOURL/extra/os/x86_64/extra.files
wget -c $REPOURL/community/os/x86_64/community.db
wget -c $REPOURL/community/os/x86_64/community.files
wget -c $REPOURL/multilib/os/x86_64/multilib.db
wget -c $REPOURL/multilib/os/x86_64/multilib.files
cd ../
~~~

~~~
echo "using curl instead wget"

curl -L -O -C - $REPOURL/core/os/x86_64/core.db
curl -L -O -C - $REPOURL/core/os/x86_64/core.files
curl -L -O -C - $REPOURL/extra/os/x86_64/extra.db
curl -L -O -C - $REPOURL/extra/os/x86_64/extra.files
curl -L -O -C - $REPOURL/community/os/x86_64/community.db
curl -L -O -C - $REPOURL/community/os/x86_64/community.files
curl -L -O -C - $REPOURL/multilib/os/x86_64/multilib.db
curl -L -O -C - $REPOURL/multilib/os/x86_64/multilib.files
cd ../
~~~

#### Config pacman.conf

~~~
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
~~~

#### Prepare Custom Repository

~~~
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
~~~

#### Copy Config and Databases

~~~
mkdir -p tmproot/var/cache/pacman/pkg/
cp -vf pacman.conf tmproot/etc/pacman.conf
rsync -avh databases/ tmproot/var/lib/pacman/sync/
~~~

#### Generate Packages URL

~~~
sudo pacstrap_pkgurl -GM -C tmproot/etc/pacman.conf \
tmproot $(cat $PKGLIST) > pkgurl.txt
~~~

#### Download Packages

~~~
sed -i -e '1d;2d' pkgurl.txt
mkdir -p packages/official
echo "cleanup packages"
rm packages/official/*
cd packages/official/
~~~

~~~
wget -c -i ../../pkgurl.txt
cd ../../
~~~

~~~
echo "using curl instead wget"

xargs -n 1 curl -L -O -C - < ../../pkgurl.txt
cd ../../
~~~

#### Clean Temporary files

~~~
rm -vf pacman.conf
#rm -vf pkgurl.txt

sudo rm -rvf tmproot/
~~~

#### new package script

~~~
./newpkg_cli.sh
./newpkg_cli.sh 2>&1 | tee newpkg_log.txt
~~~

~~~
./newpkg_mate.sh
./newpkg_mate.sh 2>&1 | tee newpkg_log.txt
~~~
