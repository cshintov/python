import sys
import mylib as my
#comment ur function here
def parse_csv(_file,delim=','):
  fh=open(_file,'r')
  file_lines=fh.readlines()
  #new_string=my.strip(file_string,delim)
  list_pars=[]
  for line in file_lines:
    list_pars.append(line.strip().split(delim))
  fh.close()
  return list_pars

#This is the main function

def main():
  if len(sys.argv) ==2:
    args=sys.argv[1:] #command line arguments as list of strings
    _file=args[0]
  else:
    print "usage: python module.py [numlist] "
    sys.exit(1)  
  result=parse_csv(_file)
  print "The result : \n"
  #print result
  my.print_2d(result)
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
