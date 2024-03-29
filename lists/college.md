# College Packages

## Official

### install libreoffice

libreoffice-still coin-or-mp

### install fortran

gcc-fortran arpack
r mpdecimal gnuplot

### install python modules

python-pyarrow
python-tabulate
python-matplotlib
python-bottleneck
python-statsmodels
python-scikit-learn
python-h5py-openmpi
python-pandas-datareader
python-numpy python-rpy2
python-sphinx python-dask
python-sympy python-scipy
python-gnuplot python-yaml
python-seaborn python-patsy
python-pytables python-tqdm
python-pandas python-numexpr

### install python interface

ipython jupyterlab
jupyter-notebook
python-pygments

### install python additional

python-setuptools-scm
python-beautifulsoup4
python-flit python-cffi
python-pillow python-pyaudio
python-invoke python-sounddevice

### install texlive

texlive texlive-langenglish
texstudio minted biber pdftk
dblatex latex2html latex2rtf

### install opencv library

opencv hdf5-openmpi
python-opencv vtk

### install programming additionals

fftw liquid-dsp libsndfile

--------------------------------------------------------------------------------

## AUR

### install ms fonts

- https://aur.archlinux.org/packages/ttf-tahoma/
- https://aur.archlinux.org/packages/ttf-ms-fonts/
- https://aur.archlinux.org/packages/ttf-vista-fonts/

### install onlyoffice

https://aur.archlinux.org/packages/onlyoffice-bin/

### install python additionals

- https://aur.archlinux.org/packages/python-soundfile/
- https://aur.archlinux.org/packages/python-pyfftw/

### install audio tools

- https://aur.archlinux.org/packages/roomeqwizard/
- https://aur.archlinux.org/packages/wavesurfer/
- https://aur.archlinux.org/packages/snack/

### install shell additional

- https://aur.archlinux.org/packages/littler/
- https://aur.archlinux.org/packages/ttyplot-git/
- https://aur.archlinux.org/packages/ncurses5-compat-libs/

--------------------------------------------------------------------------------

## External

### install python visa tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/python-modules/instrumental/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/python-modules/pyotdr/
- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/python-modules/pm100/

### install python acoustics tools

- https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/optional/pychoacoustics/

--------------------------------------------------------------------------------

## Configurations

### configure onlyoffice

```sh
sudo sed -i 's#desktopeditors %F#desktopeditors --system-title-bar %F#g' \
/usr/share/applications/onlyoffice-desktopeditors.desktop
sudo sed -i 's#desktopeditors --new#desktopeditors --system-title-bar --new#g' \
/usr/share/applications/onlyoffice-desktopeditors.desktop
```

### configure r programming

- [CRAN MIRRORs](https://cran.r-project.org/mirrors.html)
- [Packages](https://support.posit.co/hc/en-us/articles/201057987-Quick-list-of-useful-R-packages)
- [Tutorial](https://www.tutorialspoint.com/r/index.htm)

```sh
mkdir -p $HOME/R/library
echo ".libPaths(\"$HOME/R/library\")" | tee ~/.Rprofile
echo '.First <- function() {
  message("User: ", Sys.getenv("USER"), "\n", "WorkDir: ", getwd())
}
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://mirror.aarnet.edu.au/pub/CRAN/"
  options(repos = r)
  options(timeout = 120)
})' | tee -a ~/.Rprofile

R -e 'print(R.version.string)'
R -e 'print(.libPaths())'
R -e 'print(library())'

R -e 'install.packages("languageserver")'
vim -c "CocInstall coc-r-lsp"

# alternative little-r
#R -e 'install.packages("littler")'
#echo 'export PATH=$PATH:~/R/library/littler/bin' | tee -a ~/.bashrc
```

```sh
r -e 'print(R.version.string);print(.libPaths())'
r -e 'print(library())'

r -e 'install.packages(c("ImportExport","tidymodels","tidyverse","markdown"))'
r -e 'install.packages(c("randomForest","party","survival","haven","jsonlite"))'
r -e 'install.packages(c("streamR","shiny","httpgd","GGally","plyr","plotrix"))'

#sudo R CMD javareconf
#r -e 'install.packages("xlsx")'
#r -e 'options(java.parameters = c("-XX:+UseConcMarkSweepGC", "-Xmx2048m"))'
#r -e 'library(xlsx)'
```

```sh
# using VSCode

code --force --install-extension reditorsupport.r
```

### configure texstudio

```sh
"latex -shell-escape -src -interaction=nonstopmode %.tex"
"pdflatex -shell-escape -synctex=1 -interaction=nonstopmode %.tex"
```

```sh
FancyVerb error \end{minted}
Just delete \t (Tab) after \end{minted}
```

```sh
Uncheck 'Adv. Editor'->'Structure Panel'->'Mark structure elements beyond \end{document}'
```

### configure roomeqwizard

```sh
sudo sed -i 's#Categories=Application;#Categories=AudioVideo;Audio;Player;#g' \
/usr/share/applications/roomeqwizard/roomeqwizard.desktop

echo "Terminal=false" | sudo tee -a /usr/share/applications/roomeqwizard/roomeqwizard.desktop
echo "Comment=Room Equalizer Wizard"  | sudo tee -a /usr/share/applications/roomeqwizard/roomeqwizard.desktop
```
