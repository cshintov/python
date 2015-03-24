import sys
def leng(string):
  return len(string)
#returns the sorted list based on the length of the elements 
def lensort(arg):
  #arg.sort(key=lambda x: len(x))
  arg.sort(key=leng)
  return arg

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex13lensort.py [numlist] "
    sys.exit(1)  
  result=lensort(args)
  print "The sorted list based on length of list elements :\n", result 
  
if __name__=="__main__":
  main()
