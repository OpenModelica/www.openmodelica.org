---
title: "Download Mac"
---

## Experimental build

There is a new experimental build of OpenModelica for macOS 13 (Ventura) or newer. It is a universal build that runs on Apple Silicon and Intel Macs.

 - download **[OpenModelica-latest-macos-universal.dmg](https://build.openmodelica.org/omc/rust/latest/OpenModelica-latest-macos-universal.dmg)** ([all experimental builds](https://build.openmodelica.org/omc/rust/latest/))
 - built from the latest development version with the new Rust version of the OpenModelica compiler, which is not yet used in the official releases
 - intended for testing, not for productive usage; please [report the bugs]({{< param "bugreporting" >}}) that you find
 - contains only OMEdit (no OMNotebook, OMShell or OMPlot)
 - the omc command-line compiler is inside the application: `/Applications/OMEdit.app/Contents/MacOS/omc`

### Installation

1. Open the .dmg file and drag OMEdit.app to the Applications folder.
2. The package is not signed. Thus macOS does not let you open it after a download (it tells you that the application is damaged or that Apple cannot verify it). To let it run, open the Terminal and remove the quarantine flag that macOS put on the downloaded application:
   ```bash
   xattr -dr com.apple.quarantine /Applications/OMEdit.app
   ```
   Do this again each time you install a new version.
3. To simulate with the default target language (C), you need a C compiler. Install the Xcode command-line tools:
   ```bash
   xcode-select --install
   ```
   Alternatively, set *Tools > Options > Simulation > Target Language* to `wasm-jit`. This target does not use a C compiler.

## Official releases

The official Mac binary builds of OpenModelica were discontinued after version 1.16.
The reason for that is that maintaining the MacOS version of OpenModelica requires much greater effort than the Windows and Linux versions. Newer MacOS versions are often incompatible with older ones, for example requiring new C++ standard library implementation, which is a problem for us because we rely on many open-source libraries and not all of them are readily updated, so we often end up in deadlock situations where we cannot actually compile OpenModelica for newer versions of MacOS.

Considering our limited resources, and the much lower number of downloads of MacOS builds, we had to take this decision, because the MacOS version kept breaking all the time and we simply do not have the resource to keep it fully functional.

## Alternatives

There are several alternatives available to Mac users, each with its own pros and cons.

### Docker

There is a [Linux docker container](/download/docker), which installs fast and easily.
This runs on Apple Silicon and requires XQuartz for the OpenModelica GUI.

### Virtual machine

There is a [pre-built Linux virtual machine](/download/virtual-machine) that installs somewhat fast.
It uses more disk space and is harder to share your home directory than using Docker, but there is no need to install an X server.
It does not run on Apple Silicon (although you could create your own Ubuntu Linux installation and follow the [Linux installation instructions](/download/download-linux)).

### Compiling from source

Starting from version 1.20.0-dev OpenModelica can be compiled again from sources on M1 and x86 Macs.
Follow this <a href="https://github.com/OpenModelica/OpenModelica/blob/master/README.cmake.md#33-macos">howto</a>.

### Old binary release

You can use the old <a href="https://build.openmodelica.org/omc/builds/mac/binaries/">1.16.1 binary release</a>&nbsp;(only x86_64 version available, built on OSX 10.9 nightly, installs into /Applications/MacPorts/ /opt/openmodelica/bin/ and /opt/openmodelica/share/doc/omc/). Note that there is no uninstaller (see&nbsp;<a href="https://guide.macports.org/#installing.macports.uninstalling">MacPorts guide</a>&nbsp;for some hints on what is safe to remove). Also note that make and system headers are not included in this package so you will also need to install&nbsp;<a href="https://developer.apple.com/xcode">XCode3</a>&nbsp;(10.6), which is available for free with a registration, or a later version of&nbsp;<a href="https://developer.apple.com/xcode">XCode</a>&nbsp;(which is available for free from the App store). Remember to install the&nbsp;<a href="https://guide.macports.org/#installing.xcode">XCode command-line tools</a>&nbsp;(recent distributions of XCode do not install them by default). You will also need Java (which might not come preinstalled on your Mac).

You may also need to allow&nbsp;<a href="https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac">unsigned packages</a>&nbsp;to be installed.</p>
<p>Consider however that this version is now starting to be seriously obsolete.</p>

Note: OMNotebook does not work properly on OSX because the qt event system is different on OSX than on Linux/Windows, making the application crash when loading too large notebooks.
