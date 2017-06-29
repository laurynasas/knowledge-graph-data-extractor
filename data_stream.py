import urllib
from bs4 import BeautifulSoup
import requests

seed_band = u"Radiohead"

f = open('network_get.txt', 'w')
visited_f = open('already_visited_get.txt', 'w')

visited = []
frontier = [seed_band]

while frontier:
    seed_band = frontier.pop(0)
    print seed_band
    visited.append(seed_band)
    visited_f.write((seed_band + u"\n").encode("utf8"))

    band_name = u"++" + seed_band + u"\n"
    f.write(band_name.encode("utf8"))

    query = seed_band + u" similar artists"
    service_url = u'https://www.google.co.uk/search'
    params = {
        'query': query.encode("utf8")
    }
    url = service_url + u"?" + urllib.urlencode(params)


    content = requests.get(url).content

    # print content


    soup = BeautifulSoup(content)
    all_bands = soup.find(text="People also search for")
    if all_bands:
        all_bands= all_bands.parent.parent.find_all("div", attrs={"class": "_sce"})
    else:
        continue

    for band in all_bands:
        f.write((band['title'] + u"\n").encode('utf-8'))
        if band['title'] not in visited and band['title'] not in frontier:
            frontier.append(band['title'])

visited_f.close()
f.close()




# print url
#
# print requests.get(url).content

# print urllib.urlopen(url).read()
# response = json.loads(urllib.urlopen(url).read())
# print url
# print api_key
# print json.dumps(response, indent=4, sort_keys=True)


# for el in response['itemListElement']:
#     print el['result']['name'] + "("+ str(el['resultScore'])+ ")"


