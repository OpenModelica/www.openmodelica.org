---
title: "Download Docker (All OS)"
---

Docker is a lightweight alternative to virtual machines.

We have images available for the major CPU architectures: amd64, arm64, and armv7 at [docker hub](https://hub.docker.com/r/openmodelica/openmodelica/tags).

The images have 3 variants:

* `openmodelica/openmodelica:v{{< param "current_version.release" >}}-minimal` contains everything necessary to start command-line `omc`.
* `openmodelica/openmodelica:v{{< param "current_version.release" >}}-ompython` contains everything in minimal and also has the Python package OMPython installed.
* `openmodelica/openmodelica:v{{< param "current_version.release" >}}-gui` contains everything in the ompython package and also contains all graphical clients such as `OMEdit`.

The images do not come with Modelica libraries installed.
These are installed in your home directory which can be forwarded to docker and kept between sessions.

Note that you can customize docker images to your own liking, either basing them on the above images or using the same [Dockerfiles](https://github.com/OpenModelica/OpenModelicaDockerImages/tree/v{{< param "current_version.release" >}}) we used to create them.

## OpenModelica in your web browser {#web}

This setup runs a Linux desktop in one container and OpenModelica in another container.
You use them in your web browser, so you do not need an X server.
It works the same on Linux, macOS and Windows (in a WSL terminal), on amd64 and arm64.

The desktop is the [Webtop](https://docs.linuxserver.io/images/docker-webtop/) image from LinuxServer.io, with the Xfce desktop.
OpenModelica runs from the `-gui` image and shows its windows on that desktop.

You need Docker Compose 2.17 or newer.
Docker Desktop includes it.

Make an empty directory and save this file as `compose.yaml` in it:

```yaml
name: openmodelica

services:
  desktop:
    image: lscr.io/linuxserver/webtop:debian-xfce
    restart: unless-stopped
    ipc: shareable
    environment:
      PUID: ${UID:-1000}
      PGID: ${GID:-1000}
    ports:
      - 127.0.0.1:3000:3000
    shm_size: 1gb
    volumes:
      - desktop:/config
      - ${HOME}:${HOME}
    healthcheck:
      test: [CMD, test, -S, /tmp/.X11-unix/X1]
      interval: 5s

  openmodelica:
    image: openmodelica/openmodelica:v{{< param "current_version.release" >}}-gui
    restart: unless-stopped
    init: true
    network_mode: service:desktop
    ipc: service:desktop
    depends_on:
      desktop:
        condition: service_healthy
    user: ${UID:-1000}:${GID:-1000}
    environment:
      DISPLAY: ":1"
      HOME: ${HOME}
    working_dir: ${HOME}
    volumes:
      - ${HOME}:${HOME}
    command:
      - sh
      - -c
      - |
        while :; do OMEdit; sleep 1; done &
        while :; do x-terminal-emulator -e bash; sleep 1; done

volumes:
  desktop:
```

Then run these commands in that directory:

```bash
printf 'UID=%s\nGID=%s\n' "$(id -u)" "$(id -g)" > .env
docker compose up -d
```

Open <http://localhost:3000> in your web browser.

The containers use your user ID, and your home directory has the same path as on your computer.
The files that you save and the libraries that you install stay in your home directory between sessions.

OMEdit and a terminal open on the desktop.
If you close one of them, it opens again.
In the terminal, you can run `omc`, `python3` with OMPython, and the other tools, for example `OMNotebook &`.
If you close the terminal, the programs that you started from it close too.

To stop everything, use `docker compose down`.

The desktop has no password, and its own Xfce terminal can use `sudo`.
For this reason, it is only available on your own computer (`127.0.0.1`).
To use it on a remote server, connect with `ssh -L 3000:localhost:3000 server` and open <http://localhost:3000> on your computer.

## X11 forwarding {#x11}

The graphical clients can also show their windows directly on your own desktop.
This needs X forwarding, which works differently for each OS (see below).
Once the instructions below have been followed: from the terminal you can run the alias

```zsh
docker-om
```

without arguments, which gives you a Linux terminal.
You can start `OMEdit` from that terminal or run if you prefer, you can launch `OMEdit` directly using:

```zsh
docker-om OMEdit
```

### MacOS

Pre-requisities:

* [XQuartz](https://www.xquartz.org/) needs to be installed and running.
  Network connections need to be allowed in the settings.
* [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/) needs to be installed and running.

The following code when executed will add an alias to make launching OpenModelica easier.

```zsh
echo $'alias docker-om=\'docker run -it --rm -v "$HOME:$HOME" -e "HOME=$HOME" -w "$PWD" -e "DISPLAY=`ifconfig | grep -o "inet [0-9.]*" | grep -Eo "[0-9.]{7,}" | grep -Fv 127.0.0.1 | head -1`:0" --user $UID openmodelica/openmodelica:v{{< param "current_version.release" >}}-gui\'' >> "$HOME/.zshrc"
```

What it does is create a command `docker-om` which will run a the given docker container and mount your home directory inside the docker container, set the X11 DISPLAY variable so graphical clients can connect (optional for the command-line `omc`), set the UNIX user ID to your own user so files in your home directory are still owned by you.

### Linux

Install either [Docker Desktop](https://docs.docker.com/desktop/install/linux-install/) or the docker client that comes with your Linux distribution.

The following code when executed will add an alias to make launching OpenModelica easier.
The alias will be activated after the next login.

```zsh
echo $'alias docker-om=\'docker run -it --rm -v "$HOME:$HOME" -e "HOME=$HOME" -w "$PWD" -e "DISPLAY=$DISPLAY" --user $UID openmodelica/openmodelica:v{{< param "current_version.release" >}}-gui\'' >> "$HOME/.profile"
```

What it does is create a command `docker-om` which will run a the given docker container and mount your home directory inside the docker container, set the network to the host adapter and the X11 DISPLAY variable so graphical clients can connect (optional for the command-line `omc`), set the UNIX user ID to your own user so files in your home directory are still owned by you.

### Windows (WSL)

On Windows, install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/) using the WSL 2 backend.

Then in your WSL terminal, follow the instructions for Linux with the following modifications:

* Windows 11: none
* Windows 10: Install an X11 server such as [XMing](https://sourceforge.net/projects/xming/), start it in multi-window mode and disable access control before starting `OMEdit`.
