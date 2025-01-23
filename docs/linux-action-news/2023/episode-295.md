# LAN 295: Linux Action News 295

<iframe src="https://player.fireside.fm/v2/DAcK9LdX+9WWDUbTj?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2023-06-01
* Duration: 10 mins 52 secs

## About this episode

How the recent XFS bug was squashed, insights into why Microsoft built their own Linux from scratch, and recent attacks on Archive.org.

## Your hosts
* [Chris Fisher](https://linuxactionnews.com/hosts/chris)
* [Wes Payne](https://linuxactionnews.com/hosts/wes)

## Sponsored by

  * [Linode](http://linode.com/lan): [Sign up using the link on this page and receive a $100 60-day credit towards your new account. ](http://linode.com/lan)
  * [Kolide](https://l.kolide.co/3klbWzr): [Kolide can help you nail third-party audits and internal compliance goals with endpoint security for your entire fleet. ](https://l.kolide.co/3klbWzr)



## Episode links

  * [Those Using The XFS File-System Will Want To Avoid Linux 6.3 For Now](https://www.phoronix.com/news/Linux-6.3-XFS-Metadata-Corrupt "Those Using The XFS File-System Will Want To Avoid Linux 6.3 For Now")
  * [XFS Metadata Corruption On Linux 6.3 Tracked Down To One Missing One-Line Patch](https://www.phoronix.com/news/XFS-Patch-For-Linux-6.3 "XFS Metadata Corruption On Linux 6.3 Tracked Down To One Missing One-Line Patch") — This is a bug fix that we thought just fixed a livelock on stripe aligned filesystems. I'm guessing that in certain circumstances instead of livelocking on repeated failed allocations, it results in a broken mapping being returned to the writeback code and hence misdirecting the writeback IO.
  * [Linux 6.3.5 Released With XFS Metadata Corruption Fix](https://www.phoronix.com/news/Linux-6.3.5-Released "Linux 6.3.5 Released With XFS Metadata Corruption Fix") — Making Linux 6.3.5 a notable point release is that it has back-ported the fix for the XFS metadata corruption bug that was plaguing the Linux 6.3 point releases.
  * [Azure Linux - Microsoft revealed why it did not fork Fedora](https://devclass.com/2023/05/25/azure-linux-released-at-build-where-microsoft-revealed-why-it-did-not-fork-fedora/ "Azure Linux - Microsoft revealed why it did not fork Fedora") — Why did Microsoft create Azure Linux? “We needed a Linux distribution internally,” Perrin said. “We wanted a consistent platform for ourselves.” Now there is “one vendor to support the full AKS stack”.
  * [Plasma 6 is Wayland only - No X11 for Plasma 6](https://pagure.io/fedora-kde/SIG/issue/347 "Plasma 6 is Wayland only - No X11 for Plasma 6") — With Fedora KDE and Kinoite being fully Wayland by default from login (since F38) to desktop (since F34), it's now time to work toward eliminating our dependency on the Xorg server for Plasma 6.0.
  * [Xorg server is deprecated since RHEL 9.0](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/9.0_release_notes/deprecated_functionality#JIRA-RHELPLAN-121048 "Xorg server is deprecated since RHEL 9.0") — The X.org display server is deprecated, and will be removed in a future major RHEL release. The default desktop session is now the Wayland session in most cases.
  * [Fedora 36 Changes: Replace the fbdev drivers with simpledrm and the DRM fbdev emulation layer](https://fedoraproject.org/wiki/Changes/ReplaceFbdevDrivers "Fedora 36 Changes: Replace the fbdev drivers with simpledrm and the DRM fbdev emulation layer") — This change replaces the legacy Linux frame buffer device (fbdev) drivers that are still used in Fedora, with the latest simpledrm driver and the DRM fbdev emulation layer. 
  * [Ubuntu 18.04 LTS end of standard support](https://ubuntu.com//blog/time-to-prepare-for-ubuntu-18-04-lts-end-of-standard-support-on-31-may-2023-options-for-google-cloud-users "Ubuntu 18.04 LTS end of standard support") — Ubuntu 18.04 LTS, codenamed ‘Bionic Beaver,’ is approaching the end of its standard five-year maintenance period on 31 May 2023. 
  * [Let us serve you, but don’t bring us down](https://blog.archive.org/2023/05/29/let-us-serve-you-but-dont-bring-us-down/ "Let us serve you, but don’t bring us down") — Tens of thousands of requests per second for our public domain OCR files were launched from 64 virtual hosts on amazon’s AWS services. This activity brought archive.org down for all users for about an hour.
  * [Internet Archive](http://archive.org/ "Internet Archive") — Internet Archive is a non-profit library of millions of free books, movies, software, music, websites, and more.



## Tags

[azure linux](https://linuxactionnews.com/tags/azure%20linux), [back-ported patch](https://linuxactionnews.com/tags/back-ported%20patch), [cbl mariner](https://linuxactionnews.com/tags/cbl%20mariner), [eol](https://linuxactionnews.com/tags/eol), [internet archive](https://linuxactionnews.com/tags/internet%20archive), [limits](https://linuxactionnews.com/tags/limits), [linux 6.3 issues](https://linuxactionnews.com/tags/linux%206.3%20issues), [linux 6.3.5](https://linuxactionnews.com/tags/linux%206.3.5), [linux action news](https://linuxactionnews.com/tags/linux%20action%20news), [linux news podcast](https://linuxactionnews.com/tags/linux%20news%20podcast), [microsoft](https://linuxactionnews.com/tags/microsoft), [one-liner patch](https://linuxactionnews.com/tags/one-liner%20patch), [outages](https://linuxactionnews.com/tags/outages), [plasma 6](https://linuxactionnews.com/tags/plasma%206), [rpm-based](https://linuxactionnews.com/tags/rpm-based), [site scraping](https://linuxactionnews.com/tags/site%20scraping), [ubuntu 18.04 lts](https://linuxactionnews.com/tags/ubuntu%2018.04%20lts), [wayland only](https://linuxactionnews.com/tags/wayland%20only), [x11 support](https://linuxactionnews.com/tags/x11%20support), [xfs developer](https://linuxactionnews.com/tags/xfs%20developer), [xfs metadata corruption fix](https://linuxactionnews.com/tags/xfs%20metadata%20corruption%20fix)