pkgname=about-axos
pkgver=2.0
pkgrel=1
pkgdesc="About AxOS is a system information tool for the AxOS operating system."
arch=('x86_64')
license=('GPL')
depends=('python' 'python-gobject' 'gtk4' 'libadwaita' 'meson' 'ninja' 'libadwaita' 'appstream-glib' 'gtksourceview5')
# sha256sums=('SKIP') 

build() {
  cd "${srcdir}"
  meson --prefix=/usr _build
  ninja -C _build
}

package() {
  cd "${srcdir}/_build"
  DESTDIR="${pkgdir}" ninja install
}
