# Networking Packages

## Official

### install web server

openssl openssl-1.1 vsftpd
lighttpd perl-cgi apache

### install mysql

mysql++ mariadb
mariadb-libs

### install python microserver

python-flask python-dotenv
python-mysql-connector
python-mysqlclient
python-mongoengine
python-requests
python-pymongo

### install mqtt broker

mosquitto libwebsockets

--------------------------------------------------------------------------------

## AUR

### install meeting program

- https://aur.archlinux.org/packages/zoom/

### install social media

- https://aur.archlinux.org/packages/whatsdesk-bin/

### install http tools

- https://aur.archlinux.org/packages/postman-bin/

--------------------------------------------------------------------------------

## Configurations

### configure apache

```sh
sudo sed -i "s@#LoadModule unique_id_module@LoadModule unique_id_module@g" /etc/httpd/conf/httpd.conf

systemctl start httpd
systemctl enable httpd

echo "<html>
 <title>Welcome</title>
  <body>
   <h2>Welcome to HTML test page</h2>
  </body>
</html>" | sudo tee /srv/http/index.html

w3m http://localhost/index.html
```

### configure mysql

#### initialization

```sh
sudo chown -R mysql /var/lib/mysql
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

sudo systemctl enable mysqld
sudo systemctl start mysqld

sudo mariadb -B -u root -e 'SHOW DATABASES'
```

#### create new user

```sh
sudo mariadb -u root

SELECT User,Host FROM mysql.user;
CREATE USER 'sqluser'@localhost IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'sqluser'@localhost WITH GRANT OPTION;
FLUSH PRIVILEGES;

exit
```

#### check new user

```sh
mariadb -u sqluser
exit
```

#### remove new user

```sh
sudo mariadb -u root

SELECT User,Host FROM mysql.user;
DROP USER 'sqluser'@localhost;
FLUSH PRIVILEGES;

exit
```

### configure mosquitto

```sh
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

```sh
mosquitto_sub -t hello/world
mosquitto_pub -t hello/world -m "MQTT on ArchLinux"
```

### configure ftp server

```sh
echo 'vsftpd: ALL
vsftpd: 10.0.0.0/255.255.255.0
' | sudo tee /etc/hosts.allow

echo '
listen=YES
local_enable=YES
write_enable=NO
local_root=/home/alarm/Downloads/
anonymous_enable=YES
no_anon_password=YES
anon_upload_enable=NO
anon_mkdir_write_enable=NO
anon_other_write_enable=NO
anon_world_readable_only=YES
anon_root=/home/alarm/Downloads/
ftpd_banner=Welcome on Achmadi Movie Torrent
' | sudo tee /etc/vsftpd.conf

sudo systemctl enable vsftpd
sudo systemctl start vsftpd

# test on local
ftp localhost
```
