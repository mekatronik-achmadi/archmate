### prepare build script

~~~
tar -xzf pkgname.tar.gz
cd pkgname/
cat PKGBUILD
~~~

### create and apply patch

~~~
diff -Naur filename.old filename.new > filename.patch
diff -Naur directory_old directory_new > filename.patch
patch filename.old filename.patch
patch -p1 < filename.patch
~~~

### compile and build a pkg.tar.gz package

~~~
setarch i386
setarch i686
setarch x86_64
~~~

~~~
makepkg -do
makepkg -sr
makepkg -ser
makepkg -sir
makepkg -seir
makepkg -Re
makepkg -Rei
makepkg --force
makepkg --repackage
makepkg --skippgpcheck
makepkg --skipchecksums
makepkg -sir --asdeps
makepkg -seir --asdeps
~~~

### archiving and building source directory

~~~
makepkg -do
export ZIPNAME=$(cat PKGBUILD | grep -m 1 -w "pkgname" | cut -d= -f2)
zip -r $ZIPNAME-src.zip ./src/
makepkg -seir
~~~

--------------------------------------------------------------------------------

### general content of PKGBUILD

~~~
pkgname=qtserialterminal
#_pkgname=qtserialterminal
#_gitname=qtserialterminal
~~~

~~~
pkgver=0.1
pkgrel=1
pkgdesc="program stm32 chip via bootloader"
url= "http://optional.source.url/"
license=('WTFPL')
~~~

~~~
arch=('x86_64')
#arch=('i686')
#arch=('any')
#arch=('i686' 'x86_64')
#arch=('armhf')
~~~

~~~
depends=('qt5-base' 'qt5-serialport')
#depends=()
makedepends=('qt5-base' 'qt5-serialport')
#makedepends=()
~~~

~~~
options=('makeflags')
#options=('staticlibs')
#options=('libtool')
#options=('!strip')
#options=('!emptydirs')
~~~

~~~
install=pkg.install
~~~

~~~
provides=("$pkgname")
#provides=("$pkgname=$pkgver")
conflicts=("$pkgname" "$pkgname-git")
~~~

~~~
source=('${pkgname}.zip')
#source=('${pkgname}-master.zip')
#source=('${pkgname}.zip' 'pkg.install')
#source=('${pkgname}-${pkgver}.tar.xz')
#source=('$pkgname.desktop $pkgname.sh $pkgname.xml')
#source=('https://github.com/git-cola/git-cola/archive/v$pkgver.zip')
#source=('http://ftp.gnome.org/pub/GNOME/sources/${_pkgname}/${pkgver:0:3}/${_pkgname}-${pkgver}.tar.xz')
#source=("$pkgname::git+https://github.com/mekatronik-achmadi/achmadi-installer")
#source=("gtkterm::git+http://git.fedorahosted.org/git/gtkterm.git#branch=0.99.7")
#source_x86_64=($pkgname-$pkgver.run::ftp://ftp.cadsoft.de/$pkgname/program/${pkgver%.*}/$pkgname-lin64-$pkgver.run)
#source_i686=($pkgname-$pkgver.run::ftp://ftp.cadsoft.de/$pkgname/program/${pkgver%.*}/$pkgname-lin32-$pkgver.run)
~~~

~~~
sha256sums=('19614e6b70c2560cc040d7507e351adc148d6a53696d5506e17a337185edcfa5')
#sha256sums_i686=('93428e5cd6938f6a5efccce5f9ca1d2223ba2118868efd810a3fc84caf871232')
#sha256sums_x86_64=('2e7d98dc3c03bbd6ff3c10b54001722f57e25f8db8776851beac6fe755c8a7a5')
#sha256sums=('SKIP')
#md5sums=('SKIP')
~~~

~~~
prepare() {
	cd "${pkgname}-master"
	#cd "$srcdir"
	#cd "${_gitname}"
	#cd "${pkgname}-${pkgver}"
	#cd "${_pkgname}-${pkgver}"
	#cd "$srcdir/${pkgname}-$pkgver"
	patch ${pkgname}/file file.patch
	#patch -p1 < ../../patch-file.patch
	#patch < patch-file.patch
	#patch -uN -i patch-file.patch
	#patch -uN -pX -i patch-file.patch
}
~~~

~~~
build() {
	cd "${pkgname}-master"
	#cd "$srcdir"
	#cd "${_gitname}"
	#cd "${pkgname}-${pkgver}"
	#cd "${_pkgname}-${pkgver}"
	#cd "$srcdir/${pkgname}-$pkgver"
	qmake
	#./autogen.sh
	#./configure
	make all
	#make all doc html
}
~~~

~~~
check() {
	cd "${pkgname}-master"
	#cd "$srcdir"
	#cd "${_gitname}"
	#cd "${pkgname}-${pkgver}"
	#cd "${_pkgname}-${pkgver}"
	#cd "$srcdir/${pkgname}-$pkgver"
	make check
}
~~~

~~~
package() {
	cd "${pkgname}-master"
	#cd "$srcdir"
	#cd "${_gitname}"
	#cd "${pkgname}-${pkgver}"
	#cd "${_pkgname}-${pkgver}"
	#cd "$srcdir/${pkgname}-$pkgver"
	make INSTALL_ROOT=${pkgdir} install
	#make install
	#make prefix=/usr DESTDIR="$pkgdir" install
	#make prefix=/usr DESTDIR="$pkgdir" install{,-doc,-html}
	install -d $pkgdir/path/
	mv -vf file $pkgdir/path/
	#mv -vf ../file $pkgdir/path/
}
~~~

~~~
sha256sum source_package.zip
sha256sum source_package.tar.gz
md5sum source_package.zip
md5sum source_package.tar.gz
~~~

--------------------------------------------------------------------------------

### general example of pkg.install

~~~
update() {
	update-desktop-database /usr/share/applications
	update-mime-database /usr/share/mime
	glib-compile-schemas /usr/share/glib-2.0/schemas/
}

post_install() {
	update
}

post_upgrade() {
	update
}

post_remove() {
	update
}
~~~

~~~
post_install() {
  gtk-update-icon-cache -q -t -f usr/share/icons/hicolor
  update-desktop-database -q
}

post_upgrade() {
  post_install
}

post_remove() {
  post_install
}
~~~

~~~
post_install() {
    echo -e "You must be in the following groups: "
    echo -e " * lock: for /var/lock/lockdev"
    echo -e " * uucp: for /dev/ttyS0"
}

post_upgrade() {
    post_install
}
~~~

--------------------------------------------------------------------------------

### example of general content AUR packages receipt

~~~
# overwrite specific PKGBUILD fields
# multiple version of "pkgname" grouped in one "pkgbase"
# check ./SRCINFO
~~~

~~~
pkgbase = eagle
pkgname = eagle
pkgdesc = A powerful suite for schematic capture and printed circuit board design (aka eaglecad)
pkgver = 7.3.0
pkgrel = 2
url = http://www.cadsoft.de/
install = eagle.install
arch = ('i686' 'x86_64')
license = custom
depends = ('desktop-file-utils' 'fontconfig' 'libcups' 'libxcursor' 'libxi' 'libxrandr' 'shared-mime-info')
options = (!emptydirs)
sources = ('eagle.desktop' 'eagle.sh' 'eagle.xml')
sha256sums = ('86307352ad81aa0dee0dfe58ab6799b06200d489a8f6cef77845e772202d20a6'
			'0e38128c87ad72b692e16d5be75b7b21182e4e89caeadfc2bb285588c060176c'
			'293ef717030e171903ba555a5c698e581f056d2a33884868018ab2af96a94a06')
source_i686 = ("eagle-7.3.0.run::ftp://ftp.cadsoft.de/eagle/program/7.3/eagle-lin32-7.3.0.run")
sha256sums_i686 = ('93428e5cd6938f6a5efccce5f9ca1d2223ba2118868efd810a3fc84caf871232')
source_x86_64 = ("eagle-7.3.0.run::ftp://ftp.cadsoft.de/eagle/program/7.3/eagle-lin64-7.3.0.run")
sha256sums_x86_64 = ('2e7d98dc3c03bbd6ff3c10b54001722f57e25f8db8776851beac6fe755c8a7a5')
~~~

--------------------------------------------------------------------------------

### qmake variable for "make install"

~~~
# project.pro
~~~

~~~
target.path = /usr/local/bin
INSTALLS += target
~~~

### Makefile basic command for "make install"

~~~
install -d /usr/local/bin/
install -m 755 -p qtserialterminal /usr/local/bin/qtserialterminal
install -d /usr/local/share/qtserialterminal
cp -rvf resources /usr/local/share/qtserialterminal
~~~

### Makefile for "make install"

~~~
PREFIX = /usr/local
INSTALL = install
COPY	= cp -rvf
install:
	$(INSTALL) -d $(DESTDIR)$(PREFIX)/bin
	$(INSTALL) -m 755 stm32_microxplorer $(DESTDIR)$(PREFIX)/bin
	$(INSTALL) -d $(DESTDIR)$(PREFIX)/share/stm32_microxplorer
	$(COPY) db $(DESTDIR)$(PREFIX)/share/stm32_microxplorer
~~~

--------------------------------------------------------------------------------


### makepkg download agent using wget

~~~
# Format: 'protocol::agent args'
~~~

~~~
DLAGENTS=('ftp::/usr/bin/wget -c --passive-ftp -t 3 --waitretry=3 -O %o %u'
          'http::/usr/bin/wget -c -t 3 --waitretry=3 -O %o %u'
          'https::/usr/bin/wget -c -t 3 --waitretry=3 --no-check-certificate -O %o %u')
~~~

~~~
# set makepkg download agent to wget
~~~

~~~
sed -i "s#ftp::/usr/bin/curl -fC - --ftp-pasv --retry 3 --retry-delay 3 -o %o %u#ftp::/usr/bin/wget -c --passive-ftp -t 3 --waitretry=3 -O %o %u#g" /etc/makepkg.conf
sed -i "s#http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %o %u#http::/usr/bin/wget -c -t 3 --waitretry=3 -O %o %u#g" /etc/makepkg.conf
sed -i "s#https::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %o %u#https::/usr/bin/wget -c -t 3 --waitretry=3 --no-check-certificate -O %o %u#g" /etc/makepkg.conf
~~~

