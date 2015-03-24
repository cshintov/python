import sys
#both the functions works fine with both integers and strings
# < and > operators works fine with both integers and strings
# only thing is  A is less than a

def mymin(lst):
  mn=lst[0]
  for e in lst:
    if e < mn: 
      mn = e
  return mn

def mymax(lst):
  mx=lst[0]
  for e in lst:
    if e > mx: 
      mx = e

  return mx

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #list of inputs as strings
  else:
    print "usage: python ex07minmax.py [numlist] "
    sys.exit(1)  
  result=mymin(args)
  print "minimum of the given list : ",result
  result=mymax(args)
  print "maximum of the given list : ",result
  print "minimum of the integers 3,5,18,2,8 : ",mymin([3,5,18,2,8])
  print "maximum of the integers 3,5,18,2,8 : ",mymax([3,5,18,2,8])
if __name__=="__main__":
  main()
