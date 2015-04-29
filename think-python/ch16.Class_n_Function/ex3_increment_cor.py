'''
exercise 16.3 Increments the time with the given number of seconds by modifying the time object argument

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

def increment(tm,seconds):
  incr = time()
  incr.hr,rem = divmod(seconds,60**2)
  incr.mt,incr.sc = divmod(rem,60)
  tm.hr += incr.hr
  tm.mt += incr.mt
  tm.sc += incr.sc

def main():
  while True:
    time_a = create_time()
    print 'The time is :'
    print_time(time_a)
    incr = float(raw_input('how many seconds to increment? : ')) 
    increment(time_a,incr)
    print 'The time after increment'
    print_time(time_a)
    
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
