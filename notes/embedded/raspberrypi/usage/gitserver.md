# Git Server

## Git Web

### login SSH

```sh
ssh -Y alarm@10.124.4.150
```

### run headless

```sh
sudo sed -i 's#gpu_mem=256#gpu_mem=16#g' /boot/config.txt
```

### apache server

```sh
sudo systemctl enable httpd.service
sudo systemctl start httpd
```

### git server

```sh
sudo mkdir -p /srv/git
sudo gpasswd -a alarm http
sudo chown -R http:http /srv/git/
```

### git apache config

```sh
echo 'LoadModule cgi_module modules/mod_cgi.so' | sudo tee -a /etc/httpd/conf/httpd.conf
#echo 'LoadModule env_module modules/mod_env.so' | sudo tee -a /etc/httpd/conf/httpd.conf
#echo 'LoadModule alias_module modules/mod_alias.so' | sudo tee -a /etc/httpd/conf/httpd.conf

echo '
<Directory "/usr/lib/git-core*">
   Options ExecCGI Indexes
   Order allow,deny
   Allow from all
   Require all granted
</Directory>

<LocationMatch "^/.*/git-receive-pack$">
    Options +ExecCGI
    Require all granted
</LocationMatch>

<LocationMatch "^/.*/git-upload-pack$">
    Options +ExecCGI
    Require all granted
</LocationMatch>

SetEnv GIT_PROJECT_ROOT /srv/git
SetEnv GIT_HTTP_EXPORT_ALL
ScriptAlias /git/ /usr/lib/git-core/git-http-backend/
' | sudo tee -a /etc/httpd/conf/httpd.conf
```

### gitweb interface

```sh
echo '
Alias /gitweb "/usr/share/gitweb"
<Directory "/usr/share/gitweb">
    DirectoryIndex gitweb.cgi
    Options ExecCGI
    Require all granted
    <Files gitweb.cgi>
        SetHandler cgi-script
    </Files>
    SetEnv  GITWEB_CONFIG  /etc/gitweb.conf
</Directory>' | sudo tee /etc/httpd/conf/extra/gitweb.conf

echo 'Include conf/extra/gitweb.conf' | sudo tee -a /etc/httpd/conf/httpd.conf
```

```sh
export IPNUMBER='10.124.5.150'

echo "our \$projectroot = \"/srv/git\";" | sudo tee /etc/gitweb.conf
echo "\$feature{'blame'}{'default'} = [1];" | sudo tee -a /etc/gitweb.conf
echo "\$feature{'highlight'}{'default'} = [1];" | sudo tee -a /etc/gitweb.conf
```

### git authentication (optional)

```sh
cd /srv/git
htpasswd -c htpasswd-git gitserv

echo '
<Location /git/>
        AuthName "Restricted Git"
        AuthType Basic
        AuthUserFile /srv/git/htpasswd-git
        <If "%{QUERY_STRING} =~ m#service=git-receive-pack# || %{REQUEST_URI} =~ m#/git-receive-pack$#">
                Require valid-user
        </If>
        Satisfy all
</Location>
' | sudo tee -a /etc/httpd/conf/httpd.conf
```

### Reboot

```sh
sudo reboot
```

## Test on Webrowser

```sh
vimb http://10.124.4.150/gitweb
```

## Create Repository

```sh
cd /srv/git
sudo -u http git --bare init projectTes.git/
sudo chown -R http:http /srv/git/projectTes.git/

cd projectTes.git/
echo "GitServer Test" | sudo -u http tee description
sudo -u http git config --file config http.receivepack true
```

## Git Client Workflow

### git clone-push

```sh
git clone http://10.124.4.150/git/projectTes.git
cd projectTes/

echo "test gitserver" > tes.txt
git add .
git commit -m "initial commit"
git push origin master
```

### git add remote

```sh
git remote add gitlocal http://10.124.4.150/git/projectTes.git
git remote -v

git branch
git push gitlocal master
```

-------------------------------------------------

## Gitea Setup

### login SSH

```sh
ssh -Y alarm@10.3.49.199
```

### database setup

#### simpler database (MySQL)

##### initialize database

```sh
sudo chown -R mysql /var/lib/mysql
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

sudo systemctl enable mysqld
sudo systemctl start mysqld
```

##### create gitea database

```sh
sudo mariadb -u root

CREATE DATABASE `gitea` DEFAULT CHARACTER SET `utf8mb4` COLLATE `utf8mb4_unicode_ci`;
CREATE USER `gitea`@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON `gitea`.* TO `gitea`@`localhost`;
FLUSH PRIVILEGES;

exit
```

```sh
mariadb -u gitea -e "SHOW DATABASES;"

mariadb -u gitea -D gitea
exit
```

#### initial config

```sh
echo "DB_TYPE  = mysql
HOST = /var/run/mysqld/mysqld.sock
NAME = gitea
USER = gitea
PASSWD =
HTTP_ADDR = 0.0.0.0
HTTP_PORT = 3000
DISABLE_SSH = true
" | sudo tee /etc/gitea/app.ini
```

#### recommended database (PostgreSQL)

Notes: Ignore all **could not change directory to "/home/alarm": Permission denied**

##### initialize database

```sh
sudo chown -R postgres /var/lib/postgres/data/
sudo -u postgres initdb --locale en_US.UTF-8 -D /var/lib/postgres/data

sudo systemctl enable postgresql
sudo systemctl start postgresql
```

##### create gitea database

```sh
sudo -u postgres psql -c "alter user postgres with password ''"
sudo -u postgres createuser gitea
sudo -u postgres createdb -O gitea gitea

echo "local gitea gitea peer
" sudo tee /var/lib/postgres/data/pg_hba.conf
sudo systemctl restart postgresql
```

```sh
sudo -u postgres psql -c "\l"

sudo -u postgres psql --dbname=gitea --username=gitea
exit
```

#### initial config

```sh
echo "DB_TYPE = postgres
HOST = /run/postgresql/
NAME = gitea
USER = gitea
PASSWD =
HTTP_ADDR = 0.0.0.0
HTTP_PORT = 3000
DISABLE_SSH = true
" | sudo tee /etc/gitea/app.ini
```

### run Gitea

#### run service

```sh
sudo systemctl enable gitea
sudo systemctl start gitea
```

#### completing installation

```sh
# make sure database type is correct
vimb http://10.3.49.199:3000/
```

#### repository URL pattern

```txt
# repository example
http://10.3.49.199:3000/mekatronikachmadi/archlinuxmate.git

# user profile repository
http://10.3.49.199:3000/mekatronikachmadi/.profile
```

#### final settings

```sh
# app config
sudo bat /etc/gitea/app.ini

# repositories path
sudo ls -l /var/lib/gitea/data/gitea-repositories
```

#### recreate database

```sh
#MySQL
sudo mariadb -u root

DROP DATABASE gitea;
CREATE DATABASE `gitea` DEFAULT CHARACTER SET `utf8mb4` COLLATE `utf8mb4_unicode_ci`;
FLUSH PRIVILEGES;

exit
```

```sh
# PostgreSQL
sudo -u postgres dropdb -U gitea gitea
sudo -u postgres createdb -O gitea gitea
```

#### adopt existing repositories

```txt
Account -> Site Administration -> Code Assets -> Repositories

Unadopted Repositories -> Search -> Adopt Files
```
