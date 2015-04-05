'''
exercise:7.5 Uses Ramanujan's formula for estimating the value of pi
'''

import math as m

def numerator(k):
'''Returns the numerator of the summation term given k'''
  return m.factorial(4*k)*(1103+26390*k)

def denominator(k):
'''Returns the denominator of the summation term given k'''
  return m.pow(m.factorial(k),4)*m.pow(396,4*k)

def estimate_pi():
  summation,k,term=0,0,1
  epsilon=1e-15
  constant=2*m.sqrt(2)/9801
  while  term >= epsilon:
    print term
    term = numerator(k)/denominator(k) 
    summation+=term
    k+=1
  pi_inverse=constant*summation
  return 1/pi_inverse

def main():
  result=estimate_pi()
  print "The Estimate of Pi using Ramanujan's formula :",result
  print "The Value of Pi given by math.pi :",m.pi

if __name__=='__main__':
  print '*'*55,'\n'
  main()
  print '\n','*'*55

