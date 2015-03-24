import sys

#This prints the exact reverse of the line
def exact_rev(lines):
  new_lines=[]
  for line in lines:
    #line=line.split()
    line=line[::-1]         #reversing the entire line-string
    new_lines.append(line)
  for line in new_lines:
    print line,
  return
#This loop prints the words in the line in reverse 
def word_rev(lines):
  new_lines=[]
  for line in lines:
    line=line.split()
    line=line[::-1]         #Here 'list' of the component strings are reversed
    new_lines.append(line)
  for line in new_lines:
    for string in line:
      print string,
    print 
  return

#prints the lines in the file in reverse
def reverse(arg_file):
  fh=open(arg_file,'rU')
  lines=fh.readlines() #file as a list of linestrings
  #print lines
  fh.close()
  #This prints the exact reverse of the line
  print "Printing the reverse of the entire line-string"
  exact_rev(lines)
  print "\n*************************\n"
  #This prints the words in the line in reverse 
  print "Printing the reverse of the list of component strings of a line\n"
  word_rev(lines)
  return 

#This is the main function

def main():

  if len(sys.argv) >=2:
    args=sys.argv[1] 
  else:
    print "usage: python ex18linerev.py file "
    sys.exit(1)  
  reverse(args)
  #print "The result : \n", result 

if __name__=="__main__":
  print "**************************"
  main()
  print "\n\n**************************"
