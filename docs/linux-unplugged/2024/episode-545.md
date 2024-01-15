# LUP 545: 3,062 Days Later

<iframe src="https://player.fireside.fm/v2/RUkczH-V+1S4LfT5e?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2024-01-14
* Duration: 57 mins 15 secs

## About this episode

Kent Overstreet, the creator of bcachefs, helps us understand where his new filesystem fits, what it's like to upstream a new filesystem, and how they've solved the RAID write hole.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)
* [Kent Overstreet](https://linuxunplugged.com/guests/kentoverstreet)

## Sponsored by

  * [Tailscale](http://tailscale.com/): [Tailscale is a Zero config VPN. It installs on any device in minutes, manages firewall rules for you, and works from anywhere. Get 20 devices for free for a personal account. ](http://tailscale.com/)
  * [Kolide](https://kolide.com/unplugged): [Kolide is a device trust solution for companies with Okta, and they ensure that if a device isn’t trusted and secure, it can’t log into your cloud apps.](https://kolide.com/unplugged)



## Episode links

  * [💥 Gets Sats Quick and Easy with Strike](https://strike.me/ "💥 Gets Sats Quick and Easy with Strike")
  * [📻 LINUX Unplugged on Fountain.FM](https://www.fountain.fm/show/dWiuBeqpDSM86AwXRXov "📻 LINUX Unplugged on Fountain.FM")
  * [Boltz](https://boltz.exchange/ "Boltz") — Privacy First, Non-Custodial Bitcoin Exchange.
  * [bcachefs](https://bcachefs.org/ "bcachefs") — bcachefs is an advanced new filesystem for Linux, with an emphasis on reliability and robustness and the complete set of features one would expect from a modern filesystem. 
  * [bcachefs Erasure coding](https://bcachefs.org/ErasureCoding/ "bcachefs Erasure coding") — Bcachefs takes advantage of the fact that it is already a copy-on-write filesystem. If we're designing our filesystem to avoid update-in-place, why would we do update-in-place in our RAID implementation?
  * [bcachefs Caching](https://bcachefs.org/Caching/ "bcachefs Caching") — bcachefs can be configured for writethrough, writeback, and writearound caching, as well as other more specialized setups. 
  * [bachefs Compression](https://bcachefs.org/Compression/ "bachefs Compression") — Unlike other filesystems that typically do compression at the block level, bcachefs does compression at the extent level - variable size chunks, up to (by default) 128k.
  * [bcachefs Encryption](https://bcachefs.org/Encryption/ "bcachefs Encryption") — bcachefs uses AEAD style encryption (ChaCha20/Poly1305), where each encrypted block is authenticated with a MAC, with a chain of trust up to root (the superblock), and every encrypted block has a unique nonce. 
  * [bcachefs Snapshots](https://bcachefs.org/Snapshots/ "bcachefs Snapshots") — bcachefs provides Btrfs style writeable snapshots, at subvolume granularity. 
  * [(2015) [ANNOUNCE] bcachefs - a general purpose COW filesystem](https://lkml.org/lkml/2015/8/21/22 "\(2015\) \[ANNOUNCE\] bcachefs - a general purpose COW filesystem") — It's taken a long time to get to this point - longer than I would have guessed if you'd asked me back when we first started talking about it - but I'm pretty damn proud of where it's at now.
  * [Kent Overstreet's Patreon](https://www.patreon.com/bcachefs "Kent Overstreet's Patreon")
  * [Unplugged Core Membership](https://unpluggedcore.com/ "Unplugged Core Membership")
  * [Jupiter Signal PROMO 2024](https://jupitersignal.memberful.com/checkout?plan=74364&coupon=2024 "Jupiter Signal PROMO 2024") — $3 off a month forever. 
  * [Webamp](https://webamp.org/ "Webamp") — Winamp 2 re-implemented for the browser. 
  * [Webamp on GitHub](https://github.com/captbaritone/webamp "Webamp on GitHub") — Winamp 2 reimplemented for the browse. 
  * [The Official JB BBS!](http://pebkac.lol "The Official JB BBS!") — vt52 hosts our new official JB BBS! `telnet http://pebkac.lol`



## Tags

[32-bit challenge](https://linuxunplugged.com/tags/32-bit%20challenge), [bbs](https://linuxunplugged.com/tags/bbs), [bcache](https://linuxunplugged.com/tags/bcache), [bcachefs](https://linuxunplugged.com/tags/bcachefs), [boosts](https://linuxunplugged.com/tags/boosts), [btrfs](https://linuxunplugged.com/tags/btrfs), [caching](https://linuxunplugged.com/tags/caching), [car camping](https://linuxunplugged.com/tags/car%20camping), [checksumming](https://linuxunplugged.com/tags/checksumming), [ci](https://linuxunplugged.com/tags/ci), [community](https://linuxunplugged.com/tags/community), [compression](https://linuxunplugged.com/tags/compression), [copy on write](https://linuxunplugged.com/tags/copy%20on%20write), [cow](https://linuxunplugged.com/tags/cow), [database](https://linuxunplugged.com/tags/database), [encryption](https://linuxunplugged.com/tags/encryption), [erasure coding](https://linuxunplugged.com/tags/erasure%20coding), [filesystems](https://linuxunplugged.com/tags/filesystems), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kent overstreet](https://linuxunplugged.com/tags/kent%20overstreet), [linus](https://linuxunplugged.com/tags/linus), [linux](https://linuxunplugged.com/tags/linux), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [low latency](https://linuxunplugged.com/tags/low%20latency), [modern filesystem](https://linuxunplugged.com/tags/modern%20filesystem), [nixos](https://linuxunplugged.com/tags/nixos), [performance](https://linuxunplugged.com/tags/performance), [raid](https://linuxunplugged.com/tags/raid), [raspberry pi](https://linuxunplugged.com/tags/raspberry%20pi), [reliability](https://linuxunplugged.com/tags/reliability), [replication](https://linuxunplugged.com/tags/replication), [rust](https://linuxunplugged.com/tags/rust), [scalability](https://linuxunplugged.com/tags/scalability), [scale](https://linuxunplugged.com/tags/scale), [snapshots](https://linuxunplugged.com/tags/snapshots), [tail latency](https://linuxunplugged.com/tags/tail%20latency), [technology](https://linuxunplugged.com/tags/technology), [upstreaming](https://linuxunplugged.com/tags/upstreaming), [write hole](https://linuxunplugged.com/tags/write%20hole), [xfs](https://linuxunplugged.com/tags/xfs), [zfs](https://linuxunplugged.com/tags/zfs)