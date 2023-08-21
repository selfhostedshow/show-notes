# LUP 524: How Our Server Got It's Groove Back

<iframe src="https://player.fireside.fm/v2/RUkczH-V+2sorjDIw?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2023-08-20
* Duration: 66 mins 16 secs

## About this episode

Can we build an indestructible server that stands up to the test of giving out root login to the Internet?

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Tailscale](http://tailscale.com/): [Tailscale is a Zero config VPN. It installs on any device in minutes, manages firewall rules for you, and works from anywhere. Get 20 devices for free for a personal account. ](http://tailscale.com/)
  * [Linode Cloud Hosting](https://linode.com/unplugged): [A special offer for all Linux Unplugged Podcast listeners and new Linode customers, visit linode.com/unplugged, and receive $100 towards your new account. ](https://linode.com/unplugged)
  * [Kolide](https://kolide.com/unplugged): [Kolide is a device trust solution for companies with Okta, and they ensure that if a device isn’t trusted and secure, it can’t log into your cloud apps.](https://kolide.com/unplugged)



## Episode links

  * [🎉 Alby](https://getalby.com/ "🎉 Alby") — Boost into the show, first grab Alby, top it off, and then head over to the Podcast Index.
  * [⚡️ LINUX Unplugged on the Podcastindex.org](https://podcastindex.org/podcast/575694 "⚡️ LINUX Unplugged on the Podcastindex.org") — You can boost from the web. Once Alby is topped off, visit our page on the Podcast Index.
  * [Spokane Linux Love, Sat, Sep 16, 2023, 1:00 PM | Meetup](https://www.meetup.com/jupiterbroadcasting/events/295568221 "Spokane Linux Love, Sat, Sep 16, 2023, 1:00 PM | Meetup") — It's finally happening! Let's get together at Iron Goat Brewing.
  * [Best laptops for NixOS - Help - NixOS Discourse](https://discourse.nixos.org/t/best-laptops-for-nixos/8545 "Best laptops for NixOS - Help - NixOS Discourse")
  * [Mobile NixOS](https://mobile.nixos.org/ "Mobile NixOS")
  * [Devices List — Mobile NixOS](https://mobile.nixos.org/devices/index.html "Devices List — Mobile NixOS")
  * [Iron Goat Brewing](https://irongoatbrewing.com/ "Iron Goat Brewing")
  * [LinuxFest Northwest 2023 Sponsorship Prospectus](https://lfnw.org/linuxfest-northwest-2023-sponsorship-prospectus.pdf "LinuxFest Northwest 2023 Sponsorship Prospectus") — LinuxFest Northwest 2023 will be held October 20-22, 2023 at Bellingham Technical College. The Fest is a free and open community event dedicated to provide and support educational activities related to Linux and Open Source Software.
  * [NixOS friendly hosters - NixOS Wiki](https://nixos.wiki/wiki/NixOS_friendly_hosters "NixOS friendly hosters - NixOS Wiki")
  * [Install and Configure NixOS on a Linode | Linode Docs](https://www.linode.com/docs/guides/install-nixos-on-linode/ "Install and Configure NixOS on a Linode | Linode Docs")
  * [Star-History](https://star-history.com/ "Star-History") — We know, you can't fully trust a project's GitHub stars alone. It is, however, a good way to determine if a tool is an adequate one and if it's likely to grow, if you use it correctly.
  * [disko](https://github.com/nix-community/disko "disko") — NixOS is a Linux distribution where everything is described as code, with one exception: during installation, the disk partitioning and formatting are manual steps. disko aims to correct this sad 🤡 omission.
  * [nixos-anywhere](https://github.com/numtide/nixos-anywhere "nixos-anywhere") — You can then initiate an unattended installation with a single CLI command. Since nixos-anywhere can access the new machine using SSH, it's ideal for remote installations.
  * [Immutable infrastructure for mutable systems](https://grahamc.com/blog/erase-your-darlings/ "Immutable infrastructure for mutable systems") — I erase my systems at every boot.
  * [NixOS Series 4: "Stateless" Operating System](https://lantian.pub/en/article/modify-computer/nixos-impermanence.lantian/ "NixOS Series 4: "Stateless" Operating System") — Here's the question: is it really necessary to store the contents of /etc on the disk drive? They're going to be regenerated on each reboot or config switch anyway.
  * [NixOS ❄: tmpfs as root](https://elis.nu/blog/2020/05/nixos-tmpfs-as-root/ "NixOS ❄: tmpfs as root") — One fairly unique property of NixOS is the ability to boot with only /boot and /nix. Nothing else is actually required. This supports doing all sorts of weird things with your root file system.
  * [Nixos and Erasing My Darlings](https://hanckmann.com/posts/nixos-and-erasing-my-darlings/ "Nixos and Erasing My Darlings")
  * [Impermanence - NixOS Wiki](https://nixos.wiki/wiki/Impermanence "Impermanence - NixOS Wiki") — Impermanence in NixOS is where your root directory gets wiped every reboot (such as by mounting a tmpfs to /). Such a setup is possible because NixOS only needs /boot and /nix in order to boot, all other system files are simply links to files in /nix. /boot and /nix still need to be stored on a hard drive or SSD.
  * [impermanence: Modules to help you handle persistent state on systems with ephemeral root storage [maintainer=@talyz]](https://github.com/nix-community/impermanence "impermanence: Modules to help you handle persistent state on systems with ephemeral root storage \[maintainer=@talyz\]")
  * [Example ZFS + tmpfs root configuration](https://gist.github.com/ChickenParmigiana/72e5ee51bc08c07ac1bbc5ea39a90bad "Example ZFS + tmpfs root configuration")
  * [NixOS on Btrfs+tmpfs](https://cnx.gdn/blog/butter/ "NixOS on Btrfs+tmpfs")
  * [A plan to stabilize the new CLI and Flakes incrementally](https://github.com/NixOS/rfcs/pull/136 "A plan to stabilize the new CLI and Flakes incrementally") — Ever since the closing of RFC 49, we've had the new CLI and Flakes marked as experimental, with no clear plan forward.
  * [project Stratis](https://stratis-storage.github.io/ "project Stratis")
  * [Backups - Perfect Media Server](https://perfectmediaserver.com/04-day-two/backups/ "Backups - Perfect Media Server")
  * [Podverse GitHub](https://github.com/podverse/ "Podverse GitHub") — Podverse has a bounty out for Android Auto.
  * [Jay Sam Bee in Philadelphia NixOS Bounty](https://paste.docs.lol/reader/ColludeLemniscus "Jay Sam Bee in Philadelphia NixOS Bounty") — Jay has a bounty for getting Wallabag on NixOS.
  * [Self-Hosted 102: NixOS is a bit Flakey](https://selfhosted.show/102 "Self-Hosted 102: NixOS is a bit Flakey")
  * [completenoobs.com](http://completenoobs.com/ "completenoobs.com")
  * [OpenStreetMap.org](http://openstreetmap.org/ "OpenStreetMap.org") — OpenStreetMap is a map of the world, created by people like you and free to use under an open license.
  * [OSMand.net](http://osmand.net/ "OSMand.net")
  * [OSM is an extensible editor for ​OpenStreetMap](http://josm.openstreetmap.de/ "OSM is an extensible editor for ​OpenStreetMap")
  * [OSM is an extensible editor for ​OpenStreetMap](http://f-droid.org/packages/net.osmtracker/ "OSM is an extensible editor for ​OpenStreetMap")
  * [Street­Complete](http://f-droid.org/en/packages/de.westnordost.streetcomplete/ "Street­Complete") — Help to improve the OpenStreetMap with StreetComplete!
  * [nixpkg.py](https://github.com/soltros/nixpkg.py "nixpkg.py")



## Tags

[android auto](https://linuxunplugged.com/tags/android%20auto), [backups](https://linuxunplugged.com/tags/backups), [best laptops for nixos](https://linuxunplugged.com/tags/best%20laptops%20for%20nixos), [bootload](https://linuxunplugged.com/tags/bootload), [btrfs](https://linuxunplugged.com/tags/btrfs), [disko](https://linuxunplugged.com/tags/disko), [email privacy tip](https://linuxunplugged.com/tags/email%20privacy%20tip), [github star history](https://linuxunplugged.com/tags/github%20star%20history), [grub](https://linuxunplugged.com/tags/grub), [hedgedoc](https://linuxunplugged.com/tags/hedgedoc), [homelab machine](https://linuxunplugged.com/tags/homelab%20machine), [iac](https://linuxunplugged.com/tags/iac), [immutable infrastructure](https://linuxunplugged.com/tags/immutable%20infrastructure), [impermanence](https://linuxunplugged.com/tags/impermanence), [indestructible server](https://linuxunplugged.com/tags/indestructible%20server), [infrastructure as code](https://linuxunplugged.com/tags/infrastructure%20as%20code), [iron goat brewing](https://linuxunplugged.com/tags/iron%20goat%20brewing), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [linode](https://linuxunplugged.com/tags/linode), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [linuxfest northwest](https://linuxunplugged.com/tags/linuxfest%20northwest), [lvm](https://linuxunplugged.com/tags/lvm), [meetup](https://linuxunplugged.com/tags/meetup), [mesh vpn](https://linuxunplugged.com/tags/mesh%20vpn), [mobile nixos](https://linuxunplugged.com/tags/mobile%20nixos), [nix](https://linuxunplugged.com/tags/nix), [nix flakes](https://linuxunplugged.com/tags/nix%20flakes), [nixos friendly hosters](https://linuxunplugged.com/tags/nixos%20friendly%20hosters), [nixos on vps](https://linuxunplugged.com/tags/nixos%20on%20vps), [nixos server](https://linuxunplugged.com/tags/nixos%20server), [nixos wiki](https://linuxunplugged.com/tags/nixos%20wiki), [nixos-anywhere](https://linuxunplugged.com/tags/nixos-anywhere), [podverse bounty](https://linuxunplugged.com/tags/podverse%20bounty), [project cycle](https://linuxunplugged.com/tags/project%20cycle), [rollback](https://linuxunplugged.com/tags/rollback), [security](https://linuxunplugged.com/tags/security), [snapshots](https://linuxunplugged.com/tags/snapshots), [stratis](https://linuxunplugged.com/tags/stratis), [systemd](https://linuxunplugged.com/tags/systemd), [tmpfs](https://linuxunplugged.com/tags/tmpfs), [wireguard](https://linuxunplugged.com/tags/wireguard), [zfs](https://linuxunplugged.com/tags/zfs)