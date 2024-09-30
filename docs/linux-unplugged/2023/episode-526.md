# LUP 526: Canonical Wins by Default

<iframe src="https://player.fireside.fm/v2/RUkczH-V+HMSq9ihv?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2023-09-03
* Duration: 49 mins 20 secs

## About this episode

While chaos is brewing in SUSE and Red Hat land, Canonical stays the course and doubles down on the Linux desktop. Plus, our thoughts on the kernel team GPL-blocking NVIDIA.

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)

## Sponsored by

  * [Tailscale](http://tailscale.com/linuxunplugged): [Tailscale is a programmable networking software that is private and secure by default - get it free on up to 100 devices!](http://tailscale.com/linuxunplugged)
  * [Linode Cloud Hosting](https://linode.com/unplugged): [A special offer for all Linux Unplugged Podcast listeners and new Linode customers, visit linode.com/unplugged, and receive $100 towards your new account. ](https://linode.com/unplugged)
  * [Kolide](https://kolide.com/unplugged): [Kolide is a device trust solution for companies with Okta, and they ensure that if a device isn’t trusted and secure, it can’t log into your cloud apps.](https://kolide.com/unplugged)



## Episode links

  * [jblive.fm](http://jblive.fm/ "jblive.fm") — Jupiter Broadcasting Live Audio Stream
  * [🎉 Alby](https://getalby.com/ "🎉 Alby") — Boost into the show, first grab Alby, top it off, and then head over to the Podcast Index.
  * [⚡️ LINUX Unplugged on the Podcastindex.org](https://podcastindex.org/podcast/575694 "⚡️ LINUX Unplugged on the Podcastindex.org") — You can boost from the web. Once Alby is topped off, visit our page on the Podcast Index.
  * [AMD Open-Source GPU Kernel Driver Above 5 Million Lines, Entire Linux Kernel At 34.8 Million](https://www.phoronix.com/news/AMD-5-Million-Lines "AMD Open-Source GPU Kernel Driver Above 5 Million Lines, Entire Linux Kernel At 34.8 Million")
  * [Making life (even) harder for proprietary modules](https://lwn.net/Articles/939842/ "Making life \(even\) harder for proprietary modules") — It changes the behavior of symbol_get(), causing it to fail when asked to look up a symbol that is not marked GPL-only. This is an inversion of the usual test, which denies access to symbols that are marked GPL-only. The reasoning is that symbol_get() has always been intended for low-level cooperation deep within the kernel, where everything is expected to be GPL-only anyway.
  * [Linux 6.6 To Better Protect Against The Illicit Behavior Of NVIDIA’s Proprietary Driver](https://www.phoronix.com/news/Linux-6.6-Illicit-NVIDIA-Change "Linux 6.6 To Better Protect Against The Illicit Behavior Of NVIDIA’s Proprietary Driver") — Back in 2020 when the original defense was added, NVIDIA recommended avoiding the Linux 5.9 for the time being. They ended up having a supported driver several weeks later. It will be interesting to see this time how long Linux 6.6+ thwarts their kernel driver.
  * [[Hacker News] Making life (even) harder for proprietary modules](https://news.ycombinator.com/item?id=37319537 "\[Hacker News\] Making life \(even\) harder for proprietary modules")
  * [PATCH: modules: only allow symbol_get of EXPORT_SYMBOL_GPL modules](https://lore.kernel.org/lkml/20230731083806.453036-6-hch@lst.de/ "PATCH: modules: only allow symbol_get of EXPORT_SYMBOL_GPL modules") — Given that symbol_get was only ever inteded for tightly cooperating modules using very internal symbols it is logical to restrict it to being used on EXPORY_SYMBOL_GPL and prevent nvidia from costly DMCA circumvention of access controls law suites.
  * [Ubuntu Desktop: Charting a course for the future](https://discourse.ubuntu.com/t/ubuntu-desktop-charting-a-course-for-the-future/38092 "Ubuntu Desktop: Charting a course for the future") — Recently, we embarked on an internal exercise to consolidate and bring structure to our values and goals for how we plan to evolve the desktop experience over the next few years. This post is designed to share the output of those discussions and give insight into the direction we’re going.
  * [Ubuntu Desktop “Charting A Course For The Future” With Ubuntu 24.04 LTS Next Year](https://www.phoronix.com/news/Ubuntu-Desktop-2023-Future "Ubuntu Desktop “Charting A Course For The Future” With Ubuntu 24.04 LTS Next Year")
  * [Leap Replacement Discussion](https://lists.opensuse.org/archives/list/factory@lists.opensuse.org/thread/KJMMAZFTP2MPKWKFZCYUROZFJ44BNVB5/ "Leap Replacement Discussion") — I've been looking at the results from the recent contributor survey to gauge the interest and feasibility of replacing openSUSE Leap with a new community-built offering.
  * [Linux’s Marketshare on Steam Still Higher Than Apple macOS](https://linux.slashdot.org/story/23/09/03/001201/linuxs-marketshare-on-steam-still-higher-than-apple-macos?utm_source=rss1.0mainlinkanon&utm_medium=feed "Linux’s Marketshare on Steam Still Higher Than Apple macOS")
  * [Wavlake](https://www.wavlake.com/ "Wavlake") — We envision a new, online world where creators and listeners can freely transact with one another in an open ecosystem.
  * [Music Side Project Studio](https://musicsideproject.com/ "Music Side Project Studio")
  * [The Boostagram Ball](https://www.boostagramball.com/episodes/ "The Boostagram Ball")
  * [The Fairly Fun Show](https://podcastindex.org/podcast/6567390 "The Fairly Fun Show")
  * [DJ V4V Podcast | All music - no Talk](https://podcastindex.org/podcast/6583461 "DJ V4V Podcast | All music - no Talk")
  * [Before The Sch3m3s 8.21.2023 - Behind the SchƎmƎs](https://podverse.fm/episode/ovlSm2_j1 "Before The Sch3m3s 8.21.2023 - Behind the SchƎmƎs")
  * [V4V SHOW](https://www.meremortalspodcast.com/value4value/episode/c1a803d5/how-to-access-v4v-music-or-the-hurdles-to-supporting-musicians-and-artists "V4V SHOW") — How To Access V4V Music
  * [Office Hours 34](https://www.officehours.hair/34 "Office Hours 34") — Podcast Bounty Hunters
  * [[YouTube] Free Secure Phone Calls. Private Network Coms Access](https://youtu.be/6MD2Sm9S9Yo?si=t5k5-6XjTLqxhIsZ "\[YouTube\] Free Secure Phone Calls. Private Network Coms Access")



## Tags

[alp](https://linuxunplugged.com/tags/alp), [amd](https://linuxunplugged.com/tags/amd), [amdgpu](https://linuxunplugged.com/tags/amdgpu), [canonical](https://linuxunplugged.com/tags/canonical), [christoph hellwig](https://linuxunplugged.com/tags/christoph%20hellwig), [chromium](https://linuxunplugged.com/tags/chromium), [copyleft](https://linuxunplugged.com/tags/copyleft), [copyright](https://linuxunplugged.com/tags/copyright), [dmca](https://linuxunplugged.com/tags/dmca), [drm](https://linuxunplugged.com/tags/drm), [export_symbol_gpl](https://linuxunplugged.com/tags/export_symbol_gpl), [fedora](https://linuxunplugged.com/tags/fedora), [framework](https://linuxunplugged.com/tags/framework), [framework laptop](https://linuxunplugged.com/tags/framework%20laptop), [gpl](https://linuxunplugged.com/tags/gpl), [gpl condom](https://linuxunplugged.com/tags/gpl%20condom), [graphics drivers](https://linuxunplugged.com/tags/graphics%20drivers), [i915](https://linuxunplugged.com/tags/i915), [intel](https://linuxunplugged.com/tags/intel), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kernel driver](https://linuxunplugged.com/tags/kernel%20driver), [kernel modules](https://linuxunplugged.com/tags/kernel%20modules), [leap](https://linuxunplugged.com/tags/leap), [linux 6.6](https://linuxunplugged.com/tags/linux%206.6), [linux desktop](https://linuxunplugged.com/tags/linux%20desktop), [linux desktop investment](https://linuxunplugged.com/tags/linux%20desktop%20investment), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [lts](https://linuxunplugged.com/tags/lts), [luis chamberlain](https://linuxunplugged.com/tags/luis%20chamberlain), [nouveau](https://linuxunplugged.com/tags/nouveau), [nvidia](https://linuxunplugged.com/tags/nvidia), [oliver smith](https://linuxunplugged.com/tags/oliver%20smith), [opensuse](https://linuxunplugged.com/tags/opensuse), [red hat](https://linuxunplugged.com/tags/red%20hat), [rhel](https://linuxunplugged.com/tags/rhel), [snap packages](https://linuxunplugged.com/tags/snap%20packages), [snapcraft](https://linuxunplugged.com/tags/snapcraft), [suse](https://linuxunplugged.com/tags/suse), [taint_proprietary_module](https://linuxunplugged.com/tags/taint_proprietary_module), [ubuntu 23.10](https://linuxunplugged.com/tags/ubuntu%2023.10), [ubuntu 24.04](https://linuxunplugged.com/tags/ubuntu%2024.04), [ubuntu core](https://linuxunplugged.com/tags/ubuntu%20core), [ubuntu desktop](https://linuxunplugged.com/tags/ubuntu%20desktop), [v4v music](https://linuxunplugged.com/tags/v4v%20music), [value4value music](https://linuxunplugged.com/tags/value4value%20music), [voip](https://linuxunplugged.com/tags/voip), [wavlake](https://linuxunplugged.com/tags/wavlake), [zfs](https://linuxunplugged.com/tags/zfs)