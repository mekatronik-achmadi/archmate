### matlab binary packages

#### core
- MATLAB core
- No Toolboxes
- No Simulink

#### basic
- Matlab core
- Toolboxes
- No Simulink

#### all
- Matlab core
- Toolboxes
- Simulink

### mount ISO

~~~
sudo mount R2018a_glnxa64_dvd1.iso /mnt
~~~

### create installation folder

~~~
mkdir matlab-2018a
~~~

### start installation

~~~
/mnt/install
~~~

### install using gui
- Check 'Use a File Installation Key' and press Next.
- Choose 'File Installation Key' and enter product codes.
- Enter installation folder at 
~~~
$PWD_DIR/matlab-2018a-install/
~~~
- Select product you need.
- Continue installation
- Finish

### copy mathworks crack file

~~~
cp -vf ./crack_2018a/libmwservices.so matlab-2018a/bin/glnxa64/
~~~

### tar installation folder

~~~
tar -cvf matlab-2018a.tar matlab-20158a/
rm -rvf matlab-2018a/
~~~

### move installation to packaging folder

~~~
mv matlab-2018a.tar ../sources/matlab-bin-basic/
~~~

### build package

~~~
cd ../sources/matlab-bin-basic/
makepkg -sr
rm -vf matlab-2018a.tar
rm -rvf pkg/ src/
~~~

### install package

~~~
sudo pacman -U matlab-bin-*
~~~

### enter license

~~~
sudo cp -vf libmwservices.so /opt/mathworks/matlab_2015a/bin/glnxa64/
export MATLAB_LOG_DIR=~/.matlab-log
sudo matlab
~~~
- Choose 'Activate manually without internet'
- Enter 'Standalone_License.lic'

### matlab opengl

~~~
opengl info
opengl('save','software')
~~~