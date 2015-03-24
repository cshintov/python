import sys
import mylib
#returns the size of the largest line
def larg_line(list_of_lines):
  lengths=[]
  for line in list_of_lines:
    lengths.append(len(line))
  width=max(lengths)
  return width

def align(_file):
  op_file=open(_file,'r')
  list_of_lines=op_file.readlines()
  width=larg_line(list_of_lines) #gets the size of the largest line
  result=[]
  for line in list_of_lines:
    result.append(mylib.center(line,width)) #line is a string+\n
  print "Here is the center aligned file:\n\n"
  mylib.print_list(result)
  op_file.close()
  return result

#This is the main function

def main():
  if len(sys.argv) ==2:
    _file=sys.argv[1] #command line arguments as list of strings
  else:
    print "usage: python ex23center.py [file] "
    sys.exit(1)  
  result=align(_file)
  #print "The result : ", result 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
