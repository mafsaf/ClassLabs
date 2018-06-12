import requests, bs4, sys
r = requests.get('http://example.com')
if r.status_code != 200:
   quit()
sp = bs4.BeautifulSoup(r.text, 'html.parser')
pelement = sp.select('p')
sys.stdout=open('example.txt', 'w')
print(pelement[0].get_text())
sys.stdout.close()

