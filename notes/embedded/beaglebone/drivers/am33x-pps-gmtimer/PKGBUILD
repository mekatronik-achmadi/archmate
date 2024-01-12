pkgname=achmadi-am33x-drivers
pkgver=0.1
pkgrel=1
pkgdesc="some extra devices driver for BeagleBone Black by Achmadi"
arch=('i686' 'x86_64' 'armv7h')
url="https://github.com/mekatronik-achmadi/achmadi-am33x-drivers"
license=('GPL')
depends=()
makedepends=()
options=('!makeflags')
source=("$pkgname::git+https://github.com/mekatronik-achmadi/achmadi-am33x-drivers")
sha256sums=('SKIP')

build() {
	cd "$srcdir/$pkgname"
	make
	gzip pps-gmtimer.ko
	make achmadi-00A0.dtbo
}

package() {
	cd "$srcdir/$pkgname"

	install -d $pkgdir/usr/lib/firmware/
	mv -vf achmadi-00A0.dtbo $pkgdir/usr/lib/firmware/

	install -d $pkgdir/usr/lib/modules/$(uname -r)/kernel/drivers/achmadi/
	mv -vf pps-gmtimer.ko.gz $pkgdir/usr/lib/modules/$(uname -r)/kernel/drivers/achmadi/
}
