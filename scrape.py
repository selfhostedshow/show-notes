import concurrent.futures
import os
import html2text
import operator

import requests
from bs4 import BeautifulSoup
from jinja2 import Template
import yaml
from dateutil.parser import parse as date_parse


with open("templates/episode.md.j2") as f:
    TEMPLATE = Template(f.read())


def mkdir_safe(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass


def get_list(soup, pre_title):
    """
    Blocks of links are preceded by a `p` saying what it is.
    """
    pre_element = soup.find("p", string=pre_title)
    if pre_element is None:
        return None
    return pre_element.find_next_sibling("ul")


def get_duration(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes} mins {seconds} secs"


def get_plain_title(title: str):
    """
    Get just the show title, without any numbering etc
    """
    # Remove number before colon
    title = title.split(":", 1)[-1]

    # Remove data after the pipe
    title = title.rsplit("|", 1)[0]

    # Strip any stray spaces
    return title.strip()


def create_episode(api_episode, show_config, output_dir):
    try:
        base_url = show_config['fireside_url']

        # RANT: What kind of API doesn't give the episode number?!
        episode_number = int(api_episode["url"].split("/")[-1])
        episode_number_padded = f"{episode_number:03}"
        publish_date = date_parse(api_episode['date_published'])
        output_file = f"{output_dir}/{publish_date.year}/episode-{episode_number_padded}.md"

        mkdir_safe(f"{output_dir}/{publish_date.year}")

        if os.path.isfile(output_file):
            print("Skipping", api_episode['url'], "as it already exists")
            return

        api_soup = BeautifulSoup(api_episode["content_html"], "html.parser")

        blurb = api_episode["summary"]

        sponsors = html2text.html2text(str(get_list(api_soup, "Sponsored By:")))

        links = html2text.html2text(str(get_list(api_soup, "Links:") or get_list(api_soup, "Episode Links:")))

        page_soup = BeautifulSoup(requests.get(api_episode["url"]).content, "html.parser")

        tags = []
        for link in page_soup.find_all("a", class_="tag"):
            tags.append(
                {"link": base_url + link.get("href"), "text": link.get_text().strip()}
            )

        # Sort tags by text
        tags = sorted(tags, key=operator.itemgetter("text"))

        hosts = []
        for host in page_soup.find_all("ul", class_="episode-hosts"):
            for link in host.find_all("a"):
                hosts.append(
                    {"name": link.get("title"), "link": base_url + link.get("href")}
                )

        player_embed = page_soup.find("input", class_="copy-share-embed").get("value")

        show_attachment = api_episode["attachments"][0]

        output = TEMPLATE.render(
            {
                "title": api_episode["title"],
                "title_plain": get_plain_title(api_episode["title"]),
                "episode_number": episode_number,
                "episode_number_padded": episode_number_padded,
                "url": api_episode["url"],
                "audio": show_attachment["url"],
                "duration": get_duration(int(show_attachment['duration_in_seconds'])),
                "blurb": blurb,
                "sponsors": sponsors,
                "links": links,
                "hosts": hosts,
                "tags": tags,
                "player_embed": player_embed,
                "date_published": publish_date.date().isoformat(),
                "show_config": show_config
            }
        )

        with open(output_file, "w") as f:
            print("Saving", api_episode["url"])
            f.write(output)
    except Exception as e:
        print(f"Skipping {api_episode['url']} because of error: {e}")


def main():
    # Grab the config embedded in the mkdocs config
    with open("mkdocs.yml") as f:
        shows = yaml.load(f, Loader=yaml.SafeLoader)['extra']['shows']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for show_slug, show_config in shows.items():
            output_dir = f"docs/{show_slug}"

            mkdir_safe(output_dir)

            api_data = requests.get(show_config['fireside_url'] + "/json").json()
            for api_episode in api_data["items"]:
                futures.append(executor.submit(create_episode, api_episode, show_config, output_dir))

        # Drain to get exceptions. Still have to mash CTRL-C, though.
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == "__main__":
    main()
