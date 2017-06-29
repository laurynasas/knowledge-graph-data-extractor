import urllib
from bs4 import BeautifulSoup

from selenium import webdriver
from xvfbwrapper import Xvfb
import time
seed_band = u"Radiohead"

f = open('network_2.txt', 'w')
visited_f = open('already_visited_2.txt', 'w')

visited = []
frontier = []

f_rv = open("already_visited.txt", "r")
content = f_rv.readlines()
for line in content:
    visited.append(line.replace("\n","").decode('utf-8'))



f_r = open("network.txt", "r")
content = f_r.readlines()
first_time = True

for line in content:
    line = line.replace("++","")
    line = line.replace("\n", "").decode('utf-8')
    if line not in visited:
        frontier.append(line)



counter = 0
frontier_c = len(frontier)
stuck = 0
display = Xvfb()
display.start()
driver = webdriver.Chrome('/home/laurynas/workspace/knowledge-graph-data-extractor/chromedriver')
while frontier:
    time.sleep(1)

    seed_band = frontier.pop(0)
    frontier_c-=1
    counter +=1

    print "band # "+str(counter)+" | frontier size: "+str(frontier_c), seed_band


    query = seed_band + u" similar artists"
    service_url = u'https://www.google.co.uk/search'
    params = {
        'query': query.encode("utf8")
    }
    url = service_url + u"?" + urllib.urlencode(params)



    driver.get(url)
    content = driver.page_source



    soup = BeautifulSoup(content)
    all_bands = soup.find_all("div", attrs={"class": "kltat"})

    if not all_bands:
        print "Cannot reach Google will skip"
        continue
    else:

        visited.append(seed_band)
        visited_f.write((seed_band + u"\n").encode("utf8"))
        band_name = u"++" + seed_band + u"\n"
        f.write(band_name.encode("utf8"))

        for band in all_bands:
            f.write((band.text + u"\n").encode('utf-8'))
            if band.text not in visited and band.text not in frontier:
                frontier.append(band.text)
                frontier_c+=1

driver.quit()
display.stop()
visited_f.close()
f.close()
