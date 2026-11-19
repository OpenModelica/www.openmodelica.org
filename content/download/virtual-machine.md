---
title: "Download Virtual Machines"
donate: true
---

For faster installation on operating systems where there is no pre-built binary (RPM-based Linux releases, older OSX releases, or if you are unable to install the latest XCode on OSX), it is possible to install OpenModelica on a virtual machine.
We provide a [pre-built VM](https://build.openmodelica.org/omc/builds/virtual_machines/) that contains all libraries and clients that come with OpenModelica.
You will need a virtualization engine such as [VirtualBox](https://virtualbox.org) to run the virtual machine (remember to edit the machine settings to add more CPU cores than the default of 1, but allocate fewer than the number of physical processors in the machine to make everything feel smooth).

The VM version uses (x86) 64-bit Linux, which means it can be used to run OMNotebook on OSX machines (where OMNotebook is normally not available).
The "openmodelica" user has password "openmodelica".
