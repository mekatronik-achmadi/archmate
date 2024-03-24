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

sudo systemctl start docker
```

