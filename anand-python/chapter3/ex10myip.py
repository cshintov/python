#http://httpbin.org/get is the url input
#It has 'origin': ip address as one of its key:value
import sys
import json
import urllib as web
#returns the ip address of the system
def myip(url):
  response=web.urlopen(url) #response=the response from the url 
  result=json.load(response)['origin']# jason.loads() encodes the  response to json object
  return result

#This is the main function

def main():
  if len(sys.argv) ==2:
    url=sys.argv[1] #command line arguments as list of strings
  else:
    print "usage: python ex10myip.py [numlist] "
    sys.exit(1)  
  my_ip=myip(url)
  print "My Ip address : ", my_ip 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
