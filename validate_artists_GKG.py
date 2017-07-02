import json
import urllib

api_key = open('api_key.txt').read()

f_rv = open("already_visited.txt", "r")
visited=[]
content = f_rv.readlines()
enter = False
for line in content:
    if 'Tulisa' in line:

        enter=True
    if enter:
        visited.append(line.replace("\n","").decode('utf-8'))


f_rv = open("related_words_2.txt", "w")
f = open("related_words.txt", "r")
related_words = []

content = f.readlines()
for line in content:
    related_words.append(line)

for query in visited:
    query =query.encode('utf8')
    print "----------- "+query+" -------------"
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    for element in response['itemListElement']:
        el = element['result'].get('description')
        if el and el.encode("utf8")+"\n" not in related_words:
            try:
                f_rv.write(el.encode("utf-8")+u"\n")
            except:
                print "failed to write", el
                continue

            related_words.append(el.encode("utf8")+"\n")