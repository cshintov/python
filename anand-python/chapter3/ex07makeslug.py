import sys
import re
#returns the slug of the given name
def make_slug(name):
  print name
  name=re.sub(r'[-\W_]+','-',name) #replaces one or more '-' and special char combo with single -
  print name  
  name=name.strip('-') #strips the '-' at start and end of the name if exists
  return name

#This is the main function

def main():
  if len(sys.argv) >=2:
    name=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex07makeslug.py name"
    sys.exit(1)  
  name='-'.join(name) #joins the name list on '-'
  slug=make_slug(name) #make slug of the joined string
  print "The slug of the given Name : \n", slug
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
