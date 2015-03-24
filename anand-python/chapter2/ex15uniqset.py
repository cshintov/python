import sys

#returns unique list using set
def uniq(arg):
  arg=set(arg)
  result=[]
  for i in arg:
    result.append(i)
  return result

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex15uniqset.py [numlist] "
    sys.exit(1)  
  result=uniq(args)
  print "The result : ", result 
  
if __name__=="__main__":
  main()
