import sys
#Returns the sum of the integers as strings in the list numlist
def addnums(numlist):
  '''
  for i in range(len(numlist)):
    numlist[i]=int(numlist[i])
  for num in numlist:
    sumnum+=num
  Equivalent to the sum function below  
  '''
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
