---
title: "Download Docker (All OS)"
---

Docker is a lightweight alternative to virtual machines.

We have images available for the major CPU architectures: amd64, arm64, and armv7 at [docker hub](https://hub.docker.com/r/openmodelica/openmodelica/tags).

The images have 3 variants:

* `openmodelica/openmodelica:{{< param "current_version.release" >}}-minimal` contains everything necessary to start command-line `omc`.
* `openmodelica/openmodelica:{{< param "current_version.release" >}}-ompython` contains everything in minimal and also has the Python package OMPython installed.
* `openmodelica/openmodelica:{{< param "current_version.release" >}}-gui` contains everything in the ompython package and also contains all graphical clients such as `OMEdit`.

The images do not come with Modelica libraries installed.
These are installed in your home directory which can be forwarded to docker and kept between sessions.

Note that you can customize docker images to your own liking, either basing them on the above images or using the same [Dockerfiles](https://github.com/OpenModelica/OpenModelicaDockerImages/tree/v{{< param "current_version.release" >}}) we used to create them.

The graphical clients need X forwarding enabled, which works differently for each OS (see below).
Once the instructions below have been followed: from the terminal you can run the alias
```zsh
docker-om
```
without arguments, which gives you a Linux terminal.
You can start `OMEdit` from that terminal or run if you prefer, you can launch `OMEdit` directly using:
```zsh
docker-om OMEdit
```

## MacOS

Pre-requisities:

* [XQuartz](https://www.xquartz.org/) needs to be installed and running. Network connections need to be allowed in the settings.
* [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/) needs to be installed and running.

The following code when executed will add an alias to make launching OpenModelica easier.

```zsh
echo $'alias docker-om=\'docker run -it --rm -v "$HOME:$HOME" -e "HOME=$HOME" -w "$PWD" -e "DISPLAY=`ifconfig | grep -o "inet [0-9.]*" | grep -Eo "[0-9.]{7,}" | grep -Fv 127.0.0.1 | head -1`:0" --user $UID openmodelica/openmodelica:{{< param "current_version.release" >}}-gui\'' >> "$HOME/.zshrc"
```

What it does is create a command `docker-om` which will run a the given docker container and mount your home directory inside the docker container, set the X11 DISPLAY variable so graphical clients can connect (optional for the command-line `omc`), set the UNIX user ID to your own user so files in your home directory are still owned by you.

## Linux

Install either [Docker Desktop](https://docs.docker.com/desktop/install/linux-install/) or the docker client that comes with your Linux distribution.

The following code when executed will add an alias to make launching OpenModelica easier. The alias will be activated after the next login.

```zsh
echo $'alias docker-om=\'docker run -it --rm -v "$HOME:$HOME" -e "HOME=$HOME" -w "$PWD" -e "DISPLAY=$DISPLAY" --user $UID openmodelica/openmodelica:{{< param "current_version.release" >}}-gui\'' >> "$HOME/.profile"
```

What it does is create a command `docker-om` which will run a the given docker container and mount your home directory inside the docker container, set the network to the host adapter and the X11 DISPLAY variable so graphical clients can connect (optional for the command-line `omc`), set the UNIX user ID to your own user so files in your home directory are still owned by you.

## Windows (WSL)

On Windows, install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/) using the WSL 2 backend.

Then in your WSL terminal, follow the instructions for Linux with the following modifications:

* Windows 11: none
* Windows 10: Install an X11 server such as [XMing](https://sourceforge.net/projects/xming/), start it in multi-window mode and disable access control before starting `OMEdit`.
