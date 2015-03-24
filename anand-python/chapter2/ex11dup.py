import sys

#Returns the list of repeating elements 
def dup(arg):
  uniq=[]
  dupl=[]  
  for num in arg:
    if num not in uniq:  #creates a list consisting only of unique elements
      uniq.append(num)
    else:
      if num not in dupl: #creates a list consisting only of duplicate elements
        dupl.append(num)
  return dupl,uniq

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex11dup.py [numlist] "
    sys.exit(1)  
  result=dup(args)
  print "The duplicate element list is : ", result[0]
  print "The duplicate element list is : ", result[1]   
if __name__=="__main__":
  main()
