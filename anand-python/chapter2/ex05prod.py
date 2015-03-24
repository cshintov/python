import sys
def prod(numlist):
  product=1
  for num in numlist:
    product*=int(num)
  return product
#This is the main function
def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:]
  else:
    print "usage: python ex04prod.py [numlist] "
    sys.exit(1)  
  result=prod(args)
  print "result = ",result
if __name__=="__main__":
  main()
