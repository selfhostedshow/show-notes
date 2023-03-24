# SSH 093: The Podman Perspective

<iframe src="https://player.fireside.fm/v2/dUlrHQih+fp1aR6Lw?theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>

* Air Date: 2023-03-24
* Duration: 59 mins 22 secs

## About this episode

Alex goes all in on Rootless Podman, Chris is saving his Nextcloud install from disaster, and a special guest joins us.

## Your hosts
* [Alex Kretzschmar](https://selfhosted.show/hosts/alexktz)
* [Chris Fisher](https://selfhosted.show/hosts/chrislas)
* [Alex Ellis](https://selfhosted.show/guests/alexellis)

## Sponsored by

  * [Linode](https://linode.com/ssh): [Receive a $100 60-day credit towards your new account. ](https://linode.com/ssh) Promo Code: linode.com/ssh
  * [Tailscale](http://tailscale.com/selfhosted): [Tailscale is a Zero config VPN. It installs on any device in minutes, manages firewall rules for you, and works from anywhere. Get 20 devices for free for a personal account. ](http://tailscale.com/selfhosted)



## Episode links

  * [Secret Management with Ansible Vault and docker-compose - YouTube](https://www.youtube.com/watch?v=CUh8FDLbj8M "Secret Management with Ansible Vault and docker-compose - YouTube") — Secret management with docker-compose doesn't have to be an enigma. This video shows how I use Ansible and Ansible Vault in conjunction with docker-compose to keep my secrets safe and encrypted whilst still being able to push my repos to Github publicly.
  * [KTZ Systems](https://ktzsystems.com/ "KTZ Systems") — We specialize in professional cloud infrastructure management and business network services.
  * [Gitea 1.19.0 is released](https://blog.gitea.io/2023/03/gitea-1.19.0-is-released/ "Gitea 1.19.0 is released") — We are proud to present the release of Gitea version 1.19.0.
  * [Linode Green Light Beta Program ](https://www.linode.com/green-light/ "Linode Green Light Beta Program ") — Get early access and test new Linode products before they hit the market, provide valuable feedback to influence product direction, and become part of a community of developers helping us build the cloud that works for you.
  * [Docker is deleting Open Source organisations](https://blog.alexellis.io/docker-is-deleting-open-source-images/ "Docker is deleting Open Source organisations") — Yesterday, Docker sent an email to any Docker Hub user who had created an "organisation", telling them their account will be deleted including all images, if they do not upgrade to a paid team plan. The email contained a link to a tersely written PDF (since, silently edited) which was missing many important details which caused significant anxiety and additional work for open source maintainers.
  * [Alex Ellis' Web Site](https://www.alexellis.io/ "Alex Ellis' Web Site")
  * [Podman issue pulling from local registry](https://access.redhat.com/discussions/5946861 "Podman issue pulling from local registry")
  * [/etc/subuid and /etc/subgid configuration](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md#etcsubuid-and-etcsubgid-configuration "/etc/subuid and /etc/subgid configuration") — Rootless Podman requires the user running it to have a range of UIDs listed in the files /etc/subuid and /etc/subgid. 
  * [Using volumes with Podman](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md#using-volumes "Using volumes with Podman") — If your container runs with the root user, then root in the container is actually your user on the host. UID/GID 1 is the first UID/GID specified in your user's mapping in /etc/subuid and /etc/subgid, etc. If you mount a directory from the host into a container as a rootless user, and create a file in that directory as root in the container, you'll see it's actually owned by your user on the host.
  * [Hub 4 pioneers ethical AI integration for a more productive and collaborative future](https://nextcloud.com/blog/hub-4-pioneers-ethical-ai-integration-for-a-more-productive-and-collaborative-future/ "Hub 4 pioneers ethical AI integration for a more productive and collaborative future") — Today, we are excited to announce a major step forward with Hub 4 – the very first on-premises collaboration platform to integrate intelligent features across its applications.
  * [Remove not supported column comments for SQLite - Nextcloud](https://github.com/nextcloud/server/pull/36803 "Remove not supported column comments for SQLite - Nextcloud") — Some times column comments are used, e.g. to make clear an integer is used as a timestamp. For SQLite column comments are not supported and migration that use column comments will not work (see linked comment above for an example). Somehow it works when you have a clean install, then all migrations pass, but when executing single migrations they will fail.
  * [Updating to 3.2.0 fails on SQLite installations · Nextcloud](https://github.com/nextcloud/forms/issues/1549 "Updating to 3.2.0 fails on SQLite installations · Nextcloud")
  * [Command Line Shell For SQLite](https://sqlite.org/cli.html#recover "Command Line Shell For SQLite") — Like the ".dump" command, ".recover" attempts to convert the entire contents of a database file to text. 
  * [Converting Nextcloud database typw](https://docs.nextcloud.com/server/latest/admin_manual/configuration_database/db_conversion.html "Converting Nextcloud database typw") — You can convert a SQLite database to a better performing MySQL, MariaDB or PostgreSQL database with the Nextcloud command line tool. SQLite is good for testing and simple single-user Nextcloud servers, but it does not scale for multiple-user production servers.
  * [Belkin (Wemo) takes “big step back” from Matter](https://www.reddit.com/r/homeassistant/comments/11t1jsc/belkin_wemo_takes_big_step_back_from_matter/ "Belkin \(Wemo\) takes “big step back” from Matter") — Belkin says Wemo devices will support Matter once the company can "find a way to differentiate them,"
  * [Alby — Lightning for your Browser!](https://getalby.com/ "Alby — Lightning for your Browser!") — Alby brings Boosts to the web.
  * [Self-Hosted on the Podcastindex.org](https://podcastindex.org/podcast/830124 "Self-Hosted on the Podcastindex.org") — Send a Boost into the show via the web. First, top-up Alby, then head over to our entry on the Podcast Index.



## Tags

[alex ellis](https://selfhosted.show/tags/alex%20ellis), [alex youtube](https://selfhosted.show/tags/alex%20youtube), [docker-compose](https://selfhosted.show/tags/docker-compose), [gite](https://selfhosted.show/tags/gite), [gitea actions](https://selfhosted.show/tags/gitea%20actions), [green light beta program](https://selfhosted.show/tags/green%20light%20beta%20program), [jupiter broadcasting](https://selfhosted.show/tags/jupiter%20broadcasting), [nextcloud](https://selfhosted.show/tags/nextcloud), [podman](https://selfhosted.show/tags/podman), [rootless](https://selfhosted.show/tags/rootless), [secret management with ansible vault](https://selfhosted.show/tags/secret%20management%20with%20ansible%20vault), [self-hosting podcast](https://selfhosted.show/tags/self-hosting%20podcast), [sqlite](https://selfhosted.show/tags/sqlite)