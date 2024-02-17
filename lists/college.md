# College Packages

## Official

### install libreoffice

libreoffice-fresh coin-or-mp

### install fortran

gcc-fortran arpack
r mpdecimal gnuplot

### install python computing

python-pygments
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

### install python jupyter

jupyterlab jupyter-notebook

### install python additional

python-pyaudio python-sounddevice
python-pillow python-beautifulsoup4
python-invoke python-flit python-cffi

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

### install wps office

- https://aur.archlinux.org/packages/libtiff5/
- https://aur.archlinux.org/packages/wps-office/
- https://aur.archlinux.org/packages/ttf-wps-fonts/

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

### configure r programming

- [CRAN MIRRORs](https://cran.r-project.org/mirrors.html)
- [Packages](https://support.posit.co/hc/en-us/articles/201057987-Quick-list-of-useful-R-packages)
- [Tutorial](https://www.tutorialspoint.com/r/index.htm)

```sh
mkdir -p $HOME/R/library
echo ".libPaths('$HOME/R/library')" | tee ~/.Rprofile
echo '.First <- function() {
  message("Welcome back ", Sys.getenv("USER"),"!\n","Working directory is: ", getwd())
}
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://mirror.aarnet.edu.au/pub/CRAN/"
  options(repos = r)
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

r -e 'install.packages(c("ImportExport","tidymodels","tidyverse","markdown"))'
r -e 'install.packages(c("randomForest","party","survival","plyr","plotrix"))'
r -e 'install.packages(c("streamR","shiny","httpgd","GGally","haven","XML2R"))'

sudo R CMD javareconf
r -e 'install.packages("xlsx")'
r -e 'options(java.parameters = c("-XX:+UseConcMarkSweepGC", "-Xmx2048m"))'
r -e 'library(xlsx)'
```

```sh
# using VSCode

code --force --install-extension reditorsupport.r
```

### configure wps office

```sh
sudo rm -f /usr/share/applications/wps-office-pdf.desktop
sudo rm -f /usr/share/applications/wps-office-prometheus.desktop
sudo sed -i '/^$/d' /usr/share/desktop-directories/wps-office.directory
echo 'NoDisplay=true' | sudo tee -a /usr/share/desktop-directories/wps-office.directory
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
