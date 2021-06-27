import requests
from bs4 import BeautifulSoup

episode_numbers = list(range(0, 1))
hosts = {"Title":[],"Link":[]}
tags = []

for episode in episode_numbers:
    # read in show notes for each episode
    page = requests.get('https://selfhosted.show/' + format(episode+1))
    soup = BeautifulSoup(page.content, 'html.parser')

    # scrape episode tags
    for link in soup.find_all("a", class_="tag"):
        #print(link.get('href'))
        tags.append(link.get('href'))
        

    # scrape hosts
    for host in soup.find_all("ul", class_="episode-hosts"):
        for link in host.find_all("a"):
            hosts["Title"].append(link.get('title'))
            hosts["Link"].append(link.get('href'))
            #hosts.append(link.get('href'), link.get('title'))

    # scrape about this episode
    print(soup.p)

    # scrape episode metadata (air date, runtime, etc)

#print(tags)
#print(hosts)