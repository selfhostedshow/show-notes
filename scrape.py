import concurrent.futures
import os
import shutil

import requests
from bs4 import BeautifulSoup
from jinja2 import Template

BASE_URL = "https://selfhosted.show"
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


def create_episode(api_episode):
    # RANT: What kind of API doesn't give the episode number?!
    episode_number = int(api_episode["url"].split("/")[-1])

    api_soup = BeautifulSoup(api_episode["content_html"], "html.parser")

    blurb = api_episode["summary"]

    sponsors = get_list(api_soup, "Sponsored By:")
    links = get_list(api_soup, "Links:") or get_list(api_soup, "Episode Links:")

    page_soup = BeautifulSoup(requests.get(api_episode["url"]).content, "html.parser")

    tags = []
    for link in page_soup.find_all("a", class_="tag"):
        tags.append(
            {"link": BASE_URL + link.get("href"), "text": link.get_text().strip()}
        )

    hosts = []
    for host in page_soup.find_all("ul", class_="episode-hosts"):
        for link in host.find_all("a"):
            hosts.append(
                {"name": link.get("title"), "link": BASE_URL + link.get("href")}
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
            "episode_number_padded": f"{episode_number:03}",
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

    with open(f"{OUTPUT_DIR}/episode-{episode_number}.md", "w") as f:
        f.write(output)


def main():
    api_data = requests.get(BASE_URL + "/json").json()

    try:
        os.mkdir(OUTPUT_DIR)
    except:
        pass

    # Run over multiple threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for api_episode in api_data["items"]:
            executor.submit(create_episode, api_episode)


if __name__ == "__main__":
    main()
