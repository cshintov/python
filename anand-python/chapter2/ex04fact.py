import sys
def prod(numlist):
  product=1
  for num in numlist:
    product*=num
  return product
def fact(num):
    return prod(range(1,num+1))
#This is the main function
def main():
  if len(sys.argv) >=2:
    num=int(sys.argv[1])
  else:
    print "usage: python ex04fact.py num "
    sys.exit(1)  
  result=fact(num)
  print "factorial = ",result
if __name__=="__main__":
  main()
