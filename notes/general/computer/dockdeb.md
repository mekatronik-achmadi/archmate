# Debian in Docker

## Setup Docker

### Install Docker engine

```sh
sudo pacman -S docker docker-compose
```

### User/Group Settings

```sh
sudo groupadd -f docker
sudo gpasswd -a $USER docker

newgrp docker

sudo systemctl enable docker.service
sudo systemctl start docker.service
```

### Change Docker Path

```sh
sudo systemctl stop docker

mkdir -p ~/Dockers/
sudo chown -R root:root ~/Dockers/
sudo rsync -aP /var/lib/docker/ ~/Dockers/

sudo mkdir -p /etc/docker/
jq -n '
."data-root"="~/Dockers/"
' | sudo tee /etc/docker/daemon.json

sudo systemctl restart docker
```

### Checking

```sh
docker infodock
```

## Debian Images

### List Installed

```sh
docker image ls
docker images
```

### Install Images

```sh
docker pull debian
```

### Inspect Images

```sh
docker image inspect debian | bat
```

### Run Images

#### Run single command

Run command in new instance

```sh
docker run -it debian bash -c "echo hello world"
````

Run command in a already run instance

```sh
docker exec -it $(docker ps -q) bash -c "echo hello world"
```

#### Run Shell

Enter shell

```sh
docker run -it debian bash
#docker exec -it $(docker ps -q) bash
```

and to exit

```sh
exit
```

## Image Remove

### Stop All Images

```sh
docker stop $(sudo docker ps -q)
docker kill $(sudo docker ps -q)
```

### Remove an Image

```sh
docker rm debian
```

### Remove all Images

```sh
docker system prune -a
```

## Debian Packages

### Enter Shell

```sh
docker run -it debian bash
```

### Directory Paths

#### APT Configurations

- Config File: **/etc/apt/apt.conf**
- Config Folder: **/etc/apt/apt.conf.d/**

#### Server List

- ServerList File: **/etc/apt/sources.list**
- ServerList Folder: **/etc/apt/sources.list.d/**

#### Cache Folders

- Databases: **/var/lib/apt/lists/**
- Packages: **/var/cache/apt/archives/**

### Update List from server

```sh
sudo apt-get update
```

### Install from Server

#### Search Package

```sh
apt-cache search vim less
```

#### Check Package

```sh
apt-cache show vim less
```

#### Install Package

```sh
sudo apt-get install vim less
```

### Manage Installed Packages

#### Search Installed

```sh
dpkg -l | grep vim | less
```

#### Check Package

```sh
dpkg -s vim | less
```

#### Check Installed Files

```sh
dpkg -L vim | less
```

#### Check Owned Files

```sh
dpkg -S /usr/bin/vim.basic
```

### Install local Files

#### Get Package URLs

```sh
apt-get -y install --print-uris vim | cut -f 2 -d \' | grep \.deb
````

#### Get Installed Package URLs

```sh
apt-get -y install --print-uris --reinstall vim | cut -f 2 -d \' | grep \.deb
```

#### Install locally without APT

```sh
sudo dpkg -i vim_9.0.1378-2_amd64.deb
```

### Remove Packages

#### Remove single Package

```sh
sudo apt-get remove vim
```

#### Remove Package and its configurations

```sh
sudo apt-get purge vim
```

#### Remove unused/orphaned packages

```sh
sudo apt-get autoremove
```

### Clean Cache

#### Clean Old/Unused Packages

```sh
sudo apt-get autoclean
```

#### Clean All Packages

```sh
sudo apt-get clean
```

### Upgrade Packages

**NOTE:** Not Recommended in many cases.

```sh
sudo apt-get dist-upgrade
sudo apt-get upgrade
```

## Docker Compose

### Stop Running Images

```sh
docker-compose down
```

### Configuration example

#### Dockerfile

Coming Soon

#### docker-compose.yml

Coming Soon

### Run Images

#### Build

```sh
docker-compose up --build
```

#### Daemonize

```sh
docker-compose up -d
```

#### Check Log

```sh
docker-compose logs -f
```
