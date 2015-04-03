def b(z):
  prod=a(z,z)
  print z,prod
  return prod
  
def a(x,y):
  x=x+1
  return x*y
  
def c(x,y,z):
  total=x+y+z
  square=b(total)**2
  return square

def main():
  prompt='enter the number:'
  x=float(raw_input(prompt))
  y=x+1
  print "the result:",c(x,y+3,x+y)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
