---
title: "New GPG key"
date: "2026-01-27T10:00:00+01:00"
conference_end_date: null
rss_ignore: false
tags: ["news"]
---

The GPG key used by OpenModelica to sign **Debian** / **Ubuntu** packages was
updated to a newer and more secure hash algorithm. This means that in order to
install or update OpenModelica users will need to update the key.

---
**_Affected OS:_**

Ubuntu, Debian

---

## New Key

```txt
sec   rsa4096 2026-01-27 [SC]
      5DE86CC050F6623BBA7995B864CE41328E03B30A
uid           [ultimate] OpenModelica Build System <build@openmodelica.org>
ssb   rsa4096 2026-01-27 [E]
```

### Update

Overwrite the old key:

```bash
$ curl -fsSL https://build.openmodelica.org/apt/openmodelica-2026.asc | \
    sudo gpg --dearmor -o /usr/share/keyrings/openmodelica-keyring.gpg
# File '/usr/share/keyrings/openmodelica-keyring.gpg' exists. Overwrite? (y/N)
# y
$ sudo apt-get update
```

## Rationale

If you encounter missing key errors like

```bash
$ sudo apt-get update
[...]
Warning: OpenPGP signature verification failed: https://build.openmodelica.org/apt trixie Release: Sub-process /usr/bin/sqv returned an error code (1), error message is: Missing key 5DE86CC050F6623BBA7995B864CE41328E03B30A, which is needed to verify signature.
Error: The repository 'https://build.openmodelica.org/apt trixie Release' is not signed.
Notice: Updating from such a repository can't be done securely, and is therefore disabled by default.
Notice: See apt-secure(8) manpage for repository creation and user configuration details.
```

or policy warnings like

```bash
$ sudo apt-get update
[...]
W: https://build.openmodelica.org/apt/dists/trixie/Release.gpg: Policy will reject signature within a year, see --audit for details
```

please [update](#update) the OpenModelica gpg key.

The old public GPG key

```txt
pub   rsa2048 2010-06-22 [SC]
      D229 AF1C E5AE D74E 5F59  DF30 3A59 B536 6497 0947
uid                      OpenModelica Build System <build@openmodelica.org>
sub   rsa2048 2010-06-22 [E]
```

used by OpenModelica is using SHA1 as hash algorithm which is not considered
secure. Some operating systems like Debian 13 (trixie) will reject the
OpenModelica package signed with this outdated SHA1 algorithm starting on
2026-02-01.

## Old key

In case the old key is needed, e.g. for older releases of OpenModelica,
it can be found at
[build.openmodelica.org/apt/openmodelica-2010.asc](https://build.openmodelica.org/apt/openmodelica-2010.asc).
