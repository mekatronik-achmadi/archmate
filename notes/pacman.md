### basic commands

~~~
nano /var/log/pacman.log
nano /etc/pacman.conf
nano /etc/wgetrc
nano /etc/pacman.d/mirrorlist
ls /var/lib/pacman/sync/*.db
ls /var/lib/pacman/sync/*.files
ls /var/cache/pacman/pkg/*.pkg.tar.xz
pacman -Sy
pacman -S <package_name | package_group_name>
pacman -Sy <package_name | package_group_name>
pacman -S --force <package_name | package_group_name>
pacman -S <package_name | package_group_name> --ignore <package_name>
pacman -Sy
pacman -Su
pacman -Sgg
pacman -Sg <package_group_name>
pacman -Sw <package_name>
pacman -Sup
pacman -Sp <package_name>
pacman -Sc
pacman -Scc
pacman -Sl
pacman -Sl <repository>
pacman -S <repository>/<package_name>
pacman -Ssq <part_package_name>
pacman -Sii <package_name>
pacman -Fy
pacman -Fs <part_filename>
pacman -Qq | grep <package_name>
pacman -Qii <package_name>
pacman -Qlq <package_name>
pacman -Qo <full_filename>
pacman -U packagefile.pkg.tar.gz
pacman -U --force packagefile.pkg.tar.gz
pacman -U --asdeps packagefile.pkg.tar.gz
pacman -U --asexplicit packagefile.pkg.tar.gz
pacman -Rs <package_name | package_group_name>
pacman -Rns <package_name | package_group_name>
pacman -Rns $(pacman -Qdtq)
pacman -Rns $(pacman -Qdttq)
yes | pacman -S <package_name>
yes | pacman -U packagefile.pkg.tar.gz
yes | pacman -Rns <package_name>
pactree <package_name>
paclist repository
pacstrap <mount-point> <package_name>
pacstrap <mount-point> <package_group_name>
pacstrap -i <mount-point> <package_name>
pacstrap -c <mount-point> <package_name>
pacstrap -d <directory> <package_name>
pacstrap -G <mount-point> <package_name>
pacstrap -M <mount-point> <package_name>
pacman-key --init
pacman-key --populate archlinux
pacman-key --populate archlinux manjaro
pacman-key --refresh-keys
~~~

---------------------------------------------------------

### package to add on update

~~~
package_name
build/package_name
~~~

### package to remove on update

~~~
package_name
build/package_name
~~~

---------------------------------------------------------

### Mirrors
- https://www.archlinux.org/mirrorlist/
- https://www.archlinux.org/mirrorlist/all/
- https://wiki.archlinux.org/index.php/Mirrors
- http://archlinuxarm.org/about/mirrors
- https://github.com/archlinuxarm/PKGBUILDs/blob/master/core/pacman-mirrorlist/mirrorlist

### Package Sources
- https://git.archlinux.org/svntogit/packages.git/log/?h=packages/<package_name>
- https://git.archlinux.org/svntogit/community.git/log/?h=packages/<package_name>
- https://git.archlinux.org/svntogit/packages.git/tree/trunk?h=packages/<package_name>
- https://git.archlinux.org/svntogit/community.git/tree/trunk?h=packages/<package_name>

### AUR Repository
- https://wiki.archlinux.org/index.php/Arch_User_Repository
- https://aur.archlinux.org/

### Unofficial User Repository
- https://wiki.archlinux.org/index.php/Unofficial_user_repositories

### Archive Repository
- https://wiki.archlinux.org/index.php/Arch_Linux_Archive
- https://wiki.archlinux.org/index.php/downgrading_packages
- https://archive.archlinux.org/packages/
- https://archive.org/details/archlinuxarchive

---------------------------------------------------------

### Online Repository

~~~
# /etc/pacman.conf
# $repo = core, extra, community, or multilib
# $arch = i686, x86_64, armhf, or other architecture
# http://mirror.labkom.id/archlinux/iso/
~~~

~~~
echo -e "
[core]
Server = http://mirror.labkom.id/archlinux/\$repo/os/\$arch

[extra]
Server = http://mirror.labkom.id/archlinux/\$repo/os/\$arch

[community]
Server = http://mirror.labkom.id/archlinux/\$repo/os/\$arch

[multilib]
Server = http://mirror.labkom.id/archlinux/\$repo/os/\$arch
"
~~~

### Signature Check Level

~~~
# SigLevel = Never
# SigLevel = Optional TrustAll
# SigLevel = Required Database Optional
# LocalFileSigLevel = Optional
# RemoteFileSigLevel = Required
~~~

~~~
sed -i 's/SigLevel.*/SigLevel = Never/g' /etc/pacman.conf
~~~

### Package Databases URL
http://mirror.labkom.id/archlinux/core/os/x86_64/core.db
http://mirror.labkom.id/archlinux/extra/os/x86_64/extra.db
http://mirror.labkom.id/archlinux/community/os/x86_64/community.db
http://mirror.labkom.id/archlinux/multilib/os/x86_64/multilib.db

### Pacman Wget

~~~
# XferCommand = /usr/bin/wget --passive-ftp -c -O %o %u
~~~

~~~
pacman -S wget
sed -i "s@#XferCommand = /usr/bin/wget@XferCommand = /usr/bin/wget@g" /etc/pacman.conf
~~~

---------------------------------------------------------

### Create Custom Repository

~~~
# $repo -> custom-repo-name
# $arch -> i686, x86_64, armhf, or other architecture
# Server -> URL or file path
~~~

~~~
echo -e "
[custom]
SigLevel = Never
Server = file:///path
#Server = https://URL
" >> /etc/pacman.conf
~~~

### Repository File Index

~~~
repo-add /path/custom.db.tar.gz /path/*.pkg.tar.xz
cp /path/custom.db.tar.gz /path/custom.db
~~~

---------------------------------------------------------

### Backup Installation

~~~
pacman -Qq > pkglist-x86_64.txt
sudo pacman -Sc
rsync -avh --delete /var/lib/pacman/sync/ databases/
rsync -avh --delete /var/cache/pacman/pkg/ packages/archived/
rsync -avh --delete -b --backup-dir=/home/username/backup-dir/path/ /var/cache/pacman/pkg/ packages/archived/
rsync -avh --delete ~/development/Packages/ArchLinux-x86_64/ ./
rsync -avh --delete --exclude '.git' --exclude 'tugas_akhir' --exclude 'tugas_kuliah' --exclude 'DRAFT' ~/development/Projects/ ./
sudo mv -vf /var/log/pacman.log /var/log/pacman-$(date +%Y%m%d-%H%M).log
sudo touch /var/log/pacman.log
~~~

### Backup on ISO

~~~
mkdir -p pkgiso/databases/
mkdir -p pkgiso/packages/

cp -v /etc/pacman.conf pkgiso/

cp -v /var/lib/pacman/sync/* pkgiso/databases/

pacman -Sp $(cat listpkg-x86_64.txt) > file.txt
sed -i "s#file://##g" file.txt
for i in `cat file.txt`;do cp -v $i pkgiso/packages/;done

genisoimage -l -r -J -V "archlinuxpkg" -o archlinuxpkg.iso pkgiso

rm -vf file.txt
rm -rvf pkgiso/
~~~

---------------------------------------------------------

### Pacman eat powerpills

~~~
# /etc/pacman.conf
~~~

~~~
# Misc options
ILoveCandy
~~~
