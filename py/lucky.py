#! python3 
# lucky.py - Opens Google search results.

import bs4, sys, webbrowser, requests

# Retrieve the Google search web page 
print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open several web tabs
# The original code is soup.select('.r a')
# The object with CSS element return 0 links
# We just open the first five links.
linkElems = soup.select('a')
numOpen = min(10,len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    # get() return link with previous part of google
    webbrowser.open('http://google.com' + linkElems[i].get('href'))