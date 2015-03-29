'''Problem 14: Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.'''


import sys
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib as web
#downloads the url to temp.html returns the name test.html
def wget(url,tmp='temp.html'):
  urlhand=web.urlopen(url)
  web.urlretrieve(url,tmp)
  return tmp
#opens the downloaded file into doc as a string and bs takes the <a> tags with href
def links(url):
  doc=open(wget(url),'r')
  print "The links are : \n",
  for link in BeautifulSoup(doc, parseOnlyThese=SoupStrainer('a')):
    if link.has_key('href'):
      print link['href']

#This is the main function

def main():
  if len(sys.argv) ==2:
    html=sys.argv[1] #command line argument input giving url
    links(html)
  else:
    print "usage: python ex14beautifulsoup.py url "
    sys.exit(1)  

  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"

