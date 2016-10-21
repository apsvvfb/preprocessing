from bs4 import BeautifulSoup
import sys
out=sys.argv[1]
soup=BeautifulSoup(open('index.html'),"lxml")
for link in soup.find_all('tr'):
    imgId=link.p.string
    imgPath=link.a.get('href')
    with open(out,'a') as f:
	f.write(imgPath+"\n")
    #sys.exit()

