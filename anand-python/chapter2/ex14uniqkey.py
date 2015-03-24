import sys
#returns the first elements of the string
def first(string):
  return string[0]
#returns the last elements of the string
def last(string):
  return string[-1]
#returns the length of the string
def length(string):
  return len(string)
def same(string):
  return string.lower()
# Returns the key function based on the command line option
def which(key):
 
  if key=="first":
    return first
  if key=="last":
    return last
  if key=="length":
    return length
  if key=="same":
    return same
  else:
    return str #default key

#Returns the unique list based on the key function 
def uniqlst(lst,key):
  result=[lst[0]]
  for elmnt in lst[1:]:
    present=False
    for elt in result:
      if key(elmnt) == key(elt): 
        present=True      # key(elmnt) Already present in the result!" 
        break 
    if not present:
      result.append(elmnt)
  return result

#This is the main function

def main():
  
  if len(sys.argv) >=3:
    key="" #default key
    args=sys.argv[1:] #command line argument list of input list
    option=sys.argv[1]
    if option[:2] == "--":
      key=option[2:] # option discarding '--'
      if key in ['first','last','length','same']:
        print key
        args=sys.argv[2:] # Since everything is good the input list is set from the next element onwards
      else:
        key="" #first element starts with -- but is not an option but the first element of the input
  elif len(sys.argv)==2:
    print "The unique list : ",list(sys.argv[1])
    sys.exit(0)
  else:
    print "usage: python ex14uniqkey.py [--first/last/length/same] [numlist] "
    sys.exit(1)  
  
  result=uniqlst(args,which(key))
  print "The unique list : ", result 
  
if __name__=="__main__":
  main()
