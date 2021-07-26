# LUP 348: OK OOMer

<iframe src="https://player.fireside.fm/v2/RUkczH-V+ONpJHPjO?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2020-04-07
* Duration: 63 mins 56 secs

## About this episode

Today we make nice with a killer, an early out-of-memory daemon, and one of the new features in Fedora 32. We put EarlyOOM to the test in a real-world workload and are shocked by the results.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [chzbacon](https://linuxunplugged.com/hosts/chzbacon)
* [Alex Kretzschmar](https://linuxunplugged.com/guests/alexktz)
* [Neal Gompa](https://linuxunplugged.com/guests/nealgompa)

## Sponsored by

None



## Episode links

  * [Window Maker Version 0.95.9 Released](http://www.windowmaker.org/news/ "Window Maker Version 0.95.9 Released")
  * [Microsoft announces IPE, a new code integrity feature for Linux](https://www.zdnet.com/article/microsoft-announces-ipe-a-new-code-integrity-feature-for-linux/ "Microsoft announces IPE, a new code integrity feature for Linux") — Microsoft says that IPE is not intended for general-purpose computing. The IPE LSM was designed for very specific use cases where security is paramount, and administrators need to be in full control of what runs on their systems. Examples include embedded systems, such as network firewall devices running in a data center, or Linux servers running strict and immutable configurations and applications.
  * [OpenWrt - Opkg susceptible to MITM](https://openwrt.org/advisory/2020-01-31-1 "OpenWrt - Opkg susceptible to MITM")
  * [Brent sits down with Daniel Foré, founder of elementary OS](https://extras.show/68 "Brent sits down with Daniel Foré, founder of elementary OS")
  * [Know when we're going to be live. Check out the calendar!](https://www.jupiterbroadcasting.com/release-calendar/ "Know when we're going to be live. Check out the calendar!")
  * [Keep the conversation going join us on Telegram](https://jupiterbroadcasting.com/telegram "Keep the conversation going join us on Telegram")
  * [Fedora nightly compose finder](http://happyassassin.net/nightlies.html "Fedora nightly compose finder")
  * [Fedora 32 Looking At Using EarlyOOM By Default To Better Deal With Low Memory Situations](https://www.phoronix.com/scan.php?page=news_item&px=Fedora-32-Default-EarlyOOM "Fedora 32 Looking At Using EarlyOOM By Default To Better Deal With Low Memory Situations") — The oom-killer generally has a bad reputation among Linux users. This may be part of the reason Linux invokes it only when it has absolutely no other choice. It will swap out the desktop environment, drop the whole page cache and empty every buffer before it will ultimately kill a process. At least that's what I think that it will do. I have yet to be patient enough to wait for it, sitting in front of an unresponsive system. 
  * [earlyoom - Early OOM Daemon for Linux](https://github.com/rfjakob/earlyoom "earlyoom - Early OOM Daemon for Linux") — The oom-killer generally has a bad reputation among Linux users. This may be part of the reason Linux invokes it only when it has absolutely no other choice. It will swap out the desktop environment, drop the whole page cache and empty every buffer before it will ultimately kill a process. At least that's what I think that it will do. I have yet to be patient enough to wait for it, sitting in front of an unresponsive system. 
  * [rfjakob/systembus-notify: systembus-notify - system bus notification daemon](https://github.com/rfjakob/systembus-notify "rfjakob/systembus-notify: systembus-notify - system bus notification daemon")
  * [oomd](https://github.com/facebookincubator/oomd "oomd") — Out of memory killing has historically happened inside kernel space. On a memory overcommitted linux system, malloc(2) and friends usually never fail. However, if an application dereferences the returned pointer and the system has run out of physical memory, the linux kernel is forced to take extreme measures, up to and including killing processes. This is sometimes a slow and painful process because the kernel can spend an unbounded amount of time swapping in and out pages and evicting the page cache. Furthermore, configuring policy is not very flexible while being somewhat complicated.
  * [low-memory-monitor on GitLab](https://gitlab.freedesktop.org/hadess/low-memory-monitor/ "low-memory-monitor on GitLab")
  * [low-memory-monitor](http://www.hadess.net/2019/08/low-memory-monitor-new-project.html "low-memory-monitor") — low-memory-monitor, as its name implies, monitors the amount of free physical memory on the system and will shoot off signals to interested user-space applications, usually session managers, or sandboxing helpers, when that memory runs low, making it possible for applications to shrink their memory footprints before it's too late either to recover a usable system, or avoid taking a performance hit. 
  * [Nohang](https://github.com/hakavlad/nohang "Nohang") — Nohang is a highly configurable daemon for Linux which is able to correctly prevent out of memory (OOM) and keep system responsiveness in low memory conditions. 
  * [Better interactivity in low-memory situations - devel - Fedora Mailing-Lists](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/XUZLHJ5O32OX24LG44R7UZ2TMN6NY47N/#XUZLHJ5O32OX24LG44R7UZ2TMN6NY47N "Better interactivity in low-memory situations - devel - Fedora Mailing-Lists")
  * [EnableEarlyoom - Fedora Project Wiki](https://fedoraproject.org/wiki/Changes/EnableEarlyoom#Enable_EarlyOOM "EnableEarlyoom - Fedora Project Wiki")
  * [Nushell - The Unix philosophy of shells, where pipes connect simple commands together, and bring it to the modern style of development.](https://www.nushell.sh/ "Nushell - The Unix philosophy of shells, where pipes connect simple commands together, and bring it to the modern style of development.")
  * [Timekpr - simple and easy to use time managing software that helps optimizing time spent at computer.](https://launchpad.net/timekpr-next "Timekpr - simple and easy to use time managing software that helps optimizing time spent at computer.")



## Tags

[a cloud guru](https://linuxunplugged.com/tags/a%20cloud%20guru), [command line](https://linuxunplugged.com/tags/command%20line), [earlyoom](https://linuxunplugged.com/tags/earlyoom), [facebook](https://linuxunplugged.com/tags/facebook), [fedora](https://linuxunplugged.com/tags/fedora), [fedora 32](https://linuxunplugged.com/tags/fedora%2032), [integrity policy enforcement](https://linuxunplugged.com/tags/integrity%20policy%20enforcement), [ipe](https://linuxunplugged.com/tags/ipe), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [linux](https://linuxunplugged.com/tags/linux), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux router](https://linuxunplugged.com/tags/linux%20router), [low-memory-monitor](https://linuxunplugged.com/tags/low-memory-monitor), [lsm](https://linuxunplugged.com/tags/lsm), [memory pressure](https://linuxunplugged.com/tags/memory%20pressure), [microsoft](https://linuxunplugged.com/tags/microsoft), [mitm](https://linuxunplugged.com/tags/mitm), [nohang](https://linuxunplugged.com/tags/nohang), [nushell](https://linuxunplugged.com/tags/nushell), [oomd](https://linuxunplugged.com/tags/oomd), [openwrt](https://linuxunplugged.com/tags/openwrt), [opkg](https://linuxunplugged.com/tags/opkg), [opnsense](https://linuxunplugged.com/tags/opnsense), [performance](https://linuxunplugged.com/tags/performance), [pfsense](https://linuxunplugged.com/tags/pfsense), [psi](https://linuxunplugged.com/tags/psi), [security](https://linuxunplugged.com/tags/security), [shell](https://linuxunplugged.com/tags/shell), [time tracking](https://linuxunplugged.com/tags/time%20tracking), [timekpr-next](https://linuxunplugged.com/tags/timekpr-next), [unplugged](https://linuxunplugged.com/tags/unplugged)