# LUP 534: We Nixed Proxmox

<iframe src="https://player.fireside.fm/v2/RUkczH-V+8icC9VLj?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2023-10-29
* Duration: 68 mins 59 secs

## About this episode

We did Proxmox dirty last week, so we try to explain our thinking. But first, a few things have gone down that you should know about.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Kolide](https://kolide.com/unplugged): [Kolide is a device trust solution for companies with Okta, and they ensure that if a device isn’t trusted and secure, it can’t log into your cloud apps.](https://kolide.com/unplugged)
  * [Linode Cloud Hosting](https://linode.com/unplugged): [A special offer for all Linux Unplugged Podcast listeners and new Linode customers, visit linode.com/unplugged, and receive $100 towards your new account. ](https://linode.com/unplugged)
  * [Tailscale](http://tailscale.com/linuxunplugged): [Tailscale is a programmable networking software that is private and secure by default - get it free on up to 100 devices!](http://tailscale.com/linuxunplugged)



## Episode links

  * [🎉 Alby](https://getalby.com/ "🎉 Alby") — Boost into the show, first grab Alby, top it off, and then head over to the Podcast Index.
  * [⚡️ LINUX Unplugged on the Podcastindex.org](https://podcastindex.org/podcast/575694 "⚡️ LINUX Unplugged on the Podcastindex.org") — You can boost from the web. Once Alby is topped off, visit our page on the Podcast Index.
  * [Unplugged Tuxies - 2023](http://tuxies.party/ "Unplugged Tuxies - 2023") — It's time to vote on the 2023 Unplugged Tuxies!
  * [⚠️ Tuxies 2023: Did we miss something? Let us know!](https://nextcloud.tuxies.party/apps/forms/J9HiKYa2zwjsiPHy "⚠️ Tuxies 2023: Did we miss something? Let us know!")
  * [Fedora 39 Delayed To At Least 7 November](https://www.phoronix.com/news/Fedora-39-Delayed-To-7-Nov "Fedora 39 Delayed To At Least 7 November") — While Fedora 39 was aiming for an ideal "early final" release on 18 October, that didn't happen, it was delayed, and then delayed again. Now the earliest Fedora 39 will possibly shift is 7 November.
  * [Bug: F39 RC1.2 images have sometimes “RC” in their name](https://bugzilla.redhat.com/show_bug.cgi?id=2246385 "Bug: F39 RC1.2 images have sometimes “RC” in their name")
  * [Bug: Failed media check immediately disappears on bare metal, shows a black screen instead](https://bugzilla.redhat.com/show_bug.cgi?id=2246410 "Bug: Failed media check immediately disappears on bare metal, shows a black screen instead")
  * [F39 Final Go/No-Go meeting](https://meetbot-raw.fedoraproject.org/fedora-meeting/2023-10-26/f39-final-go_no_go-meeting.2023-10-26-17.00.html "F39 Final Go/No-Go meeting")
  * [Linux Mint Starts working on Wayland Support](https://blog.linuxmint.com/?p=4591 "Linux Mint Starts working on Wayland Support") — The work started on Wayland. As mentioned earlier this year, this was identified as one of the major challenges our project had to tackle in the mid to long term.
  * [Cinnamon Wayland Trello](https://trello.com/b/HHs01Pab/cinnamon-wayland "Cinnamon Wayland Trello")
  * [Linux Mint Starts Working On Wayland For Cinnamon, Likely Not Fully Ready Until 2026](https://www.phoronix.com/news/Linux-Mint-Wayland-Progress "Linux Mint Starts Working On Wayland For Cinnamon, Likely Not Fully Ready Until 2026")
  * [Six Great Features With The Upcoming Linux 6.6 Kernel](https://www.phoronix.com/news/Linux-6.6-Great-Features "Six Great Features With The Upcoming Linux 6.6 Kernel") — While there were many last minute fixes this week, the changes don't appear to be too scary or invasive. In any event the Linux 6.6 kernel is bringing some exciting features.
  * [Linux 6.6 Features Include The EEVDF Scheduler, Shadow Stack, Intel IVSC, AMD DBC & More](https://www.phoronix.com/review/linux-66-features "Linux 6.6 Features Include The EEVDF Scheduler, Shadow Stack, Intel IVSC, AMD DBC & More")
  * [Btrfs For Linux 6.6 Brings Fixes, Partially Recovers From Scrub Performance Regression](https://www.phoronix.com/news/Btrfs-Linux-6.6 "Btrfs For Linux 6.6 Brings Fixes, Partially Recovers From Scrub Performance Regression") — David Sterba of SUSE sent out the Btrfs updates on Monday for the Linux 6.6 kernel merge window. There are no explicit new features this cycle but a variety of bug fixes, including work to address the Btrfs scrub performance following a rework back in Linux 6.4. The scrub performance isn't entirely restored but at least it's inching ahead in the right direction with Linux 6.6.
  * [EXT4 Lands A Nice Performance Improvement For Appending To Delalloc Files](https://www.phoronix.com/news/Linux-6.6-EXT4 "EXT4 Lands A Nice Performance Improvement For Appending To Delalloc Files") — I conducted tests in my 32-core environment by launching 32 concurrent threads to append write to the same file. Each write operation had a length of 1024 bytes and was repeated 100000 times. Without using this patch, the test was completed in 7705 ms. However, with this patch, the test was completed in 5066 ms, resulting in a performance improvement of 34%.
  * [XFS File-System Maintainer Stepping Down](https://www.phoronix.com/news/XFS-Maintainer-Steps-Down "XFS File-System Maintainer Stepping Down") — My final act as maintainer is to write down every thing that I've been doing as maintainer for the past six years. There are too many demands placed on the maintainer, and the only way to fix this is to delegate the responsibilities. I also wrote down my impressions of the unwritten rules about how to contribute to XFS.
  * [XFS Begins Landing Online Repair, New Release Manager Takes Over](https://www.phoronix.com/news/Linux-6.6-XFS "XFS Begins Landing Online Repair, New Release Manager Takes Over") — We now have in-memory pageable memory for staging btrees, a bunch of pending fixes, and we've started the process of refactoring the scrub support code to support more of repair.
  * [SELinux In Linux 6.6 Removes References To Its Origins At The US NSA](https://www.phoronix.com/news/SELinux-Drops-NSA-References "SELinux In Linux 6.6 Removes References To Its Origins At The US NSA") — We've come a long way from the original NSA submission and I would consider SELinux a true community project at this point so removing the NSA branding just makes sense.
  * [Linux 6.6 To Bring Another Rust Toolchain Upgrade](https://www.phoronix.com/news/Linux-6.6-Rust-Changes "Linux 6.6 To Bring Another Rust Toolchain Upgrade") — Some of the other Rust changes for this imminent merge window include supporting the rust-analyzer for out-of-tree kernel modules, the Rust availability detection script has been improved, a new "paste!" proc macro, new pinned-init APIs, and a variety of other additions to continue to make Rust programming possibilities for the Linux kernel more robust.
  * [[SOLVED] - LXC Nvidia Passthrough | Proxmox Support Forum](https://forum.proxmox.com/threads/lxc-nvidia-passthrough.131929/ "\[SOLVED\] - LXC Nvidia Passthrough | Proxmox Support Forum")
  * [Contribute to Podverse](https://podverse.fm/contribute "Contribute to Podverse")
  * [Soltros' Nix Config](https://github.com/soltros/nixconfigs/blob/main/desktop/configuration.nix "Soltros' Nix Config")
  * [SilverBullet](https://silverbullet.md/ "SilverBullet") — SilverBullet is an extensible open-source, personal knowledge management system. Indeed, that’s fancy talk for “a note-taking app with links.” However, SilverBullet goes a bit beyond just that.
  * [Nixpkgs supply chain security project](https://discourse.nixos.org/t/nixpkgs-supply-chain-security-project/34345 "Nixpkgs supply chain security project") — The focus of this project is on reducing our reliance on foreign binaries to compile Nixpkgs from scratch, ensuring we are are indeed running the code we compiled by leveraging existing security components in NixOS, and putting in place mechanisms that allow us to deliver the most up-to-date, secure software whenever it is available in a way that can be sustained given our maintainer capacities.
  * [Pick: kmon](https://github.com/orhun/kmon "Pick: kmon") — Linux Kernel Manager and Activity Monitor 🐧💻
  * [kmon in nixpkgs](https://search.nixos.org/packages?channel=23.05&show=kmon&from=0&size=50&sort=relevance&type=packages&query=kmon "kmon in nixpkgs")
  * [LinuxFest Northwest Youtube](https://www.youtube.com/@LinuxFestNorthwest/videos "LinuxFest Northwest Youtube")
  * [LinuxFest Northwest 2023 Minifest: What’s New in Nextcloud?](https://www.youtube.com/watch?v=e9SXwA3Q8dc "LinuxFest Northwest 2023 Minifest: What’s New in Nextcloud?")
  * [LinuxFest Northwest 2023 Minifest Videos](https://www.youtube.com/playlist?list=PLjDc7gDlIAST09nqYxYxpn_VdQPVzyAcs "LinuxFest Northwest 2023 Minifest Videos")
  * [docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge "docker-wyze-bridge") — WebRTC/RTSP/RTMP/LL-HLS bridge for Wyze cams in a docker container.
  * [wz_mini_hacks](https://github.com/gtxaspec/wz_mini_hacks "wz_mini_hacks") — Run whatever firmware you want on your camera and have root access to the device.
  * [Bitcoin Beach](https://www.bitcoinbeach.com/ "Bitcoin Beach") — The project Bitcoin Beach is creating a sustainable Bitcoin Economic ecosystem on the coast of El Salvador, where the majority of people do not have access to bank accounts and the local businesses could never qualify for merchant accounts needed to accept credit cards.



## Tags

[32-bit challenge](https://linuxunplugged.com/tags/32-bit%20challenge), [bcachefs](https://linuxunplugged.com/tags/bcachefs), [bitcoin beach](https://linuxunplugged.com/tags/bitcoin%20beach), [btrfs](https://linuxunplugged.com/tags/btrfs), [cinnamon](https://linuxunplugged.com/tags/cinnamon), [debian](https://linuxunplugged.com/tags/debian), [ext4](https://linuxunplugged.com/tags/ext4), [fedora](https://linuxunplugged.com/tags/fedora), [fedora 39](https://linuxunplugged.com/tags/fedora%2039), [fountain](https://linuxunplugged.com/tags/fountain), [homeassistant](https://linuxunplugged.com/tags/homeassistant), [immich](https://linuxunplugged.com/tags/immich), [ipfs](https://linuxunplugged.com/tags/ipfs), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kernel](https://linuxunplugged.com/tags/kernel), [kmon](https://linuxunplugged.com/tags/kmon), [kvm](https://linuxunplugged.com/tags/kvm), [linux 6.6](https://linuxunplugged.com/tags/linux%206.6), [linux kernel manager](https://linuxunplugged.com/tags/linux%20kernel%20manager), [linux mint](https://linuxunplugged.com/tags/linux%20mint), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [linuxfest northwest](https://linuxunplugged.com/tags/linuxfest%20northwest), [lxc](https://linuxunplugged.com/tags/lxc), [nextcloud](https://linuxunplugged.com/tags/nextcloud), [nextcloud aio](https://linuxunplugged.com/tags/nextcloud%20aio), [nix](https://linuxunplugged.com/tags/nix), [nixos](https://linuxunplugged.com/tags/nixos), [phoronix](https://linuxunplugged.com/tags/phoronix), [podverse](https://linuxunplugged.com/tags/podverse), [proxmox](https://linuxunplugged.com/tags/proxmox), [rust](https://linuxunplugged.com/tags/rust), [rust-analyzer](https://linuxunplugged.com/tags/rust-analyzer), [selinux](https://linuxunplugged.com/tags/selinux), [silverbullet.md](https://linuxunplugged.com/tags/silverbullet.md), [tuxies](https://linuxunplugged.com/tags/tuxies), [virtualization](https://linuxunplugged.com/tags/virtualization), [vm](https://linuxunplugged.com/tags/vm), [wayland](https://linuxunplugged.com/tags/wayland), [wyze](https://linuxunplugged.com/tags/wyze), [xfs](https://linuxunplugged.com/tags/xfs), [zfs](https://linuxunplugged.com/tags/zfs)