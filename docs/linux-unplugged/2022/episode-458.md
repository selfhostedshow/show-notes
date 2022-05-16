# LUP 458: NVIDIA's New View

<iframe src="https://player.fireside.fm/v2/RUkczH-V+D3EXDPTO?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2022-05-15
* Duration: 67 mins 13 secs

## About this episode

NVIDIA is open-sourcing their GPU drivers, but there are a few things you need to know. Plus, we get some exclusive insights into Tailscale from one of its co-founders.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)
* [Avery Pennarun](https://linuxunplugged.com/guests/avery)
* [Christian F.K. Schaller](https://linuxunplugged.com/guests/christianschaller)

## Sponsored by

  * [Linode Cloud Hosting](https://linode.com/unplugged): [A special offer for all Linux Unplugged Podcast listeners and new Linode customers, visit linode.com/unplugged, and receive $100 towards your new account. ](https://linode.com/unplugged)
  * [Bitwarden](https://bitwarden.com/linux): [Bitwarden is the easiest way for businesses and individuals to store, share, and sync sensitive data.](https://bitwarden.com/linux)



## Episode links

  * [After losing contact with its helicopter, NASA put the entire Mars mission on hold ](https://arstechnica.com/science/2022/05/after-an-amazing-run-on-mars-nasas-helicopter-faces-a-long-dark-winter/ "After losing contact with its helicopter, NASA put the entire Mars mission on hold ") — Mars is only going to get colder and darker for the next 10 weeks as winter deepens. 
  * [Why the open source driver release from NVIDIA is so important for Linux?](https://blogs.gnome.org/uraeus/2022/05/11/why-is-the-open-source-driver-release-from-nvidia-so-important-for-linux/ "Why the open source driver release from NVIDIA is so important for Linux?") — Today NVIDIA announced that they are releasing an open source kernel driver for their GPUs, so I want to share with you some background information and how I think this will impact Linux graphics and compute going forward.
  * [NVIDIA Releases Open-Source GPU Kernel Modules](https://developer.nvidia.com/blog/nvidia-releases-open-source-gpu-kernel-modules/ "NVIDIA Releases Open-Source GPU Kernel Modules") — NVIDIA is now publishing Linux GPU kernel modules as open source with dual GPL/MIT license, starting with the R515 driver release.
  * [Hector Martin on Twitter](https://twitter.com/marcan42/status/1524615058688724992 "Hector Martin on Twitter") — So NVIDIA "released" their kernel driver as open source. By which they mean, they moved most of it to firmware and made the open source driver call into it. There are almost 900 functions implemented in the 34MB firmware, give or take, from what I can see. Broadcom vibes...
  * [Longhorn on Twitter](https://twitter.com/never_released/status/1524619508694007810 "Longhorn on Twitter") — Note that the 30MB+ firmware supports multiple GPU generations, and that’s an important factor. (If you see the elf sections, there’s ones for Turing, Ampere DC, Ampere customer and Gnext)
  * [Linux Action News 240](https://linuxactionnews.com/240 "Linux Action News 240") — NVIDIA has announced its plans for an open-source GPU driver. Christian Schaller, the Director for Desktop, Graphics, Infotainment and more at Red Hat, gives us the inside scoop on this historic announcement.
  * [Tailscale raises $100M… to fix the Internet ](https://tailscale.com/blog/series-b/ "Tailscale raises $100M… to fix the Internet ") — This is not our first rodeo. We don’t know where the economy or the market are going. We don’t want to be pressured into juicing growth numbers beyond where they belong. We don’t want to put revenue ahead of quality, because our stats say quality is where all our growth comes from. 
  * [sshuttle](https://github.com/sshuttle/sshuttle "sshuttle") — where transparent proxy meets VPN meets ssh
  * [Documentation · Tailscale](https://tailscale.com/kb/ "Documentation · Tailscale") — Welcome to the Tailscale documentation
  * [Guides · Tailscale](https://tailscale.com/kb/guides/ "Guides · Tailscale")
  * [Access a Pi-hole or Raspberry Pi from anywhere](https://tailscale.com/kb/1114/pi-hole/ "Access a Pi-hole or Raspberry Pi from anywhere") — One common use of a Raspberry Pi is to run a Pi-hole, a DNS-based ad blocking services. A typical setup is to have a Raspberry Pi in your house running Pi-hole, acting as the DNS server for your local Wi-Fi network.
  * [Tailscale on NixOS: A New Minecraft Server in Ten Minutes ](https://tailscale.com/kb/1096/nixos-minecraft/ "Tailscale on NixOS: A New Minecraft Server in Ten Minutes ") — In this article I will show how to set up a brand new Minecraft server (exposed only over Tailscale) in ten minutes
  * [Tailscale in LXC containers ](https://tailscale.com/kb/1130/lxc-unprivileged/ "Tailscale in LXC containers ")
  * [Set up a dogcam with Tailscale, Raspberry Pi, and Motion ](https://tailscale.com/kb/1076/dogcam/ "Set up a dogcam with Tailscale, Raspberry Pi, and Motion ")
  * [weron: Overlay networks based on WebRTC.](https://github.com/pojntfx/weron "weron: Overlay networks based on WebRTC.") — weron provides lean, fast & secure overlay networks based on WebRTC.
  * [newpodcastapps.com](https://podcastindex.org/apps?appTypes=app&elements=Chapters%2CValue "newpodcastapps.com")
  * [Podverse](https://podverse.fm/ "Podverse")
  * [Breez ](https://breez.technology/ "Breez ") — Send a Boost without switching Podcast apps. All powered by Lightning Network.
  * [Ansible Modules Bitwarden](https://github.com/c0sco/ansible-modules-bitwarden "Ansible Modules Bitwarden") — Bitwarden integrations for Ansible



## Tags

[ansible](https://linuxunplugged.com/tags/ansible), [ansible vaults](https://linuxunplugged.com/tags/ansible%20vaults), [avery pennarun](https://linuxunplugged.com/tags/avery%20pennarun), [bitwarden](https://linuxunplugged.com/tags/bitwarden), [christian schaller](https://linuxunplugged.com/tags/christian%20schaller), [firmware blog](https://linuxunplugged.com/tags/firmware%20blog), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [lan](https://linuxunplugged.com/tags/lan), [linux action news](https://linuxunplugged.com/tags/linux%20action%20news), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [lxd](https://linuxunplugged.com/tags/lxd), [mesh network](https://linuxunplugged.com/tags/mesh%20network), [mesh vpn](https://linuxunplugged.com/tags/mesh%20vpn), [nixos](https://linuxunplugged.com/tags/nixos), [nouveau driver](https://linuxunplugged.com/tags/nouveau%20driver), [nvidia](https://linuxunplugged.com/tags/nvidia), [open source](https://linuxunplugged.com/tags/open%20source), [red hat](https://linuxunplugged.com/tags/red%20hat), [sshuttle](https://linuxunplugged.com/tags/sshuttle), [star trek](https://linuxunplugged.com/tags/star%20trek), [starlink](https://linuxunplugged.com/tags/starlink), [tailscale](https://linuxunplugged.com/tags/tailscale), [vm](https://linuxunplugged.com/tags/vm), [vpn](https://linuxunplugged.com/tags/vpn), [webrtc](https://linuxunplugged.com/tags/webrtc), [weron](https://linuxunplugged.com/tags/weron), [wireguard](https://linuxunplugged.com/tags/wireguard)