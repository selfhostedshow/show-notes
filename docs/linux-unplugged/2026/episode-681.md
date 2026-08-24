# LUP 681: Ain’t Nothing But a Syncthing

<iframe src="https://player.fireside.fm/v3/RUkczH-V+h7LNk0eh?theme=dark" width="100%" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2026-08-23
* Duration: 95 mins 19 secs

## About this episode

Syncthing saves the day in an unexpected way, and we dig into what’s new in Linux 7.2.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Jupiter Party Annual Membership](https://jupitersignal.memberful.com/checkout?plan=117630r): [Put your support on automatic with our annual plan, and get one month of membership for free!](https://jupitersignal.memberful.com/checkout?plan=117630r)
  * [Managed Nebula](https://defined.net/unplugged): [Meet Managed Nebula from Defined Networking. A decentralized VPN built on the open-source Nebula platform that we love.](https://defined.net/unplugged)



## Episode links

  * [Web Boost](https://boost.jupiterbroadcasting.com/?show=lup "Web Boost") — Send us a boost via sats or USD
  * [💥 Gets Sats Quick and Easy with Strike](https://strike.me/ "💥 Gets Sats Quick and Easy with Strike")
  * [📻 LINUX Unplugged on Fountain.FM](https://www.fountain.fm/show/dWiuBeqpDSM86AwXRXov "📻 LINUX Unplugged on Fountain.FM")
  * [Jupiter Garage SWAG](https://www.jupitergarage.com/ "Jupiter Garage SWAG")
  * [AppleTalk 1985-2026 Memorial Sticker](https://www.jupitergarage.com/product/appletalk-1985-2026-memorial-sticker "AppleTalk 1985-2026 Memorial Sticker")
  * [Sorry, I only open regular files Sticker](https://www.jupitergarage.com/product/sorry-not-sorry "Sorry, I only open regular files Sticker")
  * [Longtime Linux CIFS/SMB3 Maintainer Passes Away](https://www.phoronix.com/news/SMB3-CIFS-Maintainer-Change "Longtime Linux CIFS/SMB3 Maintainer Passes Away")
  * [Linux 7.2 Kernel Newbies](https://kernelnewbies.org/Linux_7.2 "Linux 7.2 Kernel Newbies")
  * [Cache Aware Scheduling Merged For Linux 7.2 For Boosting Modern Intel & AMD CPUs](https://www.phoronix.com/news/Linux-7.2-Scheduler "Cache Aware Scheduling Merged For Linux 7.2 For Boosting Modern Intel & AMD CPUs")
  * [Linux 7.2 To Revert Back To The FIFO DRM Scheduler Policy Due To "Fair" Regressions](https://www.phoronix.com/news/Linux-7.2-Reverting-DRM-Fair "Linux 7.2 To Revert Back To The FIFO DRM Scheduler Policy Due To "Fair" Regressions")
  * [[REGRESSION] drm/sched: FAIR policy causes serious performance degradation at max GPU load on 9070XT](https://www.spinics.net/lists/kernel/msg6369442.html "\[REGRESSION\] drm/sched: FAIR policy causes serious performance degradation at max GPU load on 9070XT")
  * [reduce pipe->mutex contention by pre-allocating outside the lock](https://lore.kernel.org/linux-fsdevel/20260524-fix_pipe-v3-0-bb4a75d23a90@debian.org/ "reduce pipe->mutex contention by pre-allocating outside the lock") — While profiling Meta's caching code, I found pipe->mutex contention on the hot path. anon_pipe_write() currently calls alloc_page() once per page while holding pipe->mutex. The allocation can sleep doing direct reclaim and runs memcg charging, which extends the critical section and stalls any concurrent reader on the same mutex.
  * [Linux Finally Eliminates The strncpy API After Six Years Of Work, 360+ Patches](https://www.phoronix.com/news/Linux-7.2-Drops-strncpy "Linux Finally Eliminates The strncpy API After Six Years Of Work, 360+ Patches")
  * [Specially Crafted NTFS File-System Image Allows Root Access On Linux With NTFS3 Driver](https://www.phoronix.com/news/NTFS3-Vulnerability-For-Root "Specially Crafted NTFS File-System Image Allows Root Access On Linux With NTFS3 Driver")
  * [The beginning of the 7.3 merge window](https://lwn.net/SubscriberLink/1089244/65c1d71cc2f5185b/ "The beginning of the 7.3 merge window")
  * [Linux 7.3 SMP Improvement To Help Reduce Latency, Improve Real-Time Performance](https://www.phoronix.com/news/Linux-7.3-SMP "Linux 7.3 SMP Improvement To Help Reduce Latency, Improve Real-Time Performance")
  * [Linux 7.3 Expected To "Flatten The Pick" For Better Scheduling While Gaming & More](https://www.phoronix.com/news/Linux-7.3-Flattens-The-Pick "Linux 7.3 Expected To "Flatten The Pick" For Better Scheduling While Gaming & More")
  * [Linux 7.3 x86/mm Lands Patches To Greatly Improve Latency-Sensitive Workloads](https://www.phoronix.com/news/Linux-7.3-x86-mm-Latency "Linux 7.3 x86/mm Lands Patches To Greatly Improve Latency-Sensitive Workloads")
  * [Sched_ext's Sub-Scheduler Support Now "Feature Complete" With Linux 7.3](https://www.phoronix.com/news/Linux-7.3-sched-ext "Sched_ext's Sub-Scheduler Support Now "Feature Complete" With Linux 7.3")
  * [Btrfs Ready With More Performance Improvements For Linux 7.3: Some ~3x To ~5x Wins](https://www.phoronix.com/news/Linux-7.3-Btrfs "Btrfs Ready With More Performance Improvements For Linux 7.3: Some ~3x To ~5x Wins")
  * [Linux 7.3 binfmt_misc To Allow BPF Programs To Dynamically Choose Execution Environments](https://www.phoronix.com/news/Linux-7.3-binfmt-misc "Linux 7.3 binfmt_misc To Allow BPF Programs To Dynamically Choose Execution Environments")
  * [Linux 7.3 drops support for two ancient file systems](https://www.neowin.net/news/linux-73-merge-window-kicks-off-by-throwing-out-two-ancient-file-systems/ "Linux 7.3 drops support for two ancient file systems")
  * [Linux 7.3 Network Changes Merged But Developers "Completely Overwhelmed" Due To AI/LLMs](https://www.phoronix.com/news/Linux-7.3-Networking "Linux 7.3 Network Changes Merged But Developers "Completely Overwhelmed" Due To AI/LLMs")
  * [Two Very Exciting Memory Management Optimizations Going Into Linux 7.3](https://www.phoronix.com/news/Linux-7.3-MM "Two Very Exciting Memory Management Optimizations Going Into Linux 7.3")
  * [Syncthing](https://syncthing.net/ "Syncthing") — Syncthing is a continuous file synchronization program. It synchronizes files between two or more computers in real time, safely protected from prying eyes
  * [Syncthing GitHub](https://github.com/syncthing/syncthing "Syncthing GitHub")
  * [Rclone](https://rclone.org/ "Rclone") — Feature-rich alternative to cloud storage vendors' web storage interfaces.
  * [LocalComet](https://github.com/AleksSmash2019/LocalComet "LocalComet") — A private, local-first Windows AI assistant built and validated with Codex.
  * [A look at the Quickshell desktop-component toolkit](https://lwn.net/Articles/1083090/ "A look at the Quickshell desktop-component toolkit")
  * [MCP-NixOS - Model Context Protocol for NixOS](https://mcp-nixos.io/ "MCP-NixOS - Model Context Protocol for NixOS") — Because your AI shouldn't hallucinate package names.
  * [dataiku/kiji-proxy](https://github.com/dataiku/kiji-proxy "dataiku/kiji-proxy") — Privacy proxy for your OpenAI requests
  * [Rockbox - Free Music Player Firmware](https://www.rockbox.org/ "Rockbox - Free Music Player Firmware")
  * [Pick: ssh-clipboard](https://ssh-clipboard.standardagents.ai/ "Pick: ssh-clipboard") — Peer-to-peer clipboard sync over SSH. Copy anything on one machine, paste on another. Open source, and Written in Rust ackchyually.



## Tags

[ad blocking](https://linuxunplugged.com/tags/ad%20blocking), [adblockplus](https://linuxunplugged.com/tags/adblockplus), [ai agents](https://linuxunplugged.com/tags/ai%20agents), [ai security](https://linuxunplugged.com/tags/ai%20security), [aleks](https://linuxunplugged.com/tags/aleks), [andrew morton](https://linuxunplugged.com/tags/andrew%20morton), [api](https://linuxunplugged.com/tags/api), [awtrix](https://linuxunplugged.com/tags/awtrix), [bpf](https://linuxunplugged.com/tags/bpf), [btrfs](https://linuxunplugged.com/tags/btrfs), [cache-aware scheduling](https://linuxunplugged.com/tags/cache-aware%20scheduling), [cifs](https://linuxunplugged.com/tags/cifs), [cpu scheduler](https://linuxunplugged.com/tags/cpu%20scheduler), [dropbox](https://linuxunplugged.com/tags/dropbox), [failfs](https://linuxunplugged.com/tags/failfs), [file sync](https://linuxunplugged.com/tags/file%20sync), [filesystems](https://linuxunplugged.com/tags/filesystems), [firefox](https://linuxunplugged.com/tags/firefox), [frigate](https://linuxunplugged.com/tags/frigate), [garuda](https://linuxunplugged.com/tags/garuda), [gpu scheduler](https://linuxunplugged.com/tags/gpu%20scheduler), [grapheneos](https://linuxunplugged.com/tags/grapheneos), [hermes-syncthing](https://linuxunplugged.com/tags/hermes-syncthing), [home assistant](https://linuxunplugged.com/tags/home%20assistant), [home automation](https://linuxunplugged.com/tags/home%20automation), [hyprland](https://linuxunplugged.com/tags/hyprland), [igalia](https://linuxunplugged.com/tags/igalia), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kicinski](https://linuxunplugged.com/tags/kicinski), [kiji-proxy](https://linuxunplugged.com/tags/kiji-proxy), [linus torvalds](https://linuxunplugged.com/tags/linus%20torvalds), [linux 7.2](https://linuxunplugged.com/tags/linux%207.2), [linux 7.3](https://linuxunplugged.com/tags/linux%207.3), [linux kernel](https://linuxunplugged.com/tags/linux%20kernel), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [local llm](https://linuxunplugged.com/tags/local%20llm), [localcomet](https://linuxunplugged.com/tags/localcomet), [maestral](https://linuxunplugged.com/tags/maestral), [mcp-nixos](https://linuxunplugged.com/tags/mcp-nixos), [memory management](https://linuxunplugged.com/tags/memory%20management), [namjae jeon](https://linuxunplugged.com/tags/namjae%20jeon), [nixos](https://linuxunplugged.com/tags/nixos), [ntfs](https://linuxunplugged.com/tags/ntfs), [ntfs vulnerability](https://linuxunplugged.com/tags/ntfs%20vulnerability), [omarchy](https://linuxunplugged.com/tags/omarchy), [open source](https://linuxunplugged.com/tags/open%20source), [paragon software](https://linuxunplugged.com/tags/paragon%20software), [paulo alcantara](https://linuxunplugged.com/tags/paulo%20alcantara), [peer-to-peer sync](https://linuxunplugged.com/tags/peer-to-peer%20sync), [peter zijlstra](https://linuxunplugged.com/tags/peter%20zijlstra), [quickshell](https://linuxunplugged.com/tags/quickshell), [rclone](https://linuxunplugged.com/tags/rclone), [rockbox](https://linuxunplugged.com/tags/rockbox), [sandboxing](https://linuxunplugged.com/tags/sandboxing), [security](https://linuxunplugged.com/tags/security), [self-hosting](https://linuxunplugged.com/tags/self-hosting), [smb3](https://linuxunplugged.com/tags/smb3), [ssh-clipboard](https://linuxunplugged.com/tags/ssh-clipboard), [steve french](https://linuxunplugged.com/tags/steve%20french), [storage encryption](https://linuxunplugged.com/tags/storage%20encryption), [swap](https://linuxunplugged.com/tags/swap), [syncthing](https://linuxunplugged.com/tags/syncthing), [tauri](https://linuxunplugged.com/tags/tauri), [tvrtko ursulin](https://linuxunplugged.com/tags/tvrtko%20ursulin), [usb4stream](https://linuxunplugged.com/tags/usb4stream), [🐒🥧](https://linuxunplugged.com/tags/%F0%9F%90%92%F0%9F%A5%A7)