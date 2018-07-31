import requests
import json
import urllib2
github_url = r'http://bing-blink.azurewebsites.net/api/blink/summary?count=5&cutoff=5&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCoffee'
data = json.dumps({'Url':'https://en.wikipedia.org/wiki/Coffee'})
r = requests.post(github_url, data)

response = urllib2.urlopen(github_url)
#html = json.loads(response.read())
t=r.json
print t['Status']
print response.read()
print r.json
print r.data

