---
title: "Download Linux"
donate: true
toc: true
---

Official Release
: * contains only validated new features
  * intended for productive usage
  * latest official release **<span id="omc-version-release">{{< param "current_version.release" >}}</span>** (<a href="https://github.com/OpenModelica/OpenModelica/commits/{{< param "current_branch.release" >}}">commit history</a>) (<a href="https://github.com/OpenModelica/OpenModelica/releases/tag/v{{< param "current_version.release" >}}">release notes</a>)

Stable Development
: * dev.xx versions are released during development when the performance is sufficiently stable; they contain bug fixes and some new features that still need to be validated
  * dev.beta.xx versions are released in preparation to official releases for testing; no new features are added to beta versions, only bug fixes
  * latest stable release: **<span id="omc-version-stable">{{< param "current_version.stable" >}}** (<a href="https://github.com/OpenModelica/OpenModelica/commits/{{< param "current_branch.stable" >}}">commit history</a>) (<a href="https://github.com/OpenModelica/OpenModelica/releases/tag/v{{< param "current_version.stable" >}}">release notes</a>)

Nightly Build
: * built daily with the latest additions to the code base that pass the standard regression tests (<a href="https://github.com/OpenModelica/OpenModelica/commits/{{< param "current_branch.nightly" >}}">commit history</a>)
  * intended to make the latest developments and enhancements available for testers and developers, not for productive usage
  * features that are not subject to regression testing may get broken between one nightly build and the next
  * current nightly builds **<span id="omc-version-nightly">{{< param "current_version.nightly" >}}**

## Debian / Ubuntu Packages

<script>
var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
  var status = xhr.status;
  if (status === 200) {
    callback(null, xhr.response);
  } else {
    callback(status, xhr.response);
  }
  };
  xhr.send();
};
var omLinuxAPIData;
function escapeHtml(unsafe)
{
  return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/\\/g, "&bsol;")
         .replace(/'/g, "&#039;");
}
var selectedDebArch = function() {
  var archSelect = document.getElementById("deb-arch-select");
  document.getElementById("deb-arch").innerHTML = archSelect.value;
  var codenameSelect = ['<option value="$('+escapeHtml('cat /etc/os-release | grep "\\(UBUNTU\\\\|DEBIAN\\\\|VERSION\\)_CODENAME" | sort | cut -d= -f 2 | head -1')+')" selected>(auto)</option>'];
  var value = archSelect.value;
  if (value.startsWith("$")) {
    value = "amd64";
  }
  codenameSelect = codenameSelect.concat(omLinuxAPIData.deb[value].map(key => '<option value="'+key+'">'+key+'</option>'));
  document.getElementById("deb-codename-select").innerHTML=codenameSelect.join("\n");
  selectedDebCodename();
};
var selectedRpmArch = function() {
  var archSelect = document.getElementById("rpm-arch-select");
  var codenameSelect = [];
  var value = archSelect.value;
  codenameSelect = codenameSelect.concat(Object.keys(omLinuxAPIData.rpm[value]).reverse().map(key => '<option value="'+key+'">'+key+'</option>'));
  document.getElementById("rpm-codename-select").innerHTML=codenameSelect.join("\n");
  selectedRpmCodename();
};
var detectedArch = function(debArch) {
  var debArchSelect = ['<option value="$(dpkg --print-architecture)">(auto)</option>'];
  debArchSelect = debArchSelect.concat(Object.keys(omLinuxAPIData.deb).map(function (key) {
    return '<option value="'+key+(key==debArch ? '" selected' : '"')+'>'+key+'</option>'
  }));
  var rpmArchSelect = [];
  rpmArchSelect = rpmArchSelect.concat(Object.keys(omLinuxAPIData.rpm).map(function (key) {
    return '<option value="'+key+(key==debArch ? '" selected' : '"')+'>'+key+'</option>'
  }));
  document.getElementById("deb-arch-select").innerHTML=debArchSelect.join("\n");
  document.getElementById("rpm-arch-select").innerHTML=rpmArchSelect.join("\n");
  selectedDebArch();
  selectedRpmArch();
}
var selectedDebCodename = function() {
  var codenameSelect = document.getElementById("deb-codename-select");
  document.getElementById("deb-codename").innerHTML=codenameSelect.value;
};
var selectedRpmCodename = function() {
  var codeNameValue=document.getElementById("rpm-codename-select").value;
  var addRepoCommand=(codeNameValue=="fc41" ? "addrepo --from-repofile=" : "--add-repo ");
  document.getElementById("rpm-os").innerHTML=codeNameValue;
  document.getElementById("rpm-os-add-repo-command").innerHTML=addRepoCommand;
  var codenameSelect = [];
  var archValue = document.getElementById("rpm-arch-select").value;
  var collator = new Intl.Collator(undefined, {numeric: true, sensitivity: 'base'});
  var branches = omLinuxAPIData.rpm[archValue][codeNameValue].sort(collator.compare).reverse();
  codenameSelect = codenameSelect.concat(branches.map(key => '<option value="'+key+'">'+key+'</option>'));
  var specifics = document.getElementById(codeNameValue+"-specifics");
  document.getElementById("el-specifics-container").innerHTML=specifics ? specifics.innerHTML : "";
  document.getElementById("rpm-branch-select").innerHTML=codenameSelect.join("\n");
  selectedRpmBranch();
};
var selectedBranch = function() {
  var branchSelect = document.getElementById("deb-branch-select");
  document.getElementById("deb-branch").innerHTML=branchSelect.value;
}
var selectedRpmBranch = function() {
  var branchSelect = document.getElementById("rpm-branch-select");
  document.getElementById("rpm-branch").innerHTML=branchSelect.value;
}
getJSON('/api/linux.json', function(err, data) {
  omLinuxAPIData = data;
  var debOSNames = "";
  if (err !== null) {
    debOSNames = "Failed to load list of OSes: " + err;
  } else {
    debOSNames = omLinuxAPIData["deb"]["amd64"].join(", ");
    try {
      var arch = navigator.userAgentData.getHighEntropyValues([ "architecture", "bitness" ]);
      arch.then(function (arch) {
        console.log(arch);
        var debArch = "amd64";
        if (arch.architecture == 'x86') {
          if (arch.bitness == 64) {
            debArch = "amd64";
          }
          if (arch.bitness == 32) {
            debArch = "i386";
          }
        } else if (arch.architecture == 'arm') {
          if (arch.bitness == 64) {
            debArch = "arm64";
          }
          if (arch.bitness == 32) {
            debArch = "armhf";
          }
        }
        detectedArch(debArch);
      });
    } catch (error) {
      console.error(error);
      detectedArch("amd64");
    }
  }
  document.getElementById("debian-os-names").innerHTML=debOSNames;
  document.getElementById("omc-version-release").innerHTML=omLinuxAPIData.version.release;
  document.getElementById("omc-version-stable").innerHTML=omLinuxAPIData.version.stable;
  document.getElementById("omc-version-nightly").innerHTML=omLinuxAPIData.version.nightly;
});
</script>

<p><img style="vertical-align: baseline;" src="/images/ubuntu-logo.gif" alt="" width="80" height="80" border="0" /><img style="vertical-align: baseline;" src="/images/debian_splash.png" alt="" width="80" height="80" border="0" /></p>

We provide .deb packages for the following Debian and Ubuntu versions:
<span id="debian-os-names">LTS versions of both and non-LTS versions of the latest Ubuntu (x86, amd64, and armv7). You can also check the <a href="https://build.openmodelica.org/apt/dists/">full list including latest update</a></span>.

Source packages are also provided if your distribution is too old (or still not released yet) for the binary packages. Older distributions may not have all build dependencies used by omc, but can still be built. Some older distributions still have binary packages, but are no longer maintained. Note that armhf packages are only available for more recent versions of Ubuntu (and not Debian at all).

Use the following lines in a shell to update your packages and install the certificate signing the OpenModelica packages:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
curl -fsSL https://build.openmodelica.org/apt/openmodelica.asc | \
  sudo gpg --dearmor -o /usr/share/keyrings/openmodelica-keyring.gpg
```

Then update your sources.list using the lines below.
Choose your CPU architecture, OS and preferred release branch to follow.
If you are unsure, select the auto options and the **stable** release branch.
If your OS is not in the list, it is probably outdated and you might be able install an older version using the auto option, or it is a recent Debian/Ubuntu release not yet on the list (contact us to get it added once there is a release candidate for the OS), or you are running Mint Linux (use the corresponding Debian/Ubuntu upstream release; check /etc/os-release to see which one or use the auto option).

CPU architecture <select label="CPU architecture" id="deb-arch-select" onChange="selectedDebArch()"></select>
OS <select id="deb-codename-select" onChange="selectedDebCodename()"></select>
Release branch <select id="deb-branch-select" onChange="selectedBranch()">
  <option value="release">release</option>
  <option value="stable" selected>stable</option>
  <option value="nightly">nightly</option>
</select>


<div class="highlight"><pre tabindex="0" class="chroma">
<code>echo "deb [arch=<span id="deb-arch">$(dpkg --print-architecture)</span> signed-by=/usr/share/keyrings/openmodelica-keyring.gpg] \
  https://build.openmodelica.org/apt \
  <span id="deb-codename">$(cat /etc/os-release | grep "\(UBUNTU\\|DEBIAN\\|VERSION\)_CODENAME" | sort | cut -d= -f 2 | head -1)</span> \
  <span id="deb-branch">stable</span>" | sudo tee /etc/apt/sources.list.d/openmodelica.list</code>
</pre></div>


Then update and install OpenModelica:

```bash
sudo apt update
sudo apt install openmodelica
```

For a smaller installation without graphical clients:

```bash
sudo apt install --no-install-recommends omc
```

### Modelica libraries

There is a package manager for Modelica libraries built into the scripting interface and the OMEdit graphical user interface. See the [documentation](/doc/OpenModelicaUsersGuide/latest/packagemanager.html) for details.

#### Offline Installation

If you install OpenModelica from a USB stick in a place without Internet access, for example during a tutorial at a conference, it is still possible to install the Modelica Standard Library.


```bash
sudo apt install omlibrary
```

This installs cached versions of the Modelica Standard library to the system directory.
These libraries will be automatically installed by the package manager in the user's .openmodelica directory as soon as any OpenModelica tool tries to load any system library for the first time, e.g. when starting OMEdit.

### C++ runtime

The C++ runtime is an alternative to the default C runtime. To install the C++ runtime run this command:

```bash
sudo apt install libomccpp
```

### Older Releases

Older releases are stored for some stable Debian/Ubuntu versions along with the libraries that existed at the time of the release.
You can find the releases at https://build.openmodelica.org/omc/builds/linux/releases.

Starting with OpenModelica 1.9.4 you can use apt to download the packages using a deb-line such as the one below; make sure all existing OpenModelica packages have been uninstalled (so you do not end up with mismatching versions of dependencies):

```text
deb https://build.openmodelica.org/omc/builds/linux/releases/1.13.0/ bionic release
```

## RPM packages

<p><img style="vertical-align: baseline;" src="/images/rpm-package.png" alt="" width="80" height="80" border="0" /></p>

To add the OpenModelica yum/dnf repository to your system, choose your OS below and run the command(s):

CPU architecture <select label="CPU architecture" id="rpm-arch-select" onChange="selectedRpmArch()"></select>
OS <select id="rpm-codename-select" onChange="selectedRpmCodename()"></select>
Release branch <select id="rpm-branch-select" onChange="selectedRpmBranch()">
</select>

<noscript id="el7-specifics">

```bash
yum install centos-release-scl-rh
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

</noscript>
<noscript id="el8-specifics">

AlmaLinux 8:

```bash
dnf install epel-release
dnf config-manager --set-enabled powertools
```

RHEL 8 (see [#10292](https://github.com/OpenModelica/OpenModelica/issues/10292) for details; postgis30_12 might fail to install):

```bash
subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
dnf install postgis30_12
```

Then for both:

</noscript>
<noscript id="el9-specifics">

```bash
dnf install epel-release
dnf config-manager --set-enabled crb
```

</noscript>

<div id="el-specifics-container"></div>

<div class="highlight"><pre tabindex="0" class="chroma">
<code>dnf config-manager <span id="rpm-os-add-repo-command">ENTER-RPM-ADD-REPO-COMMAND-HERE</span>https://build.openmodelica.org/rpm/<span id="rpm-os">ENTER-RPM-OS-VERSION-HERE</span>/omc.repo</code>
</pre></div>

Once the repository has been enabled in the OS, install OpenModelica:

<div class="highlight"><pre tabindex="0" class="chroma">
<code>dnf install <span id="rpm-branch">openmodelica-nightly</span></code>
</pre></div>

It is possible to install multiple version of OpenModelica (although this use-case has mostly been replaced by using docker).
You can then select which version /usr/bin/omc (and OMEdit, etc) should point to:

```bash
alternatives --config openmodelica
```

You can also use commands like `omc-{{< param current_version.release >}}` or `/opt/openmodelica-{{< param current_version.release >}}/bin/omc` directly if you want to try other OpenModelica versions.

To install libraries, see [above](#modelica-libraries).

## Source Code

If you can't use deb packages at all, we recommended installing OpenModelica from <a href="/developersresources/sourcecode">source code</a>.
