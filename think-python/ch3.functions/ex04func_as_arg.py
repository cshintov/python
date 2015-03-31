#Passing a function object as argument
import sys

def print_string(string):
  print string

def do_twice(func,arg):
  func(arg)
  func(arg)
  
def do_four(func,arg):
  do_twice(func,arg)
  do_twice(func,arg)

def main():
  if len(sys.argv)==2:
    string=sys.argv[1]
  else:
    print "usage: python function-as-argument.py string"
    sys.exit(1)

  print "calling do-four function with print-string and %s as arguments"%string
  do_four(print_string,string)	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
