#right justifies the given string into a 100 width line

import sys

def rightjustify(string):
  print "%100s" % string

def main():
  if len(sys.argv)==2:
    string=sys.argv[1]
  else:
    print "usage: python right_justify.py input"
    sys.exit(1)
  rightjustify(string)
	
if __name__=='__main__':
  print '*'*100,'\n'
  main()
  print '\n','*'*100
