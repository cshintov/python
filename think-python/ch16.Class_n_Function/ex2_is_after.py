
'''
exercise 16.2 checks whether timea is after timeb

'''
from ex1_print_time import *

#is_after using if
def if_after(timea,timeb):
  if timea.hr < timeb.hr:
    return False
  elif timea.hr == timeb.hr:
    if timea.mt < timeb.mt:
      return False
    elif timea.mt == timeb.mt:
      if timea.sc < timeb.sc:
        return False
  return True

def abs(a):
  
  return (a.hr) * (60 ** 2) + (a.mt) * 60 + a.sc

#is_after without if
def is_after(timea,timeb):

  return abs(timea) > abs(timeb)

def main():
  while True:
    time_a = create_time()
    time_b = create_time()
    if is_after(time_a,time_b):
      print "Time a is after time b!"
    else :
      print "Time a is NOT after time b!"
      
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
