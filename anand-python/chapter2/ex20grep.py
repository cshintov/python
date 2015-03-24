import sys

#comment ur function here
def grep(string,_file):
  lines=open(_file,'rU').readlines() #File as list of lines
  result=[]
  for line in lines:
    if string in line:
      result.append(line)
  for line in result: 
    print line,
  return 

#This is the main function

def main():
  if len(sys.argv) >=3:
    args=sys.argv[1:] 
    string=args[0]
    _file=args[1]
  else:
    print "usage: python ex20grep.py [string] [file] "
    sys.exit(1)  
  grep(string,_file)
  #result=grep(string,_file)
  #print "The result : ", result 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
