#https://docs.python.org/2/library/types.html
#<a indepth="true" class="reference internal" href="getting-started.html">1. Getting Started</a>
#file:///home/cshintov/Anand-python/anand-python/chapter3/test.html
#file:///home/cshintov/Anand-python/anand-python/chapter3/types.html
import sys
import re
import urllib as web

def wget(url,tmp='temp.html'):
  urlhand=web.urlopen(url)
  web.urlretrieve(url,tmp)
  return tmp

def get_links(cont_string):
  _links=re.findall(r'href="(.*?)"',cont_string,flags=re.DOTALL)   #get all href links
  cont_string=' '.join(_links)
  cont_string=re.sub(r'.*[.]css? ','',cont_string,flags=re.DOTALL) #remove css links
  cont_string=re.sub(r'.*[.]xml? ','',cont_string,flags=re.DOTALL) #remove xml links
  #cont_string=re.sub(r' ',r'\n',cont_string,flags=re.DOTALL)       #replace a space with newline
  _links=cont_string.split()
  return _links


#comment ur function here
def links(url):
  html_file=wget(url)
  fh=open(html_file,'rU')
  cont_string=fh.read()
  _links=get_links(cont_string)
  #_links=re.findall(r'[\w/.]+html',cont_string,flags=re.DOTALL)
  fh.close()
  return _links

#This is the main function

def main():
  if len(sys.argv) ==2:
    url=sys.argv[1] #command line argument giving the url 
  else:
    print "usage: python ex08links.py url "
    sys.exit(1)  
  _links=links(url)
  print "The links in this page :"
  #print _links
  for link in _links:
    print link    
  return
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
