# LUP 317: Performance Picks for Kicks

<iframe src="https://player.fireside.fm/v2/RUkczH-V+jWiPfjqn?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2019-09-03
* Duration: 66 mins 27 secs

## About this episode

We take a trip to visit Level1Tech's Wendell Wilson and come back with some of his performance tips for a smoother Linux desktop.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [chzbacon](https://linuxunplugged.com/hosts/chzbacon)
* [Alex Kretzschmar](https://linuxunplugged.com/guests/alexktz)
* [Brent Gervais](https://linuxunplugged.com/guests/brentgervais)
* [Cassidy James Blaede](https://linuxunplugged.com/guests/cassidyjames)
* [Drew DeVore](https://linuxunplugged.com/guests/drewdevore)
* [Ell Marquez](https://linuxunplugged.com/guests/ell)

## Sponsored by

None



## Episode links

  * [XKCD Forum Hacked](https://thehackernews.com/2019/09/xkcd-forum-hacked.html "XKCD Forum Hacked") — The security breach occurred two months ago, according to security researcher Troy Hunt who alerted the company of the incident, with unknown hackers stealing around 562,000 usernames, email and IP addresses, as well as hashed passwords.
  * [Examining exFAT](https://lwn.net/Articles/797963/ "Examining exFAT") — Linux kernel developers like to get support for new features — such as filesystem types — merged quickly. In the case of the exFAT filesystem, that didn't happen; exFAT was created by Microsoft in 2006 for use in larger flash-storage cards, but there has never been support in the kernel for this filesystem. Microsoft's recent announcement that it wanted to get exFAT support into the mainline kernel would appear to have removed the largest obstacle to Linux exFAT support. But, as is so often the case, it seems that some challenges remain.
  * [Waypipe Is Successfully Working For This Network-Transparent Wayland Apps/Games Proxy](https://www.phoronix.com/scan.php?page=news_item&px=Waypipe-Successful-GSoC-2019 "Waypipe Is Successfully Working For This Network-Transparent Wayland Apps/Games Proxy") — Waypipe development was successful this summer by student developer Manuel Stoeckl who was working on the effort as part of this year's Google Summer of Code (GSoC). Waypipe is successfully working now for running Wayland games/applications over the network using this proxy mechanism and supports features like compression, multi-threading optimizations, and hardware-accelerated VA-API for video encode/decode across the network. 
  * [GSOC 2019 - M. Stoeckl's website](https://mstoeckl.com/notes/gsoc/blog.html "GSOC 2019 - M. Stoeckl's website") — Waypipe supports many quality of life features, including a user-friendly command line wrapper for ssh, hardware accelerated video encoding, transfer compression with either LZ4 or Zstd, and a method to reconnect applications when the ssh connection breaks. With more recent kernels and versions of Mesa that support DMABUFs (GPU-side buffers), it can proxy programs that render images using OpenGL. 
  * [What to Expect in GNOME 3.34, Out Next Week - OMG! Ubuntu!](https://www.omgubuntu.co.uk/2019/09/best-gnome-3-34-features/amp "What to Expect in GNOME 3.34, Out Next Week - OMG! Ubuntu!") — GNOME 3.34 makes it MUCH easier to create app folders in the GNOME Shell ‘Application Overview’, i.e. the grid of app shortcuts you see when pressing the All Apps icon on the Ubuntu Dock. 
  * [GNOME 3.34's Mutter Lands A Last-Minute Performance Fix For NVIDIA](https://www.phoronix.com/scan.php?page=news_item&px=GNOME-3.34-Last-Minute-NVIDIA "GNOME 3.34's Mutter Lands A Last-Minute Performance Fix For NVIDIA") — Canonical's Daniel van Vugt who is known for his many GNOME performance optimizations over the past two years has been toying with this NVIDIA fix/optimization the past few months and merged the code this morning to Mutter. This change that landed is the removal of GLX threaded swap wait handling for the NVIDIA binary driver. 
  * [Geometric Picking Finally Lands In GNOME/Mutter 3.34 For Lowering CPU Usage](https://www.phoronix.com/scan.php?page=news_item&px=GNOME-3.34-Geometric-Picking "Geometric Picking Finally Lands In GNOME/Mutter 3.34 For Lowering CPU Usage") — This is about cursor movement and now avoiding OpenGL/GPU usage for the color picking operations. That logic is now being done on the CPU without OpenGL but turns out is more efficiently done this way and is able to cause a measurable drop in CPU usage when moving the mouse cursor and especially when moving around windows.
  * [Geometric (OpenGL-less) picking · GNOME / mutter · GitLab)](https://gitlab.gnome.org/GNOME/mutter/merge_requests/189 "Geometric \(OpenGL-less\) picking  · GNOME / mutter · GitLab\)") — By avoiding OpenGL and the graphics driver we also reduce CPU usage. Despite reimplementing the logic on the CPU, it still takes less CPU time than going through GL did. 
  * [GTK, Adwaita, and Vendor Styles - Platform - GNOME Discourse](https://discourse.gnome.org/t/gtk-adwaita-and-vendor-styles/1641 "GTK, Adwaita, and Vendor Styles - Platform - GNOME Discourse") — After the BoF, we decided to continue the discussion and find actionable items to move things forward to improve Adwaita itself, the situation for app developers, and the experience for downstream vendors that wish to ship a distinct visual style. We decided that continuing here on Discourse is a good plan to keep the discussion persistent and centralized. 
  * [The Need for a FreeDesktop Dark Style Preference - GUADEC 2019 - Videos](https://guadec.ubicast.tv/videos/the-need-for-a-freedesktop-dark-style-preference/ "The Need for a FreeDesktop Dark Style Preference - GUADEC 2019 - Videos") — Cassidy has been observing and researching dark styles in consumer software for several months, and conducted a user study with over 1,500 participants. In this talk he shares his research, observations, prior art, and requirements for a dark style preference on FreeDesktop platforms. 
  * [gamemode](https://github.com/FeralInteractive/gamemode "gamemode") — GameMode is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process. 
  * [Free Courses at Linux Academy — September 2019 – Linux Academy](https://linuxacademy.com/blog/uncategorized/free-courses-at-linux-academy-september-2019/ "Free Courses at Linux Academy — September 2019 – Linux Academy") — On September 17th Linux Torvald first released the Linux Operating System Kernel on September 17th, 1991 so we are celebrating by offering free training for you to increase your Linux Skills. 
  * [Texas Cyber Summit](https://www.texascybersummit.org/ "Texas Cyber Summit") — October 10th-12th in San Antonio, Texas.
  * [Unofficial Hacker Family Dinner & Unbirthday Party | Meetup](https://www.meetup.com/jupiterbroadcasting/events/262984590/ "Unofficial Hacker Family Dinner & Unbirthday Party | Meetup") — Join us for a meet and greet with fellow Texas Cyber Summit attendees and a belated celebration of Ell and Allie's Birthdays! There will be good food, good friends, and we hope some good conversation. 
  * [Level1Linux Channel](https://www.youtube.com/channel/UCOWcZ6Wicl-1N34H0zZe38w "Level1Linux Channel")
  * [Chatting With Alex and Chris From The Self Hosted Podcast! - Level1Linux](https://www.youtube.com/watch?v=8ZZJu0uty9E "Chatting With Alex and Chris From The Self Hosted Podcast! - Level1Linux")
  * [cpufreq - GNOME Shell Extensions](https://extensions.gnome.org/extension/1082/cpufreq/ "cpufreq - GNOME Shell Extensions") — This is a lightweight CPU frequency scaling monitor and powerful CPU management tool. The extension is using standard cpufreq kernel modules to collect information and manage governors. It needs root permission to able changing governors. 
  * [i7z](https://code.google.com/archive/p/i7z/ "i7z") — A better i7 (and now i3, i5) reporting tool for Linux.
  * [CPUFREQ Extension](http://konkor.github.io/cpufreq/ "CPUFREQ Extension")
  * [throttled](https://github.com/erpalma/throttled "throttled") — Workaround for Intel throttling issues in Linux. 
  * [Re: [X1C6/T480s] low cTDP and trip temperature in Linux - Page 9 - Lenovo Community](https://forums.lenovo.com/t5/Other-Linux-Discussions/X1C6-T480s-low-cTDP-and-trip-temperature-in-Linux/m-p/4513821#M13563 "Re: \[X1C6/T480s\] low cTDP and trip temperature in Linux - Page 9 - Lenovo Community") — The good news: This problem is being very actively investigated and we (Lenovo) hope to have a solution soon. 
  * [Jupiter.Gallery](https://jupiter.gallery/# "Jupiter.Gallery") — Our self-hosted photo gallery powered by Lychee. Send your photos to chz at jupiterbroadcasting.com.
  * [Lychee](https://github.com/LycheeOrg/Lychee/ "Lychee") — A great looking and easy-to-use photo-management-system you can run on your server, to manage and share photos.
  * [Audio in Linux question](https://slexy.org/view/s2Q91OadFn "Audio in Linux question") — Is there something lacking in our ALSA/JACK/PuleAudio stack that I'm not aware of? We obviously can do pro audio production, given Ardour, REAPER and even Audacity. What's missing?
  * [zFRAG by LostTrainDude](https://losttraindude.itch.io/zfrag "zFRAG by LostTrainDude") — Defrag your mind by manually defragging a virtual Hard Disk, sector by sector, or enable the AUTODEFRAG to sit back and watch it do it on its own. 
  * [meshroom: 3D Reconstruction Software](https://github.com/alicevision/meshroom "meshroom: 3D Reconstruction Software") — Meshroom is a free, open-source 3D Reconstruction Software based on the AliceVision Photogrammetric Computer Vision framework.



## Tags

[adwaita](https://linuxunplugged.com/tags/adwaita), [cpu tuning](https://linuxunplugged.com/tags/cpu%20tuning), [cpufreq](https://linuxunplugged.com/tags/cpufreq), [dark mode](https://linuxunplugged.com/tags/dark%20mode), [dark style preference](https://linuxunplugged.com/tags/dark%20style%20preference), [exfat](https://linuxunplugged.com/tags/exfat), [freedesktop](https://linuxunplugged.com/tags/freedesktop), [game mode](https://linuxunplugged.com/tags/game%20mode), [geometric picking](https://linuxunplugged.com/tags/geometric%20picking), [gnome](https://linuxunplugged.com/tags/gnome), [gnome 3.34](https://linuxunplugged.com/tags/gnome%203.34), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [level1tech](https://linuxunplugged.com/tags/level1tech), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [meshroom](https://linuxunplugged.com/tags/meshroom), [microsoft](https://linuxunplugged.com/tags/microsoft), [mutter](https://linuxunplugged.com/tags/mutter), [network transparency](https://linuxunplugged.com/tags/network%20transparency), [nvidia](https://linuxunplugged.com/tags/nvidia), [open invention network](https://linuxunplugged.com/tags/open%20invention%20network), [performance](https://linuxunplugged.com/tags/performance), [photogrammetry](https://linuxunplugged.com/tags/photogrammetry), [remote desktop](https://linuxunplugged.com/tags/remote%20desktop), [throttling](https://linuxunplugged.com/tags/throttling), [unplugged](https://linuxunplugged.com/tags/unplugged), [vendor themes](https://linuxunplugged.com/tags/vendor%20themes), [wayland](https://linuxunplugged.com/tags/wayland), [waypipe](https://linuxunplugged.com/tags/waypipe), [wendell wilson](https://linuxunplugged.com/tags/wendell%20wilson), [xkcd](https://linuxunplugged.com/tags/xkcd)