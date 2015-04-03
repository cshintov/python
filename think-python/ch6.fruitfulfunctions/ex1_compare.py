
def compare(x,y):
  if x < y:
    return -1
  if x > y:
    return 1
  return 0        
  
def main():
  print "compares two values"
  x=raw_input('enter value1:')
  y=raw_input('enter value2:')
  if compare(x,y) == 1:
    print "{0} is greater than {1}".format(x,y)
  if compare(x,y) == -1:
    print "{0} is less than {1}".format(x,y)
  if compare(x,y) == 0:
    print "{0} is equal to {1}".format(x,y)
  
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
