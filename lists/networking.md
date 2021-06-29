##### install web server
apache wt fcgi
openssl openssl-1.0
perl-cgi perl-cgi-fast

##### install mqtt broker
mosquitto libwebsockets

##### install mysql
mysql++ mariadb
mariadb-libs

##### install python webserver
python-flask python-werkzeug
python-tornado python-pycurl
python-pyodbc python-psycopg2
python-mysqlclient
python-mysql-connector
python-django-extensions
python-django python-django-q
python-blinker python-simplejson

##### install python networking
python-pbkdf2 python-pycryptodome

##### install webkit/webengine
qt5-webkit webkit2gtk
python-pyqtwebengine

##### install telegram
telegram-desktop

--------------------------------------------------------------------------------

##### install meeting program
- https://aur.archlinux.org/packages/zoom/
- https://aur.archlinux.org/packages/teams/

##### install chat program
- https://aur.archlinux.org/packages/whatsapp-for-linux/

##### install youtube program
- https://aur.archlinux.org/packages/youtube-bin/
- https://aur.archlinux.org/packages/youtube-dl-git/
- https://aur.archlinux.org/packages/youtube-dl-qt-git/

##### install remote pc
- https://aur.archlinux.org/packages/teamviewer/

##### install http tools
- https://aur.archlinux.org/packages/postman-bin/

##### install mongodb
- https://aur.archlinux.org/packages/mongodb-bin/
- https://aur.archlinux.org/packages/mongodb-tools-bin/

##### install public ip tunnel
- https://aur.archlinux.org/packages/ngrok-bin/
- https://aur.archlinux.org/packages/ngrok-tunnel-docker/

##### install cisco packet simulator
- https://aur.archlinux.org/packages/packettracer/

##### install python networking
- https://aur.archlinux.org/packages/python-wifiwrapper/

--------------------------------------------------------------------------------

##### configure teams login

~~~
echo 'adjust timezone'
sudo ln -svf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
~~~

##### configure apache

~~~
sudo sed -i "s@#LoadModule unique_id_module@LoadModule unique_id_module@g" /etc/httpd/conf/httpd.conf

systemctl start httpd
systemctl enable httpd

echo "<html>
 <title>Welcome</title>
  <body>
   <h2>Welcome to HTML test page</h2>
  </body>
</html>" | sudo tee /srv/http/index.html
~~~

##### configure mysql

~~~
sudo chown -R mysql /var/lib/mysql
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

sudo systemctl enable mysqld
sudo systemctl start mysqld

sudo mysql -N -B -u root -e 'SHOW DATABASES'
~~~

~~~
sudo mysql -u root
SELECT User,Host FROM mysql.user;
CREATE USER 'sqluser'@localhost IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'sqluser'@localhost WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit

mysql -u sqluser
exit

sudo mysql -u root
SELECT User,Host FROM mysql.user;
DROP USER 'sqluser'@localhost;
FLUSH PRIVILEGES;
exit
~~~

##### configure mosquitto

~~~
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
~~~

~~~
mosquitto_sub -t hello/world
mosquitto_pub -t hello/world -m "MQTT on ArchLinux"
~~~

##### configure teamviewer

~~~
sudo rm -f /usr/share/applications/teamviewerapi.desktop

sudo systemctl enable teamviewerd
sudo systemctl start teamviewerd
~~~

##### configure cisco packet simulator

~~~
sudo ln -svf /opt/packettracer/packettracer /usr/bin/packettracer
~~~

##### configure youtube

~~~
sudo sed -i 's#Categories=Video;#Categories=Network;Application;#g' \
/usr/share/applications/Youtube-bin.desktop
~~~

##### configure youtube-dl

~~~
youtube-dl -F https://www.youtube.com/watch?v=xxxxxxxxxxx
youtube-dl -f vid+aud --merge-output-format mkv https://www.youtube.com/watch?v=xxxxxxxxxxx
youtube-dl -f 137+251 --merge-output-format mkv https://www.youtube.com/watch?v=xxxxxxxxxxx

echo "vid code -> 1920x1080: avc1.64xxxx, 25fps, video only"
echo "aud code -> audio only: opus @160k (48000Hz)"

FILENM="LP Rebellion"
ffmpeg -i "${FILENM}.webm" -vn -ab 128k -ar 44100 -y "${FILENM}.mp3"
~~~

##### configure public ip

~~~
ngrok authtoken 1xxxxxxxxxxxxxxxx_yyyyyyyyyyyyyyy
ngrok http 80
~~~

##### configure free VPS
- https://www.heroku.com/
- https://vercel.com/
- https://www.netlify.com/

