##### install qt programming
qt qt5 qtcreator
perf x11-ssh-askpass

##### install qt python bindings
sip4 python-pyqt5-sip
pyside2 pyside2-tools
python-pyqt5 python-qtpy

##### install qt5 graph plot
qcustomplot
qwt qwtpolar
pyqt-builder
python-pyqt3d
python-pyqtgraph
python-pyqtchart

--------------------------------------------------------------------------------

##### install qwt additionals
- https://aur.archlinux.org/packages/qwt5-qt5/
- https://aur.archlinux.org/packages/qwtplot3d-qt5/
- https://aur.archlinux.org/packages/python-pyqt-qwt/

--------------------------------------------------------------------------------

##### configure qtcreator

~~~
echo "Tools->Options->Environment->System"
echo "mate-terminal -x"
~~~

~~~
echo "Tools->Options->C++->Code Model"
echo "Interpret ambiguous headers as C headers"
echo "Ignore precompiled headers"
~~~

~~~
echo "Disable Clang Code Model"
echo "Help->About Plugins->ClangCodeModel"
echo "Help->About Plugins->ClangTools"
~~~

~~~
echo "Tools->Options->FakeVim->General"
echo "Use FakeVim"
~~~
