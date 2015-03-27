import sys
import os
import urllib as web
#comment ur function here
def get_name(url):
  #'html' in url and 
  name='index.html'
  print url[-5:]
  if url[-5:] == '.html':
    print "here"
    url=list(url)[::-1]
    name=url[:list.index(url,'/')][::-1] 
    name=''.join(name)
  return name

def wget(url):
  urlhand=web.urlopen(url)
  the_file=get_name(url)
  print the_file,' is the name chosen!'
  web.urlretrieve(url,the_file)
  return the_file

#This is the main function

def main():
  if len(sys.argv) ==2:
    url=sys.argv[1] #command line arguments as list of strings
  else:
    print "usage: python ex05wget.py url "
    sys.exit(1)  
  print "Downloading --------------", 
  #print "Downloading Completed!", 
  os.system('xdg-open '+wget(url))
  
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
