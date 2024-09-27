# LUP 567: So Long sudo

<iframe src="https://player.fireside.fm/v2/RUkczH-V+3R9Ckl8O?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2024-06-16
* Duration: 91 mins 41 secs

## About this episode

Your Linux box is a-changin'. systemd has a huge new release; we'll get into the most impressive features, including the new sudo replacement. Plus, our thoughts on the new Linux Arm laptops that are just around the corner.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Core Contributor Membership](https://jupitersignal.memberful.com/checkout?plan=52946&coupon=summer): [Take $1 a month of your membership for a lifetime!](https://jupitersignal.memberful.com/checkout?plan=52946&coupon=summer)
  * [Tailscale](http://tailscale.com/linuxunplugged): [Tailscale is a programmable networking software that is private and secure by default - get it free on up to 100 devices!](http://tailscale.com/linuxunplugged)
  * [1Password Extended Access Management](https://1password.com/unplugged): [1Password Extended Access Management is a device trust solution for companies with Okta, and they ensure that if a device isn't trusted and secure, it can't log into your cloud apps.](https://1password.com/unplugged)



## Episode links

  * [💥 Gets Sats Quick and Easy with Strike](https://strike.me/ "💥 Gets Sats Quick and Easy with Strike")
  * [📻 LINUX Unplugged on Fountain.FM](https://www.fountain.fm/show/dWiuBeqpDSM86AwXRXov "📻 LINUX Unplugged  on Fountain.FM")
  * [Announcing systemd v256](https://0pointer.net/blog/announcing-systemd-v256.html "Announcing systemd v256") — In the weeks leading up to this release I have posted a series of serieses of posts to Mastodon about key new features in this release.
  * [systemd changes with v2⁸:](https://github.com/systemd/systemd/releases/tag/v256 "systemd changes with v2⁸:")
  * [systemd 256 Released With run0, systemd-vpick, importctl & Other New Features](https://www.phoronix.com/news/systemd-256 "systemd 256 Released With run0, systemd-vpick, importctl & Other New Features")
  * [Lennart on systemd-vpick](https://mastodon.social/@pid_eins/112332457438509644 "Lennart on systemd-vpick") — Basically, you can now place multiple versions of the same resource in some dir of your choice, suffix that dir's name with .v/ and the you get some basic version management in place: delete or add new versions by just removing/adding new files, and the tools will find the newest item dropped in automatically.
  * [Introduction to Portable Services](https://systemd.io/PORTABLE_SERVICES/ "Introduction to Portable Services") — “Portable services” do not provide a fully isolated environment to the payload, like containers mostly intend to. Instead, they are more like regular system services, can be controlled with the same tools, are exposed the same way in all infrastructure, and so on. The main difference is that they use a different root directory than the rest of the system.
  * [Trying out systemd's Portable Services](https://samthursfield.wordpress.com/2022/05/13/trying-out-systemds-portable-services/ "Trying out systemd's Portable Services") — All in all, the core pieces are already in place for a very promising new technology that should make it easier for 3rd parties to provide Linux system-level software in a safe and convenient way, well done to the systemd team for a well executed concept. All it lacks is some polish around the tooling and integration.
  * [systemd sleep](https://mastodon.social/@pid_eins/112404050701925757 "systemd sleep") — Putting a PC to sleep is complicated business and there are different mechanisms available to achieve this on Linux. 
  * [Lennart on SSH and AF_VSOCK](https://mastodon.social/@pid_eins/112411213727666482 "Lennart on SSH and AF_VSOCK") — This automatic ssh-via-AF_VSOCK logic is particularly useful 
  * [DDIs and systemd-nspawn](https://mastodon.social/@pid_eins/112364314961758625 "DDIs and systemd-nspawn") — Or in other words: there's now unprivileged systemd-npsawn containers. Yay!
  * [Lennart on systemd-vmspawn](https://mastodon.social/@pid_eins/112376110947253007 "Lennart on systemd-vmspawn")
  * [Lennart on sd_notify](https://mastodon.social/@pid_eins/112341584011845948 "Lennart on sd_notify")
  * [Lennart on dlopen](https://mastodon.social/@pid_eins/112445409388762154 "Lennart on dlopen")
  * [Lennart on run0](https://mastodon.social/@pid_eins/112353324518585654 "Lennart on run0") — There's a new tool in systemd, called run0. Or actually, it's not a new tool, it's actually the long existing tool systemd-run, but when invoked under the run0 name (via a symlink) it behaves a lot like a sudo clone. But with one key difference: it's not in fact SUID.
  * [doas - dedicated openbsd application subexecutor](https://flak.tedunangst.com/post/doas "doas - dedicated openbsd application subexecutor")
  * [Doas - NixOS Wiki](https://nixos.wiki/wiki/Doas "Doas - NixOS Wiki")
  * [Doas on Wikipedia](https://en.wikipedia.org/wiki/Doas "Doas on Wikipedia")
  * [The Tragedy of systemd](https://www.youtube.com/watch?v=o_AIw9bGogo "The Tragedy of systemd") — Join me on a journey through the bootstrap process, the history of init, the reasons why change can be scary, and the discovery of a part of your OS you may not even know existed.
  * [The Two Year Journey Funded By Arm/Qualcomm For Improving ARM Linux Laptop Support](https://www.phoronix.com/news/Two-Years-Improving-ARM-Laptops "The Two Year Journey Funded By Arm/Qualcomm For Improving ARM Linux Laptop Support") — ARM Kernel developers spent the last two years working on improving ARM Linux laptop support with a focus on the Lenovo ThinkPad X13s powered by a Qualcomm SoC.
  * [Ubuntu 24.04 LTS support to the Lenovo ThinkPad x13s](https://www.omgubuntu.co.uk/2024/05/ubuntu-24-04-lenovo-thinkpad-x13s-snapdragon "Ubuntu 24.04 LTS support to the Lenovo ThinkPad x13s")
  * [Snapdragon 8cx](https://www.qualcomm.com/products/mobile/snapdragon/pcs-and-tablets/snapdragon-mobile-compute-platforms/snapdragon-8cx-gen-3-compute-platform "Snapdragon 8cx")
  * [Ubuntu Asahi project](https://www.omgubuntu.co.uk/2023/10/ubuntu-ashai-for-apple-silicon "Ubuntu Asahi project")
  * [TUXEDO Working on Snapdragon X Elite Linux Laptop](https://www.omgubuntu.co.uk/2024/06/tuxedo-working-on-snapdragon-x-elite-linux-laptop "TUXEDO Working on Snapdragon X Elite Linux Laptop")
  * [Membership Summer Discount](https://jupitersignal.memberful.com/checkout?plan=52946&coupon=summer "Membership Summer Discount") — Take $1 a month of your membership for a lifetime!
  * [Spokane Meetup, Sat, Jul 13, 2024, 4:00 PM](https://www.meetup.com/jupiterbroadcasting/events/301471716/ "Spokane Meetup, Sat, Jul 13, 2024, 4:00 PM")
  * [Berlin with Brent: September Meetup @ Nextcloud Conference, Fri, Sep 13, 2024 | Meetup](https://www.meetup.com/jupiterbroadcasting/events/300421391/ "Berlin with Brent: September Meetup @ Nextcloud Conference, Fri, Sep 13, 2024 | Meetup")
  * [A Nix Flake for Bitfocus Companion](https://github.com/noblepayne/bitfocus-companion-flake "A Nix Flake for Bitfocus Companion")
  * [ChrisLAS' Beelink NixOS Config](https://github.com/ChrisLAS/nix "ChrisLAS' Beelink NixOS Config")
  * [Bluetooth - NixOS Wiki](https://nixos.wiki/wiki/Bluetooth "Bluetooth - NixOS Wiki")
  * [nix-direnv](https://determinate.systems/posts/nix-direnv/ "nix-direnv")
  * [xscreensaver on Android](https://www.jwz.org/xscreensaver/google.html "xscreensaver on Android")
  * [Rainier cherry - Wikipedia](https://en.wikipedia.org/wiki/Rainier_cherry "Rainier cherry - Wikipedia")
  * [Pick: Iotas](https://gitlab.gnome.org/World/iotas "Pick: Iotas") — Markdown notes that syncs with NextCloud Notes.



## Tags

[256](https://linuxunplugged.com/tags/256), [arm](https://linuxunplugged.com/tags/arm), [beelink](https://linuxunplugged.com/tags/beelink), [berlin meetup](https://linuxunplugged.com/tags/berlin%20meetup), [berlin with brent](https://linuxunplugged.com/tags/berlin%20with%20brent), [bitfocus companion](https://linuxunplugged.com/tags/bitfocus%20companion), [cgroups](https://linuxunplugged.com/tags/cgroups), [doas](https://linuxunplugged.com/tags/doas), [father's day](https://linuxunplugged.com/tags/father's%20day), [homed-managed](https://linuxunplugged.com/tags/homed-managed), [importctl](https://linuxunplugged.com/tags/importctl), [iotas](https://linuxunplugged.com/tags/iotas), [ipod](https://linuxunplugged.com/tags/ipod), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [lenovo thinkpad x13s](https://linuxunplugged.com/tags/lenovo%20thinkpad%20x13s), [liblzma](https://linuxunplugged.com/tags/liblzma), [linux arm](https://linuxunplugged.com/tags/linux%20arm), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [nextcloud conference](https://linuxunplugged.com/tags/nextcloud%20conference), [nextcloud notes](https://linuxunplugged.com/tags/nextcloud%20notes), [nix drinking game](https://linuxunplugged.com/tags/nix%20drinking%20game), [nix-darwin](https://linuxunplugged.com/tags/nix-darwin), [nix-direnv](https://linuxunplugged.com/tags/nix-direnv), [norwich meetup](https://linuxunplugged.com/tags/norwich%20meetup), [ntp challenge](https://linuxunplugged.com/tags/ntp%20challenge), [omakub](https://linuxunplugged.com/tags/omakub), [portable service](https://linuxunplugged.com/tags/portable%20service), [qualcomm](https://linuxunplugged.com/tags/qualcomm), [rockbox os](https://linuxunplugged.com/tags/rockbox%20os), [run0](https://linuxunplugged.com/tags/run0), [snapdragon](https://linuxunplugged.com/tags/snapdragon), [spokane meetup](https://linuxunplugged.com/tags/spokane%20meetup), [squid](https://linuxunplugged.com/tags/squid), [ssh](https://linuxunplugged.com/tags/ssh), [sudo](https://linuxunplugged.com/tags/sudo), [suid](https://linuxunplugged.com/tags/suid), [system v](https://linuxunplugged.com/tags/system%20v), [systemd](https://linuxunplugged.com/tags/systemd), [systemd sleep](https://linuxunplugged.com/tags/systemd%20sleep), [systemd-nspawn](https://linuxunplugged.com/tags/systemd-nspawn), [systemd-run0](https://linuxunplugged.com/tags/systemd-run0), [systemd-vmspawn](https://linuxunplugged.com/tags/systemd-vmspawn), [systemd-vpick](https://linuxunplugged.com/tags/systemd-vpick), [the tragedy of systemd](https://linuxunplugged.com/tags/the%20tragedy%20of%20systemd), [ubuntu](https://linuxunplugged.com/tags/ubuntu), [v2⁸](https://linuxunplugged.com/tags/v2%E2%81%B8), [xscreensaver for android](https://linuxunplugged.com/tags/xscreensaver%20for%20android), [xz](https://linuxunplugged.com/tags/xz)