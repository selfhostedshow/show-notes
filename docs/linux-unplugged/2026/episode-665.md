# LUP 665: Patch Me If You Can

<iframe src="https://player.fireside.fm/v3/RUkczH-V+03JRT3oG?theme=dark" width="100%" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2026-05-03
* Duration: 80 mins 41 secs

## About this episode

We dig into the Copy Fail vulnerability and test a proof-of-concept against our own box. Plus, Jon Seager, VP of Engineering at Canonical joins us, and we kick off the BSD Challenge!

## Your hosts
* [Chris Fisher](https://linuxunplugged.com/hosts/chrislas)
* [Wes Payne](https://linuxunplugged.com/hosts/wes)
* [Brent Gervais](https://linuxunplugged.com/hosts/brent)
* [Jon Seager](https://linuxunplugged.com/guests/seager)

## Sponsored by

  * [Jupiter Party Annual Membership](https://jupitersignal.memberful.com/checkout?plan=117630r): [Put your support on automatic with our annual plan, and get one month of membership for free!](https://jupitersignal.memberful.com/checkout?plan=117630r)
  * [Managed Nebula](https://defined.net/unplugged): [Meet Managed Nebula from Defined Networking. A decentralized VPN built on the open-source Nebula platform that we love.](https://defined.net/unplugged)



## Episode links

  * [💥 Gets Sats Quick and Easy with Strike](https://strike.me/ "💥 Gets Sats Quick and Easy with Strike")
  * [📻 LINUX Unplugged on Fountain.FM](https://www.fountain.fm/show/dWiuBeqpDSM86AwXRXov "📻 LINUX Unplugged on Fountain.FM")
  * [Copy Fail — CVE-2026-31431](https://copy.fail/#exploit "Copy Fail — CVE-2026-31431") — "An unprivileged local user can write four controlled bytes into the page cache of any readable file on a Linux system, and use that to gain root." — Theori
  * [Copy Fail: 732 Bytes to Root - Xint](https://xint.io/blog/copy-fail-linux-distributions "Copy Fail: 732 Bytes to Root - Xint") — "A single 732-byte Python script can edit a setuid binary and obtain root on essentially all Linux distributions shipped since 2017." — Xint
  * [Linux Kernel Bug Explained - Jorijn](https://jorijn.com/en/blog/copy-fail-cve-2026-31431-linux-kernel-bug-explained/ "Linux Kernel Bug Explained - Jorijn") — "CopyFail is more portable. One script, every distro, no offsets. Dirty Pipe needed kernel ≥ 5.8; Copy Fail covers 2017–2026." — Jorijn"Kubernetes Pod Security Standards (Restricted) and default seccomp do NOT block the syscall used." — Jorijn
  * [Ars: Most Severe Linux Threat in Years](https://arstechnica.com/security/2026/04/as-the-most-severe-linux-threat-in-years-surfaces-the-world-scrambles/ "Ars: Most Severe Linux Threat in Years") — "The most severe Linux threat to surface in years catches the world flat-footed." — Ars Technica
  * [Sysdig: CVE-2026-31431 Analysis](https://www.sysdig.com/blog/cve-2026-31431-copy-fail-linux-kernel-flaw-lets-local-users-gain-root-in-seconds/ "Sysdig: CVE-2026-31431 Analysis") — "The flaw was introduced in 2017 via commit 72548b093ee3, which switched AEAD operations to in-place processing." — Sysdig
  * [CERT-EU Advisory](https://cert.europa.eu/publications/security-advisories/2026-005/ "CERT-EU Advisory")
  * [Ubuntu Security Tracker](https://ubuntu.com/security/CVE-2026-31431 "Ubuntu Security Tracker")
  * [The Register: Crypto Flaw](https://www.theregister.com/2026/04/30/linux_cryptographic_code_flaw/ "The Register: Crypto Flaw")
  * [Kernel Patch (reverts 2017 optimization)](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5.diff "Kernel Patch \(reverts 2017 optimization\)") — "This mostly reverts commit 72548b093ee3 except for the copying of the associated data." — Kernel Commit
  * [Buggy Commit: 72548b093ee3 (2017)](https://github.com/torvalds/linux/commit/72548b093ee3 "Buggy Commit: 72548b093ee3 \(2017\)")
  * [DeepWiki: AF_ALG Internals](https://deepwiki.com/theori-io/copy-fail-CVE-2026-31431/3.1-linux-crypto-api-\(af_alg\)-internals "DeepWiki: AF_ALG Internals")
  * [oss-security Disclosure](https://www.openwall.com/lists/oss-security/2026/04/29/23 "oss-security Disclosure")
  * [PSA + GRUB Mitigation - Jan Wildeboer](https://jan.wildeboer.net/2026/05/PSA-CopyFail-CVE-2026-31431/ "PSA + GRUB Mitigation - Jan Wildeboer")
  * [Ubuntu 26.04 LTS (Resolute Raccoon) Released](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon "Ubuntu 26.04 LTS \(Resolute Raccoon\) Released") — "Ubuntu 26.04 LTS sets the example for providing best-in-class resilience while simultaneously embracing innovation and the advancement of open source." — Jon Seager, VP Ubuntu Engineering
  * [The Future of AI in Ubuntu - Jon Seager](https://discourse.ubuntu.com/t/the-future-of-ai-in-ubuntu/81130 "The Future of AI in Ubuntu - Jon Seager") — "Throughout 2026 we'll be working on enabling access to frontier AI for Ubuntu users in a way that is deliberate, secure, and aligned with our open source values." — Jon Seager
  * [Ubuntu 26.04 Release Notes](https://documentation.ubuntu.com/release-notes/26.04/ "Ubuntu 26.04 Release Notes")
  * [Ubuntu AI Features Throughout 2026 - Phoronix](https://www.phoronix.com/news/Ubuntu-AI-Features-2026 "Ubuntu AI Features Throughout 2026 - Phoronix") — "Canonical's approach to AI is refreshingly thoughtful — Microsoft should take note." — ZDNet
  * [Canonical DDoS Attack Update](https://discourse.ubuntu.com/t/update-concerning-ddos-attack-on-canonical-and-ubuntu/81482 "Canonical DDoS Attack Update") — "Canonical's web infrastructure is under a sustained, cross-border attack and we are working to address it." — arcticp, Canonical
  * [Ubuntu Weekly Newsletter #942](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-942/81204 "Ubuntu Weekly Newsletter #942")
  * [Canonical AI Approach - ZDNet](https://www.zdnet.com/article/canonical-ai-approach-thoughtful-microsoft-should-take-note/ "Canonical AI Approach - ZDNet")
  * [9to5Linux: Opt-In LLM Tools](https://9to5linux.com/canonical-plans-to-integrate-opt-in-llm-based-tools-in-future-ubuntu-releases/ "9to5Linux: Opt-In LLM Tools")
  * [uutils/coreutils: Cross-platform Rust rewrite of the GNU coreutils](https://github.com/uutils/coreutils "uutils/coreutils: Cross-platform Rust rewrite of the GNU coreutils")
  * [LINUX Unplugged 636: Engineering the Future](https://linuxunplugged.com/636 "LINUX Unplugged 636: Engineering the Future")
  * [LiveCD fails to start X session on QEMU · Issue #354 · ghostbsd/issues](https://github.com/ghostbsd/issues/issues/354 "LiveCD fails to start X session on QEMU · Issue #354 · ghostbsd/issues")
  * [Monty's “rescue” drive NixOS config](https://github.com/pmontgo33/nix-config "Monty's “rescue” drive NixOS config")
  * [Magnolia Mayhem's BSD Challenge Report](https://www.ministryofmayhem.space/posts/bsdptdeux/ "Magnolia Mayhem's BSD Challenge Report")
  * [Pick: NASty](https://github.com/nasty-project/nasty "Pick: NASty") — NASty is a NAS operating system built on NixOS and bcachefs. It turns commodity hardware into a storage appliance serving NFS, SMB, iSCSI, and NVMe-oF — managed from a single web UI, updated atomically, and rolled back when things go sideways.
  * [Pick: Defuse](https://github.com/shonebinu/Defuse "Pick: Defuse") — Defuse is a GTK4 application for removing image backgrounds locally.
  * [Defuse on Flathub](https://flathub.org/en/apps/io.github.shonebinu.Defuse "Defuse on Flathub")



## Tags

[ai developer](https://linuxunplugged.com/tags/ai%20developer), [ai in ubuntu](https://linuxunplugged.com/tags/ai%20in%20ubuntu), [amd rocm](https://linuxunplugged.com/tags/amd%20rocm), [background removal](https://linuxunplugged.com/tags/background%20removal), [backup system](https://linuxunplugged.com/tags/backup%20system), [bcachefs](https://linuxunplugged.com/tags/bcachefs), [bcachefs nas](https://linuxunplugged.com/tags/bcachefs%20nas), [bsd challenge](https://linuxunplugged.com/tags/bsd%20challenge), [bsd jails](https://linuxunplugged.com/tags/bsd%20jails), [canonical](https://linuxunplugged.com/tags/canonical), [canonical vp engineering](https://linuxunplugged.com/tags/canonical%20vp%20engineering), [container escape](https://linuxunplugged.com/tags/container%20escape), [copy fail](https://linuxunplugged.com/tags/copy%20fail), [cuda](https://linuxunplugged.com/tags/cuda), [cve-2026-31431](https://linuxunplugged.com/tags/cve-2026-31431), [declarative configuration](https://linuxunplugged.com/tags/declarative%20configuration), [defuse](https://linuxunplugged.com/tags/defuse), [freebsd](https://linuxunplugged.com/tags/freebsd), [freebsd setup](https://linuxunplugged.com/tags/freebsd%20setup), [frontier ai for ubuntu](https://linuxunplugged.com/tags/frontier%20ai%20for%20ubuntu), [ghostbsd](https://linuxunplugged.com/tags/ghostbsd), [gnu coreutils](https://linuxunplugged.com/tags/gnu%20coreutils), [jon seager](https://linuxunplugged.com/tags/jon%20seager), [jupiter broadcasting](https://linuxunplugged.com/tags/jupiter%20broadcasting), [kernel security](https://linuxunplugged.com/tags/kernel%20security), [linux exploit](https://linuxunplugged.com/tags/linux%20exploit), [linux kernel vulnerability](https://linuxunplugged.com/tags/linux%20kernel%20vulnerability), [linux podcast](https://linuxunplugged.com/tags/linux%20podcast), [linux unplugged](https://linuxunplugged.com/tags/linux%20unplugged), [local llm](https://linuxunplugged.com/tags/local%20llm), [nas os](https://linuxunplugged.com/tags/nas%20os), [nasty](https://linuxunplugged.com/tags/nasty), [nixos](https://linuxunplugged.com/tags/nixos), [nixos nas](https://linuxunplugged.com/tags/nixos%20nas), [odroid](https://linuxunplugged.com/tags/odroid), [open source](https://linuxunplugged.com/tags/open%20source), [page cache attack](https://linuxunplugged.com/tags/page%20cache%20attack), [patch sunday](https://linuxunplugged.com/tags/patch%20sunday), [python](https://linuxunplugged.com/tags/python), [rescue nix config](https://linuxunplugged.com/tags/rescue%20nix%20config), [resolute raccoon](https://linuxunplugged.com/tags/resolute%20raccoon), [rust](https://linuxunplugged.com/tags/rust), [rust coreutils](https://linuxunplugged.com/tags/rust%20coreutils), [security](https://linuxunplugged.com/tags/security), [snaps](https://linuxunplugged.com/tags/snaps), [tpm-backed full disk encryption](https://linuxunplugged.com/tags/tpm-backed%20full%20disk%20encryption), [ubuntu](https://linuxunplugged.com/tags/ubuntu), [ubuntu 26.04 lts](https://linuxunplugged.com/tags/ubuntu%2026.04%20lts), [ubuntu engineering](https://linuxunplugged.com/tags/ubuntu%20engineering), [ubuntu lts](https://linuxunplugged.com/tags/ubuntu%20lts), [uutils coreutils](https://linuxunplugged.com/tags/uutils%20coreutils), [ventoy](https://linuxunplugged.com/tags/ventoy), [wayland](https://linuxunplugged.com/tags/wayland), [zfs](https://linuxunplugged.com/tags/zfs), [🦝](https://linuxunplugged.com/tags/%F0%9F%A6%9D)