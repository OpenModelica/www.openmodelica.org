---
title: "Source Code"
---

Source code can be fetched from:
 - GitHub repository: <https://github.com/OpenModelica/OpenModelica>
 - OpenModelica read-only mirror: <https://openmodelica.org/git-readonly/OpenModelica.git>

Instructions on how to set up the Git repository and how to compile from sources are available in the [GitHub repository's README.md](https://github.com/OpenModelica/OpenModelica/blob/master/README.md).

Development of OpenModelica takes place on the master branch.
The preferred way to contribute is via pull requests, that are only accepted if they don't cause regressions in the testsuite.
For more information on contributing, see the [GitHub repository's CONTRIBUTING.md](https://github.com/OpenModelica/OpenModelica/blob/master/CONTRIBUTING.md).

During development:
 - Nightly builds for Windows and Linux are made available daily marked `x.y.z~dev-xxx`.
 - Stable development releases  may be branched off once or twice in-between official releases, to make bug fixes available in a more stable way than with the nightly builds.
 - At the beginning of the official release process, a stable beta release marked `x.y.z-dev.beta.1` is branched off *master* for testing, while the development of the next release starts on the *master* branch.
 - Only bug fixes are added to the *beta* branch, possibly with more beta releases marked `x.y.z-dev.beta.xx`, until the official release is finally issued.
 - If critical issues are found after an official release `x.y.0`, bug fixes can be applied to the maintenance branch, eventually issuing one or more maintenance releases `x.y.z`.

## Nightly-Builds

We provide experimental nightly builds for Windows (see [Download &rarr; Windows](/download/download-windows)) and Linux (see [Download &rarr; Linux](/download/download-linux)) between releases.
You can use the nightly build to get the latest developments and help testing them and reporting bugs.
You can also use them to access the latest bug fixes, that have not yet been included in a stable release.

### Status of Nightly Builds
 - [Pipeline of LINUX_BUILDS](https://test.openmodelica.org/jenkins/job/LINUX_BUILDS/)

## Explore

* <a href="http://build.openmodelica.org/omc/builds/">The Directory Structure</a> which contains nightly builds or older releases.

## Reporting bugs

Reporting of bugs can be made through <a href="{{< param "bugreporting" >}}">GitHub</a>.
