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
f_songs = open("songs_already_visited.txt","w")
content = f_rv.readlines()
for line in content:
    visited.append(line.replace("\n","").decode('utf-8'))




counter = 0
stuck = 0
display = Xvfb()
display.start()
driver = webdriver.Chrome('/home/laurynas/workspace/knowledge-graph-data-extractor/chromedriver')
visited_size = len(visited)
while visited:
    time.sleep(1)

    seed_band = visited.pop(0)
    counter +=1

    print "band # "+str(counter)+"/"+str(visited_size)+"|"+str(seed_band.encode("utf8"))+"|"+" | with # of songs: "


    query = seed_band + u" songs"
    service_url = u'https://www.google.co.uk/search'
    params = {
        'query': query.encode("utf8")
    }
    url = service_url + u"?" + urllib.urlencode(params)



    driver.get(url)
    content = driver.page_source



    soup = BeautifulSoup(content)
    all_songs = soup.find_all("div", attrs={"class": "title"})
    # print content

    if not all_songs:
        print "Cannot reach Google will skip"
        continue
    else:

        print len(all_songs)
        f_songs.write((u"++"+seed_band + u"\n").encode("utf8"))

        for song in all_songs:
            f_songs.write((song.text + u"\n").encode('utf-8'))


driver.quit()
display.stop()
visited_f.close()
f.close()
