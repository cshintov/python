import sys

#the key function for sort method which returns the 'ext' element of the innerlist
def key_ext(inlist):
  return inlist[1]

#splits extension, retuns a [[name,ext],...] list
def split_ext(lst):
  result=[]
  for string in lst:
    result.append(string.split('.'))
  return result

#joins each inner list and returns the ["name.ext",...] list
def list_join(lst):
  result=[]
  for inner_list in lst:
    result.append('.'.join(inner_list))
  return result

#sorts incoming list of strings based on the extension in the strings
def ext_sort(lst):
  split_list=split_ext(lst) #splits the strings into [name,ext]
  split_list.sort(key=key_ext) #sorts the resulting list by the ext element 
  result=list_join(split_list) #joins the [name,ext] to "name.ext"
  return result

#This is the main function

def main():
  print "**************************\n"
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python ex16extsort.py [numlist] "
    sys.exit(1)  
  result=ext_sort(args)
  print "The ext sorted list : ", result 
  print "\n**************************"  
if __name__=="__main__":
  main()

