import sys
import os

def main():
  #print os.listdir('.')
  if len(sys.argv)==2:
    _dir=sys.argv[1]
  else:
    print "usage: python ex01listdir.py directory-path"
    sys.exit(1)
  print "These are the contents of the given directory:\n"
  print os.listdir(_dir)

	
if __name__=='__main__':
  print '*'*15,'\n'
  main()
  print '\n','*'*15
