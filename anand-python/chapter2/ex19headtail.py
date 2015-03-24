import sys

#comment ur function here
def head(_file,num=10):
  list_of_lines=open(_file,'rU').readlines()
  result=list_of_lines[:num] #This works even if the num is larger than the length of the list
  for string in result:
    print string,
  return

def tail(_file,num=10):
  list_of_lines=open(_file,'rU').readlines()
  result=list_of_lines[-num:] #This works even if the num is larger than the length of the list
  for string in result:
    print string,
  return

#This is the main function

def main():

  if len(sys.argv) >=4:
    _file=sys.argv[3] 
    option=sys.argv[1]
    num_lines=int(sys.argv[2])
  elif len(sys.argv)==3:
    if sys.argv[1] in ('--head','--tail'):
      _file=sys.argv[2] 
      option=sys.argv[1]
      num_lines=10
    else:
      print "Unknown Option: use --head or --tail "
      sys.exit(1)
  else:
    print "usage: python ex19headtail.py --[head/tail] [number of lines] [file] "
    sys.exit(1)  
  
  if option=='--head':
    print "First %d lines of the file %s" % (num_lines,_file) ,'\n'
    head(_file,num_lines)
  elif option=='--tail':
    print "Last %d lines of the file %s" % (num_lines,_file) ,'\n'
    tail(_file,num_lines)
  else:
    print "Unknown Option:",option
    sys.exit(1)
  
  return 

if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
