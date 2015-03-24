import sys
# returns a list of integers if the input is a list of integers as strings
# if the input is a list of strings as strings returns the list as it is
def isint(lst):
  for i in range(len(lst)):
    if lst[i].isdigit() :
      lst[i]=int(lst[i])
  return lst

def cumulative_sum(lst):
  csumlst,csum=[lst[0]],lst[0] #initializes csumlst=[first el of lst] and csum=first el of lst
  for e in lst[1:]:
    csum+=e
    csumlst.append(csum)
  return csumlst
#This is the main function
def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex08cumlsum.py [numlist] "
    sys.exit(1)  
  args=isint(args) # returns a list of integers if the input is a list of integers as strings
  result=cumulative_sum(args)
  print "The cumulative sum list : ", result 
if __name__=="__main__":
  main()
