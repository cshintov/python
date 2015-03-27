#https://docs.python.org/2/library/types.html

import sys
import re
from ex05wget import wget
#comment ur function here
def antihtml(url):
  html_file=wget(url)
  fh=open(html_file,'rU')
  cont_string=fh.read()
  new_cont=re.sub(r'<.*?>','',cont_string,flags=re.DOTALL)
  new_cont=re.sub(r'\n +',r'\n',new_cont)  
  new_cont=re.sub(r'\n+',r'\n',new_cont)
  fh.close()
  #print list(new_cont)
  return new_cont

#This is the main function

def main():
  if len(sys.argv) ==2:
    url=sys.argv[1] #command line argument giving the url 
  else:
    print "usage: python ex06antihtml.py url "
    sys.exit(1)  
  stripped=antihtml(url)
  print "The result : \n", stripped
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
