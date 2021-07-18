import requests
from bs4 import BeautifulSoup
from jinja2 import Template
import shutil
import os

episode_numbers = list(range(0, 1))
hosts = []
tags = []
desc_links = []

BASE_URL = "https://selfhosted.show"

api_data = requests.get(BASE_URL + "/json").json()

for episode in api_data['items']:
    episode_number = api_data['']

for episode in episode_numbers:
    realepnumber = episode+1

    # read in show notes for each episode
    page = requests.get(f"{BASE_URL}/{realepnumber}")
    soup = BeautifulSoup(page.content, 'html.parser')

    # scrape episode tags
    for link in soup.find_all("a", class_="tag"):
        tags.append({
            "link": BASE_URL + link.get('href'),
            "text": link.get_text().strip()
        })
        

    # scrape hosts
    for host in soup.find_all("ul", class_="episode-hosts"):
        for link in host.find_all("a"):
            hosts.append({
                "title": link.get('title'),
                "link": BASE_URL + link.get('href')
            })

    # scrape about this episode description
    for item in soup.find_all("div", class_="split-primary prose"):
        # grab episode description blurb
        for p in item.p:
            #print(p)
            description = p
        # grab episode links
        for linkblock in item.find_all("ul"):
            for link in item.find_all("li"):
                desc_links.append(link)

    # grab episode stats
    #for stat in soup.find_all("div", class_="column"):
        #print(stat.p)

    # scrape episode metadata (air date, runtime, etc)


    template = Template(open('templates/episode.md.j2').read())
    output = template.render({"desc_links": desc_links, "tags": tags, "hosts": hosts})

    # Remove any outputs from a previous run
    try:
        shutil.rmtree("output")
        os.mkdir("output")
    except:
        pass

    with open('output/episode%s.md' % realepnumber, 'w') as f:
        f.write(output)

#print(tags)
#print(hosts)
#print(description)
#print(desc_links)

