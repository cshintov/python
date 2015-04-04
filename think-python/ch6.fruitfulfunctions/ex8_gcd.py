'''
exercise:6.8 find the gcd of number a and number b

'''

def gcd(numa,numb):
  if numb == 0:
    return numa
  return gcd(numb,numa%numb)

def get_input(prompt):
  num=int(raw_input(prompt))
  return num
  
def main():
  prompt="enter the number a:"
  numa=get_input(prompt)
  prompt="enter the number b:"
  numb=get_input(prompt)
  result=gcd(numa,numb)
  print "{0} is the gcd of {1} and {2}!".format(result,numa,numb)

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
