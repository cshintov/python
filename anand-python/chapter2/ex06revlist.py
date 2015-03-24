import sys
def reverse(lis):
  for i in range(len(lis)/2):
    lis[i],lis[len(lis)-(i+1)]=lis[len(lis)-(i+1)],lis[i]
  return lis
#This is the main function
def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:]
  else:
    print "usage: python exn.py [numlist] "
    sys.exit(1)  
  
  revlist=reverse(args)
  print "reverse(the list) : ",revlist
  revlist=reverse(revlist)
  print "reverse(reverse(the list)) : ",revlist
if __name__=="__main__":
  main()
