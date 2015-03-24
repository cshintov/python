import sys

#Returns a split of the list based on size
def split(lst,size):
  result=[]
  #i in (size,2size,3size...,len(lst)) if len(lst)%size==0 else i in (size,2size,...,len(lst)-(len(lst)%size))
  for i in range(size,len(lst)+1,size): 
    tmp=[]                              
    # j1 in (0,1,..,size),j2 (size,size+1,..2size)... 
    for j in range(i-size,i):
      tmp.append(lst[j])                
    
    result.append(tmp)
  if len(lst) % size != 0:
    result.append(lst[i:])
  return result

#This is the main function

def main():
  if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
    lst=args[:-1]
    size=args[-1]
  else:
    print "usage: python module.py [numlist] [size]"
    sys.exit(1)  
  result=split(lst,int(size))
  print "The split list is : ", result 
  
if __name__=="__main__":
  main()
