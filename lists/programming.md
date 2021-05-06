##### install fortran compiler
gcc-fortran arpack

##### install debugger
nemiver valgrind lldb

##### install python2 builder
python2-setuptools
cython2 python2-pip
python2-wheel python2-six

##### install opengl programming
freeglut glu glm
glfw-x11 glew
python-opengl

##### install javascript programming
code electron11
typescript ts-node

##### install docker
docker docker-machine docker-compose
python-docker python-dockerpty

##### install build dependencies
ant guile2.0
libharu gtest
utf8cpp pegtl
patchelf gperf
xmlto asciidoc
libcurl-gnutls
swt maven junit
libxslt chrpath
texinfo perl-gd

--------------------------------------------------------------------------------

##### install glade-gtk2
- https://aur.archlinux.org/packages/glade-gtk2/
- https://aur.archlinux.org/packages/python2-gobject2/

##### install wxgtk programming
- https://aur.archlinux.org/packages/gamin/ (--asdeps)
- https://aur.archlinux.org/packages/codeblocks-svn/
- https://aur.archlinux.org/packages/wxformbuilder-git/

##### install android sdk
- https://aur.archlinux.org/packages/android-sdk/
- https://aur.archlinux.org/packages/android-platform-28/
- https://aur.archlinux.org/packages/android-platform-29/
- https://aur.archlinux.org/packages/android-platform-30/
- https://aur.archlinux.org/packages/android-sdk-platform-tools/
- https://aur.archlinux.org/packages/android-sdk-build-tools-29.0.2/

##### install android screen mirror
- https://aur.archlinux.org/packages/scrcpy/

##### install vim-coc languages
- https://aur.archlinux.org/packages/vim-coc-css-git/
- https://aur.archlinux.org/packages/vim-coc-html-git/
- https://aur.archlinux.org/packages/vim-coc-java-git/
- https://aur.archlinux.org/packages/vim-coc-json-git/
- https://aur.archlinux.org/packages/vim-coc-yaml-git/
- https://aur.archlinux.org/packages/vim-coc-tsserver-git/

--------------------------------------------------------------------------------

##### install custom doxygen tools
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/custom-doxygen/

##### install codeblocks additionals
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/cbp2make/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/cbcc-stm32/

##### install android reverse tethering
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/gnirehtet-bin/

##### install java build system
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/bazel-bin/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/gradle-bin/

##### install java android programming
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/android-flutter/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/android-apksign/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/android-envars/

##### install vscode settings
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vscode-settings/

##### install vim additionals
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vimlsp-tex/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vimlsp-dart/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/vimlsp-flutter/

--------------------------------------------------------------------------------

##### configure codeblocks bugs

~~~
sudo sed -i '28s#n") +#n" +#' /usr/share/codeblocks/templates/wizard/gtk/wizard.script
~~~

##### configure android-sdk

~~~
sudo groupadd android-sdk
sudo gpasswd -a $USER android-sdk
sudo setfacl -R -m g:android-sdk:rwx /opt/android-sdk
sudo setfacl -d -m g:android-sdk:rwx /opt/android-sdk

#sdkmanager --licenses
signapk default
~~~

##### configure flutter

~~~
sudo groupadd flutterusers
sudo gpasswd -a $USER flutterusers
sudo chown -Rf :flutterusers /opt/flutter
sudo chmod -Rf g+w /opt/flutter
~~~

~~~
#sudo archlinux-java set java-8-openjdk
echo "Re-Login before continue"

flutter doctor
flutter doctor --android-licenses
~~~

~~~
flutter create appname
flutter create --offline appname
cd appname/

flutter run
flutter build apk --split-per-abi

flutter clean
gradle --stop
~~~

~~~
#flutter upgrade

flutter config --enable-linux-desktop
flutter config --enable-windows-desktop
flutter devices

flutter create appname
flutter create --offline appname

flutter run -d linux
flutter run -d windows

flutter build linux
flutter build windows
~~~

##### configure vscodium

~~~
echo "copy some settings"
vscode-set
~~~

~~~
echo "install some usefull plugins"
echo "Python, Clangd, Flutter, Dart, ,TexLab, Vim"

ls ~/.vscode-oss/extensions/
~~~

##### configure docker

~~~
echo "loop" | sudo tee /etc/modules-load.d/loop.conf
sudo modprobe loop

sudo groupadd -f docker
sudo gpasswd -a $USER docker

sudo systemctl enable docker.service
sudo systemctl start docker.service

docker pull hello-world
docker run hello-world
~~~

~~~
sudo systemctl stop docker
mkdir -p /path/to/your/docker
sudo chown -R root:root /path/to/your/docker
sudo touch /etc/docker/daemon.json
echo '
{
    "data-root": "/path/to/your/docker"
}' | sudo tee /etc/docker/daemon.json
sudo rsync -aP /var/lib/docker/ /path/to/your/docker
sudo systemctl start docker
~~~

~~~
git clone https://github.com/repo/dockerweb.git
cd dockerweb/

ls docker-compose.yml
docker-compose up --build

docker-compose up
docker-compose down
docker-compose up -d --build
~~~
