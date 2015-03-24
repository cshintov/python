import sys
import mylib

def wrap(_file,width):
  op_file=open(_file,'r')
  list_of_lines=op_file.readlines()
  result=[]
  for line in list_of_lines:
    result.append(mylib.nice_split(line,width)) #line is a string+\n
  print "Here is the wrapped file:\n"
  mylib.print_list(result)
  op_file.close()
  return result


#This is the main wraption

def main():
  if len(sys.argv) >=3:
    args=sys.argv[1:] # line arguments as list of strings ; convert your ints 
    _file=args[0]
    width=int(args[1])
  else:
    print "usage: python ex22wrapmod.py [filename] [width to split] "
    sys.exit(1)  
  result=wrap(_file,width)
  #print "The result : \n", result 
  return
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
