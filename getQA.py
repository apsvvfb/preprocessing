from bs4 import BeautifulSoup
import sys
#out=sys.argv[1]
soup=BeautifulSoup(open('index.html'),"lxml")
for link in soup.find_all('tr'):
    tds=link.find_all('td')
    td=tds[1]
    for p in td.find_all('p'):
	print(p.string)



    sys.exit()


