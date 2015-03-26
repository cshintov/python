import sys

#Returns the key,value tuple list sorted based on the key
def v(_dict):
  key_val=_dict.items()
  key_val.sort(key=key_fn)
  sort_val=[]
  for tup in key_val:
    sort_val.append(tup[1])
  print sort_val
  return key_val
#Interchanges each of the (key, value) pair
def invertdict(_dict):
  new_dict={}
  for key, val in _dict.items():
    new_dict[val]=key
  print new_dict
  return new_dict



#This is the main function

def main():
  invertdict({'x': 1, 'y': 2, 'z': 3})
  '''
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python module.py [numlist] "
    sys.exit(1)  
  result=function(args)
  print "The result : \n", result '''
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
