import sys

# 
def uniqlst(lst):
  result=[]
  for num in lst:
    if num not in result:
      result.append(num)
  return result

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex10uniq.py [numlist] "
    sys.exit(1)  
  result=uniqlst(args)
  print "The unique list : ", result 
  
if __name__=="__main__":
  main()
