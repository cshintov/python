import sys
def prod(numlist):
  product=1
  for num in numlist:
    product*=int(num)
  return product
def fact(num):
  numb=int(num[0])
  return prod(range(1,numb+1))
#This is the main function
def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:]
  else:
    print "usage: python exn.py num "
    sys.exit(1)  
  result=fact(args)
  print "factorial = ",result
if __name__=="__main__":
  main()
