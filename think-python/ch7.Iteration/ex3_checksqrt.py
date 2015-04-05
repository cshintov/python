'''
exercise:7.3 Computes the square root of a number using Newtons approximation method
compares it with the result of the builtin method sqrt in math module and prints the
absolute difference between both the results

'''
import math
def get_input(prompt):
  num=raw_input(prompt)
  return num

def sqrt(num):
  epsilon = 0.000000001
  rt=num/2
  while True:
    newrt=(rt+num/rt)/2
    if abs(newrt-rt) < epsilon :
      return newrt   
    rt=newrt

def checksqrt(num):
  itrnum=1.0
  while itrnum <= num:
    myrt=sqrt(itrnum)
    mathrt=math.sqrt(itrnum)
    absdif=abs(mathrt-myrt)
    string="{:>6.1f} | {:>12.11f} | {:>12.11f} | {:12.10}".format(itrnum,myrt,mathrt,absdif)
    print string
    itrnum+=1

def main():
  prompt="enter the number limit :  "
  num=float(get_input(prompt))
  print "\n{0:>6s} | {1:13s} | {2:13s} | {3:<13s}".format('Number','MyRoot','MathRoot','AbsDifference')
  print "-"*55
  checksqrt(num)
  
if __name__=='__main__':
  print '*'*55,'\n'
  main()
  print '\n','*'*55
