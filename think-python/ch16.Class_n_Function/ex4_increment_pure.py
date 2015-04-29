'''
exercise 16.4 Returns a new time object after incrementing  the time with the given number of seconds
              without modifying the time object argument(pure function)

'''

class time(object):
  '''time in the format hour:minute:second'''

def create_time():
  t = time()
  t.hr = int (raw_input('enter the hour : '))
  t.mt = int (raw_input('enter the minutes : '))
  t.sc = float (raw_input('enter the seconds : '))
  return t

def print_time(tim):
  print '\nhour:minute:seconds ==> {:02.0f}:{:02.0f}:{:06.4f}'.format(tim.hr,tim.mt,tim.sc) 

def add_time(timea,timeb):
  sum = time()
  sum.hr = timea.hr + timeb.hr
  sum.mt = timea.mt + timeb.mt
  sum.sc = timea.sc + timeb.sc
  return sum

def increment(tm,seconds):
  incr = time()
  incr.hr,rem = divmod(seconds,60**2)
  incr.mt,incr.sc = divmod(rem,60)
  incr = add_time(tm,incr)
  return incr
  
def main():
  while True:
    time_a = create_time()
    print 'The time is :'
    print_time(time_a)
    incr = float(raw_input('how many seconds to increment? : ')) 
    print 'The time after increment'
    print_time(increment(time_a,incr))
    
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
