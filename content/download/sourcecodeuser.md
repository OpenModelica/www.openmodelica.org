---
title: "Source Code"
aliases: ["/developersresources/source-code", "/free-and-open-source-software/bugs"]
---

Source code can be fetched from <a href="https://github.com/OpenModelica/OpenModelica" style="line-height: 1.8;">https://github.com/OpenModelica/OpenModelica</a> or the OpenModelica <a href="https://openmodelica.org/git-readonly/OpenModelica.git">read-only mirror</a>.
Instructions on how to set up the GIT repository and how to compile from sources are available <a href="https://github.com/OpenModelica/OpenModelica/blob/master/README.md">here</a>.

Development of OpenModelica takes place on the master branch.
The preferred way to contribute is via pull requests, that are only accepted if they don't cause regressions in the testsuite.
For more information on contributing, see <a href="https://github.com/OpenModelica/OpenModelica/blob/master/CONTRIBUTING.md">here</a>.

During development, nightly builds for <a href="https://build.openmodelica.org/omc/builds/windows/nightly-builds/">Windows</a> and <a href="/download/download-linux">Linux</a> are made available daily, marked x.y.z-dev-xxx.
Stable development releases, marked x.y.z.-dev.xx may be branched off once or twice in-between official releases, to make bug fixes available in a more stable way than with the nightly builds.
At the beginning of the official release process, a stable beta release marked x.y.z.-dev-beta1 is branched off master for testing, while the development of the next release starts on the master branch.
Only bug fixes are added to the beta branch, possibly with more beta releases marked x.y.z.-dev-betaxx, until the official release is finally issued.
If critical issues are found after an official release x.y.0, bug fixes can be applied to the maintenance branch, eventually issuing one or more maintenance releases x.y.z.

## Nightly-Builds

We provide experimental nightly builds for <a href="http://build.openmodelica.org/omc/builds/windows/">Windows </a>and&nbsp;<a href="/download/download-linux">Linux</a> between releases.
You can use the nightly build to get the latest developments and help testing them and reporting bugs.
You can also use them to access the latest bug fixes, that have not yet been included in a stable release.

## Explore

* <a href="http://build.openmodelica.org/omc/builds/">The Directory Structure</a> which contains nightly builds or older releases.

## Reporting bugs

Reporting of bugs can be made through <a href="{{< param "bugreporting" >}}">GitHub</a>.
