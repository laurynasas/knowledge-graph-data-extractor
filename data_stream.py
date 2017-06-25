import json
import urllib
import requests

api_key = open("api_key.txt").read()
query = "Radiohead similar artists"
service_url = 'https://www.google.co.uk/search'
params = {
    'query':query
}

url = service_url + "?" + urllib.urlencode(params)
print url

print requests.get(url).content

# print urllib.urlopen(url).read()
# response = json.loads(urllib.urlopen(url).read())
# print url
# print api_key
# print json.dumps(response, indent=4, sort_keys=True)


# for el in response['itemListElement']:
#     print el['result']['name'] + "("+ str(el['resultScore'])+ ")"


