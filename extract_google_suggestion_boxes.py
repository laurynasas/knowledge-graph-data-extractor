import urllib
from bs4 import BeautifulSoup

from selenium import webdriver
from xvfbwrapper import Xvfb

query = "metallica similar artists"
service_url = 'https://www.google.co.uk/search'
params = {
    'query':query
}
url = service_url + "?" + urllib.urlencode(params)

display = Xvfb()
display.start()
driver = webdriver.Chrome('/home/laurynas/workspace/knowledge-graph-data-extractor/chromedriver')

driver.get(url)
content = driver.page_source

driver.quit()
display.stop()

soup = BeautifulSoup(content)


all_bands = soup.find_all("div", attrs={"class":"kltat"})

for band in all_bands:
    print band.text