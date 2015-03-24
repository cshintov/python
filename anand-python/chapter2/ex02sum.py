import sys
#Returns the sum of the integers after converting the strings in the list numlist to integers 
def addnums(numlist):
  sumnum=sum(int(x) for x in numlist)
  return sumnum  
#This is the main function
def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:]  
  else:
    print "usage: python ex19add.py [numlist] "
    sys.exit(1)
  result=addnums(args)
  print "sum = ",result
if __name__=="__main__":
  main()
