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

# reload group without relogin
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

Run command

```sh
docker run -it debian bash -c "echo hello world"
```

Enter shell

```sh
docker run -it debian bash
```

and to exit

```sh
exit
```
