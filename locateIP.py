import requests, bs4, json, urllib, webbrowser
r = requests.get('http://httpbin.org/ip')
if r.status_code != 200:
   quit()
sp = bs4.BeautifulSoup(r.text, 'html.parser')
newDictionary = json.loads(str(sp))
data = urllib.urlencode({'q': newDictionary['origin']})
url = 'http://google.com/'
full_url = url + '?' + data 
webbrowser.open(full_url)

