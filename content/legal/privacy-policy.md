---
title: "Privacy Policy"
url: "/privacy-policy"
weight: 6
---

_Last updated: 2026-09-17_

## Short version

The OpenModelica tools run on your own computer. We do not operate a cloud
service for them, we have no user accounts, and nothing is reported back to us
in the background. Your models, simulation results and files never pass through
our servers unless you deliberately send them.

There is one way to send them deliberately, and it is worth understanding
before you use it: OMEdit's crash and issue report. It runs only when you ask
it to, but the log files it offers to attach are detailed enough to reconstruct
the model you were working on. [Crash and issue reports in
OMEdit](#crash-and-issue-reports-in-omedit) says exactly what is in them.

When you connect OMEdit to a cloud storage provider such as Google Drive or
Microsoft OneDrive, OMEdit talks to that provider **directly from your
computer**. Nothing is proxied through, copied to, or logged by OpenModelica
servers.

The only personal data we process ourselves is what any web server unavoidably
records when you visit this website or download a file.

## Who we are

This website and the OpenModelica software are published by the **Open Source
Modelica Consortium (OSMC)**, a non-profit organization working in close
collaboration with [Linköping University](https://www.liu.se/), Sweden. OSMC is
the data controller for the processing described here.

You can reach us at **OpenModelica [at] ida.liu.se**. More contact details are
on the [Contact us](/home/contact-us) page.

## The OpenModelica software

This section covers OMEdit, OMC, OMSimulator, OMShell, OMNotebook, OMPython and
the other tools distributed as part of the OpenModelica Environment.

* All modelling, compilation and simulation happens locally on your own
  computer.
* There is no account, no registration and no licence server.
* There is no usage tracking and no analytics, and nothing is sent to us
  automatically — in particular, a crash does not report itself. OMEdit can
  send a crash or issue report, but only after you fill in the dialog and press
  **Send Report**; see [Crash and issue reports in
  OMEdit](#crash-and-issue-reports-in-omedit) below.
* Your models, parameters, simulation results and file names stay on your
  machine unless you deliberately send them somewhere.

Some features do fetch data over the network when you ask them to — for example
installing a Modelica library through the package manager, which downloads an
index and packages from `libraries.openmodelica.org`, or following a
documentation link. Those requests reach our web servers and are recorded in the
server logs described below, exactly like a page visit.

## Crash and issue reports in OMEdit

OMEdit shows a report dialog in two situations: when it has crashed, and when
you choose to report an issue yourself from the Help menu. **Nothing leaves
your computer until you press "Send Report."** Closing the dialog sends
nothing.

If you do send a report, it is uploaded over HTTPS to a server operated by OSMC
and read by OpenModelica developers to work out what went wrong. It is not used
for statistics, not published, and not passed on to anyone else. The legal
basis is your consent, which you give by sending the report.

What a report contains:

* **Your e-mail address**, if you enter one. It is optional — the dialog offers
  to send the report without it — and it is used only to contact you about this
  particular issue.
* **The description you write**, plus a pre-filled line naming your
  OpenModelica version, operating system and processor architecture.
* **Log files, each with its own tick box.** Every file is listed with its full
  path and is ticked by default. Untick one and it is not sent. The files sit
  in your temporary directory, so you can read them first.

Those log files deserve a closer look, because they hold a good deal more than
a stack trace:

* `omeditcommunication.log` — a transcript of every command OMEdit sent to the
  OpenModelica Compiler during the session, and every answer it got back.
  **This is usually enough to reconstruct the model you were working on.**
  Ordinary editing passes model source text to the compiler, so the transcript
  can contain your Modelica code, class and component names, parameter values,
  the paths of the files you opened, and compiler error messages.
* `omeditcommands.mos` — the same commands written out as a replayable script,
  so it carries the same content.
* `openmodelica.stacktrace.OMEdit` — the backtrace of the crashed process:
  function names, addresses, and the paths of the binaries and sources
  involved. This one is mostly about our code, but it can contain paths from
  your machine.

If the session involved something you would rather not share, untick the log
files and describe the problem in the text box instead. A report with only a
backtrace, or only a description, is still useful to us.

## Cloud storage connections in OMEdit

OMEdit can open and save models in a cloud storage account, currently Google
Drive and Microsoft OneDrive, and possibly further providers in the future.

**We are not part of that connection.** OMEdit authenticates with the provider
using OAuth 2.0 and then speaks to the provider's API directly from your
computer. OSMC operates no server in that path and receives no copy of your
files, your file listings, your account identity or your access tokens.

What this means in practice:

* **What OMEdit is allowed to see.** For Google Drive, OMEdit requests only the
  `drive.file` scope, which limits it to files that OMEdit itself created or
  that you explicitly picked. It cannot see the rest of your Drive. For
  OneDrive, OMEdit requests `Files.ReadWrite`, `User.Read` and `offline_access`.
* **Why an account name is shown.** OMEdit asks the provider for the e-mail
  address or display name of the signed-in account, so that you can tell several
  connected accounts apart in the user interface. That name is displayed and
  stored locally only.
* **Where the credentials live.** The OAuth refresh and access tokens are stored
  on your own computer, in a file readable only by your user account (in the
  browser-based version of OMEdit, in the browser's own storage for that site).
  They are never transmitted to us.
* **What is cached.** Files you open from cloud storage are cached locally so
  that OMEdit can work with them; that cache is on your computer.
* **How to disconnect.** Signing the account out in OMEdit deletes the stored
  tokens. You can also revoke OMEdit's access at any time from your provider —
  [Google account permissions](https://myaccount.google.com/permissions) or
  [Microsoft app permissions](https://account.live.com/consent/Manage).

Your use of Google Drive or OneDrive is governed by the privacy policy of that
provider, not by this one.

OpenModelica's use of information received from Google APIs adheres to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements. Because OpenModelica transfers no Google
user data to any server of ours, that data is never used for advertising, sold,
transferred to third parties, or read by humans.

## This website

Like practically every web server, our servers write a log entry for each
request. An entry typically contains your IP address, the date and time, the
requested address, the HTTP status and response size, the referring page and the
browser's user-agent string.

We use those logs for two purposes only:

1. **Download and usage statistics** — how many people fetch a release, which
   pages are read, which platforms are used. These statistics are aggregated and
   contain no individual identification.
2. **Security** — detecting and blocking abuse, intrusion attempts and denial of
   service.

The legal basis is our legitimate interest (Art. 6(1)(f) GDPR) in keeping the
service running, secure, and in knowing how our software is used. Raw log files
are kept only for a limited period and are then aggregated or deleted. Note
that system backups, which may contain log files, are retained longer as part of
ordinary backup routines.

We do not sell, rent or trade this data, and we do not use it to build profiles
or to advertise.

## Cookies, analytics and third-party content

This website sets **no cookies of its own** and uses **no analytics or tracking
service**. There is no consent banner because there is nothing to consent to.

One exception is worth knowing about. A few pages embed videos from YouTube. We
use YouTube's privacy-enhanced mode (`youtube-nocookie.com`), so no tracking
cookie is set unless you actually start a video, but loading such a page does
tell Google your IP address and which page you are on. That processing is
Google's, under [Google's privacy policy](https://policies.google.com/privacy).

## Mailing lists and the forum

* **Mailing lists.** The OpenModelica Interest and Announce
  [mailing lists](/useresresources/mailing-list) are run with Mailman on
  `lists.liu.se`, operated by Linköping University. If you subscribe, your
  e-mail address is stored there for as long as you stay subscribed, and
  messages you send are distributed to subscribers and kept in the list archive.
  You can unsubscribe yourself at any time using the links on that page. Your
  address is not passed on to third parties.
* **Forum.** The [forum](/forum) is a read-only archive of historical
  discussions. It shows the display names and message texts that the authors
  themselves published at the time. No new registrations or posts are accepted.

## Your rights

If we hold personal data about you, EU data protection law gives you the right
to request access to it, to have it corrected or erased, to have its processing
restricted, and to object to processing based on legitimate interest. Write to
**OpenModelica [at] ida.liu.se** and we will help you.

In practice the only data we are likely to hold is server log entries, which we
cannot reliably link to a person; we may therefore be unable to identify your
records without further information from you.

You also have the right to lodge a complaint with a supervisory authority. In
Sweden that is the [Swedish Authority for Privacy Protection (IMY)](https://www.imy.se/).

## Children

OpenModelica is a technical tool for modelling and simulation. It is not
directed at children, and we do not knowingly collect data from them.

## Changes to this policy

We will update this page if our practices change, and the date at the top always
reflects the most recent revision. Substantial changes will also be announced
through the usual OpenModelica channels.

## Contact

Questions about this policy, or about privacy in OpenModelica generally:
**OpenModelica [at] ida.liu.se**.
