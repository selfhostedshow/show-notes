# LUP 556: The xz Backdoor Exposed 🚨

<iframe src="https://player.fireside.fm/v2/RUkczH-V+RJk2qe3U?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2024-03-31
* Duration: 70 mins 3 secs

## About this episode

We're breaking down the attack: how it works, how it was hidden, and why time was running out for the attacker.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Tailscale](http://tailscale.com/linuxunplugged): [Tailscale is a programmable networking software that is private and secure by default - get it free on up to 100 devices!](http://tailscale.com/linuxunplugged)
  * [Kolide](https://kolide.com/unplugged): [Kolide is a device trust solution for companies with Okta, and they ensure that if a device isn't trusted and secure, it can't log into your cloud apps.](https://kolide.com/unplugged)



## Episode links

  * [💥 Gets Sats Quick and Easy with Strike](https://strike.me/ "💥 Gets Sats Quick and Easy with Strike")
  * [📻 LINUX Unplugged on Fountain.FM](https://www.fountain.fm/show/dWiuBeqpDSM86AwXRXov "📻 LINUX Unplugged on Fountain.FM")
  * [oss-security mailing list](https://www.openwall.com/lists/oss-security/2024/03/29/4 "oss-security mailing list") — Backdoor in upstream xz/liblzma leading to ssh server compromise.
  * [Fedora Announcement](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users "Fedora Announcement")
  * [Debian Announcement](https://security-tracker.debian.org/tracker/CVE-2024-3094 "Debian Announcement")
  * [Ubuntu Announcement](https://discourse.ubuntu.com/t/xz-liblzma-security-update/43714 "Ubuntu Announcement")
  * [Kali Linux Announcement](https://www.kali.org/blog/about-the-xz-backdoor/ "Kali Linux Announcement")
  * [Arch Linux Announcement](https://archlinux.org/news/the-xz-package-has-been-backdoored/ "Arch Linux Announcement")
  * [Gentoo Announcement](https://bugs.gentoo.org/928134 "Gentoo Announcement")
  * [openSUSE Tumbleweeed Announcement](https://news.opensuse.org/2024/03/29/xz-backdoor/ "openSUSE Tumbleweeed Announcement")
  * [NixOS Unstable Discussion](https://discourse.nixos.org/t/cve-2024-3094-malicious-code-in-xz-5-6-0-and-5-6-1-tarballs/42405 "NixOS Unstable Discussion")
  * [Why does it take two weeks for NixOS to replace xz?](https://discourse.nixos.org/t/cve-2024-3094-malicious-code-in-xz-5-6-0-and-5-6-1-tarballs/42405/5 "Why does it take two weeks for NixOS to replace xz?")
  * [Andres Freund on Mastodon](https://mastodon.social/@AndresFreundTec/112180406142695845 "Andres Freund on Mastodon") — I was doing some micro-benchmarking at the time, needed to quiesce the system to reduce noise. Saw sshd processes were using a surprising amount of CPU, despite immediately failing because of wrong usernames etc....
  * [rwmj on Hacker News](https://news.ycombinator.com/item?id=39865810 "rwmj on Hacker News") — Very annoying - the apparent author of the backdoor was in communication with me over several weeks trying to get xz 5.6.x added to Fedora 40 & 41 because of its "great new features"
  * [A Microcosm of the interactions in Open Source projects](https://robmensching.com/blog/posts/2024/03/30/a-microcosm-of-the-interactions-in-open-source-projects/ "A Microcosm of the interactions in Open Source projects") — Make no mistake. This is the way it works. It needs to change.
  * [Devuan GNU/Linux on X](https://twitter.com/devuanorg/status/1774029432979653069?t=ASJqAbm5fVHDKeq7CLKqjw "Devuan GNU/Linux on X") — Devuan is not affected by the latest vulnerability caused by systemd.
  * [systemd PR: Dynamically load compression libraries](https://github.com/systemd/systemd/pull/31550#issuecomment-1972737923 "systemd PR: Dynamically load compression libraries")
  * [Matteo Croce on X](https://twitter.com/teknoraver85/status/1774452847188312163 "Matteo Croce on X") — I'm the author of such PR. While I absolutely didn't know that libxz had a backdoor, I really think that libraries should be loaded on-demand when rarely used, hence my change :)
  * [Ryan C. Gordon on X](https://twitter.com/icculus/status/1774310925035524333 "Ryan C. Gordon on X") — This is probably how the xz thing happened, right?
  * [Jan Wildeboer on the Fediverse](https://social.wildeboer.net/@jwildeboer/112184074379919145 "Jan Wildeboer on the Fediverse") — Again the FOSS world has proven to be vigilant and proactive in finding bugs and backdoors, IMHO.
  * [Unplugged Core Membership](https://unpluggedcore.com/ "Unplugged Core Membership")
  * [TXLF is coming up! ](https://2024.texaslinuxfest.org/ "TXLF is coming up! ") — April 12 - 13 in Austin, Texas.
  * [LFNW coming up!](https://linuxfestnorthwest.org/ "LFNW coming up!") — April 26 - 28
  * [Mobile Game Ads Are Boosting Podcast Follower Counts](https://www.bloomberg.com/news/newsletters/2024-03-28/mobile-game-ads-are-boosting-podcast-follower-counts "Mobile Game Ads Are Boosting Podcast Follower Counts") — Wondery, iHeart and Lemonada Media are all using a non-public product from MowPod - which gives extra lives and game credits to gamers if they follow shows on Apple Podcasts from game apps.
  * [MowPod's podcast promotion tools: tales from the bar](https://podnews.net/article/mowpod-promotion "MowPod's podcast promotion tools: tales from the bar")
  * [fortydeux's NixOS Configs](https://github.com/fortydeux/Fortydeux-NixOS-System-Flake/ "fortydeux's NixOS Configs")
  * [Prism Launcher](https://prismlauncher.org/ "Prism Launcher") — An Open Source Minecraft launcher with the ability to manage multiple instances, accounts and mods.
  * [World Backup Day — March 31st](https://www.worldbackupday.com/en/ "World Backup Day — March 31st") — One small accident or failure could destroy all the important stuff you care about.
  * [Updating Our Fiddly Bits | LINUX Unplugged 494](https://www.jupiterbroadcasting.com/show/linux-unplugged/494/ "Updating Our Fiddly Bits | LINUX Unplugged 494")



## Tags

[alpine](https://linuxunplugged.com/tags/alpine), [arch linux](https://linuxunplugged.com/tags/arch%20linux), [backdoor](https://linuxunplugged.com/tags/backdoor), [burnout](https://linuxunplugged.com/tags/burnout), [compression libraries](https://linuxunplugged.com/tags/compression%20libraries), [debian](https://linuxunplugged.com/tags/debian), [fedora](https://linuxunplugged.com/tags/fedora), [gentoo](https://linuxunplugged.com/tags/gentoo), [humint](https://linuxunplugged.com/tags/humint), [jia tan](https://linuxunplugged.com/tags/jia%20tan), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kali linux](https://linuxunplugged.com/tags/kali%20linux), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [nixos](https://linuxunplugged.com/tags/nixos), [open source](https://linuxunplugged.com/tags/open%20source), [openssh](https://linuxunplugged.com/tags/openssh), [opensuse](https://linuxunplugged.com/tags/opensuse), [remote code execution](https://linuxunplugged.com/tags/remote%20code%20execution), [systemd](https://linuxunplugged.com/tags/systemd), [transparency](https://linuxunplugged.com/tags/transparency), [trust model](https://linuxunplugged.com/tags/trust%20model), [ubuntu](https://linuxunplugged.com/tags/ubuntu), [xz](https://linuxunplugged.com/tags/xz)