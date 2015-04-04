'''
exercise:6.7 check whether number a is a power of number b

'''

def is_power(numa,numb):
  if numa == 0 or numa % numb != 0:
    return False
  if  numa == numb or is_power(numa/numb,numb):
    return True

def get_input(prompt):
  num=int(raw_input(prompt))
  return num
  
def main():
  prompt="enter the number a:"
  numa=get_input(prompt)
  prompt="enter the number b:"
  numb=get_input(prompt)
  result=is_power(numa,numb)
  if result:
    print "{0} is a power of {1}!".format(numa,numb)
  else:
    print "{0} is NOT a power of {1}!".format(numa,numb)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
