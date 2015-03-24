import sys

#Accepts a list of numbers and returns the cumulative product list
def cprod(lst):
  result=[]
  prod=1
  for e in lst:
    prod*=int(e)
    result.append(prod)
  return result

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex08cumlprod.py [numlist] "
    sys.exit(1)  
  result=cprod(args)
  print "The result : ", result 
  
if __name__=="__main__":
  main()
