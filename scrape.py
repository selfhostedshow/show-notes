import concurrent.futures
import os
import shutil

import requests
from bs4 import BeautifulSoup
from jinja2 import Template
from ruamel.yaml import YAML

OUTPUT_DIR = "output"


with open("templates/episode.md.j2") as f:
    TEMPLATE = Template(f.read())


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


def create_episode(api_episode, base_url, output_dir):
    # RANT: What kind of API doesn't give the episode number?!
    episode_number = int(api_episode["url"].split("/")[-1])
    episode_number_padded = f"{episode_number:03}"
    output_file = f"{output_dir}/episode-{episode_number_padded}.md"

    if os.path.isfile(output_file):
        print(f"Skipping {api_episode['url']}", end="\n")
        return

    api_soup = BeautifulSoup(api_episode["content_html"], "html.parser")

    blurb = api_episode["summary"]

    sponsors = get_list(api_soup, "Sponsored By:")
    links = get_list(api_soup, "Links:") or get_list(api_soup, "Episode Links:")

    page_soup = BeautifulSoup(requests.get(api_episode["url"]).content, "html.parser")

    tags = []
    for link in page_soup.find_all("a", class_="tag"):
        tags.append(
            {"link": base_url + link.get("href"), "text": link.get_text().strip()}
        )

    hosts = []
    for host in page_soup.find_all("ul", class_="episode-hosts"):
        for link in host.find_all("a"):
            hosts.append(
                {"name": link.get("title"), "link": base_url + link.get("href")}
            )

    try:
        player_embed = page_soup.find("input", class_="copy-share-embed").get("value")
    except:
        player_embed = None

    show_attachment = api_episode["attachments"][0]

    output = TEMPLATE.render(
        {
            "title": api_episode["title"],
            "title_plain": api_episode["title"].split(":", 1)[-1].strip(),
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
            "date_published": api_episode["date_published"].split("T", 1)[0],  # Date parsing? What's that?
        }
    )

    with open(output_file, "w") as f:
        f.write(output)


def main():
    with open("shows.yml") as f:
        shows = YAML().load(f)

    try:
        os.mkdir(OUTPUT_DIR)
    except:
        pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for show in shows:
            output_dir = f"{OUTPUT_DIR}/{show['show_name']}"

            try:
                os.mkdir(output_dir)
            except FileNotFoundError:
                pass

            docs_dir = f"shows/{show['show_name']}"
            mkdocs_config = f"shows/{show['show_name']}.yml"
            docs_output_dir = output_dir + "/docs"

            try:
                os.mkdir(docs_output_dir)
            except FileNotFoundError:
                pass

            api_data = requests.get(show['fireside_url'] + "/json").json()
            for api_episode in api_data["items"]:
                executor.submit(create_episode, api_episode, show['fireside_url'], docs_output_dir)

            try:
                os.remove(output_dir + "/mkdocs.yml")
            except FileNotFoundError:
                pass
            shutil.copy2(mkdocs_config, output_dir + "/mkdocs.yml")


if __name__ == "__main__":
    main()
