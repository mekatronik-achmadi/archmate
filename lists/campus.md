##### install libreoffice
libreoffice-fresh
coin-or-mp unoconv
libreoffice-fresh-id
libreoffice-extension-texmaths
libreoffice-extension-writer2latex

##### install python computing
spyder jupyterlab
jupyter-notebook
python-pyaudio
python-gnuplot
python-pytables
python-matplotlib
python-bottleneck
python-virtualenv
python-statsmodels
python-sounddevice
python-scikit-learn
python-beautifulsoup4
python-cffi python-yaml
python-patsy python-nose
python-numpy python-rpy2
python-sympy python-scipy
python-pandas python-h5py
python-pillow python-seaborn
python-pyqtdatavisualization

##### install tesseract
python-pytesseract
tesseract-data-eng
tesseract-data-ind

##### install sage
sagemath sagemath-jupyter

##### install latex
texlive-formatsextra
texlive-bibtexextra
texlive-latexextra
texlive-publishers
texlive-fontsextra
texlive-pictures
texlive-pstricks
texlive-science
texlive-core
texlive-bin
latex2html
latex2rtf
texstudio
dblatex
minted
biber

##### install opencv
opencv hdf5 vtk

##### install python learning
python-tensorflow-estimator tensorboard
python-keras-applications python-keras-preprocessing

~~~
basic
~~~
tensorflow
python-pytorch
python-tensorflow

~~~
cpu avx2
~~~
tensorflow-opt
python-pytorch-opt
python-tensorflow-opt

~~~
nvidia cuda
~~~
tensorflow-cuda
python-pytorch-cuda
python-tensorflow-cuda

##### install maxima
wxmaxima maxima-ecl
rlwrap gnuplot

--------------------------------------------------------------------------------

##### install diagram editor
- https://aur.archlinux.org/packages/yed/

##### install mendeley
- https://aur.archlinux.org/packages/mendeleydesktop-bundled/

##### install project manager
- https://aur.archlinux.org/packages/projectlibre/

##### install data tools
- https://aur.archlinux.org/packages/scidavis-qt5/

##### install opencv additionals
- https://aur.archlinux.org/packages/python-imutils/

##### install python learning
- https://aur.archlinux.org/packages/python-keras/
- https://aur.archlinux.org/packages/python-theano/

##### install ncurses5 (for matlab-bin)
- https://aur.archlinux.org/packages/ncurses5-compat-libs/ (--skippgpcheck)

##### install r-studio
- https://aur.archlinux.org/packages/rstudio-desktop-bin/

##### install jupyterthemes
- https://aur.archlinux.org/packages/python-lesscpy/ (--asdeps)
- https://aur.archlinux.org/packages/jupyterthemes/

--------------------------------------------------------------------------------

##### install texstudio themes
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/texstudio-themes/

##### install matlab binary
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/matlab-bin/matlab-bin-basic/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/matlab-bin/matlab-bin-core/

##### install matlab themes
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/matlab-bin/matlab-schemer/

##### install python computing
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/mle/
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/simupy/

##### install python thorlabs pm100
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/instrumental/ (--asdeps)
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/pm100/

##### install OTDR python parser
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/pyutils  (--asdeps)
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/lazyxml  (--asdeps)
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/crcmod  (--asdeps)
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/python-modules/pyotdr

##### install pychoacoustics
- https://github.com/mekatronik-achmadi/archmate/tree/master/packages/pkgbuild/pychoacoustics/

--------------------------------------------------------------------------------

##### configure mendeley desktop

~~~
sudo sed -i 's#mendeleydesktop %f#mendeleydesktop -style gtk %f#g' /usr/share/applications/mendeleydesktop.desktop
sed -i 's#mendeleydesktop %f#mendeleydesktop -style gtk %f#g' ~/.local/share/applications/mendeleydesktop.desktop
~~~

##### configure scidavis

~~~
sudo sed -i "s#Categories=Qt;Science;DataVisualization;#\
Categories=Education;Math;Science;#g" /usr/share/applications/scidavis.desktop
~~~


##### configure texstudio

~~~
"latex -shell-escape -src -interaction=nonstopmode %.tex"
"pdflatex -shell-escape -synctex=1 -interaction=nonstopmode %.tex"
~~~

##### configure jupyter themes

~~~
jt -t onedork -altp -N -f inconsolata -fs 9 -tfs 11 -nfs 11 -ofs 8 -cellw 100%
jt -t grade3 -altp -N -f inconsolata -fs 9 -tfs 11 -nfs 11 -ofs 8 -cellw 100%
jt -r
~~~

~~~
from jupyterthemes import jtplot

jtplot.style(theme='onedork')
jtplot.style(theme='grade3')
~~~

##### configure matlab

~~~
echo "09806-07443-53955-64350-21751-41297"
~~~

~~~
sudo mount R2018a_glnxa64_dvd1.iso /mnt/
/mnt/install &
sudo umount /mnt/
sudo mount R2018a_glnxa64_dvd2.iso /mnt/
~~~

~~~
sudo cp libmwlmgrimpl.so /opt/mathworks/matlab-2018a/bin/glnxa64/matlab_startup_plugins/lmgrimpl/
sudo chown -R $USER:users $HOME/.matlab/R2018a/
~~~

~~~
matlab-cli
cd /opt/mathworks/addons/schemer/
schemer_import
~~~

##### configure wxmaxima

~~~
echo "dark theme ini file to load"
xdg-open https://gist.github.com/motchy869/fd68dba6d7320f0335092c9ffe47611a#file-dark-style-ini
~~~
