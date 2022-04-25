#! python3
# lucky.byMe.py - Opens the first 10 google search result links

import bs4, sys, requests, webbrowser

# Get web page 
print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve web contents
linkElems = bs4.BeautifulSoup(res.text)

# todo: Open the first 10 google search result
links = linkElems.select('a')
numberOpen = min(10,len(links))
for i in range(numberOpen):
    webbrowser.open('http://google.com' + links[i].get('href'))