import sys

#comment ur function here
def reverse(arg_file):
  fh=open(arg_file,'rU')
  result_lines=fh.readlines()#file as a list of linestrings
  for line in result_lines:
    new_lines=result_lines[::-1]
  for line in new_lines:
    print line,
  fh.close()
  return result_lines

#This is the main function

def main():

  if len(sys.argv) >=2:
    args=sys.argv[1] 
  else:
    print "usage: python ex17reverse.py file "
    sys.exit(1)  
  result=reverse(args)
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"

