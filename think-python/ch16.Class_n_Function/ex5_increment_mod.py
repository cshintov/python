'''
exercise 16.5 Increment using int to time and time to int functions

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

def time_to_int(t):
  minutes = t.hr * 60 + t.mt
  seconds = minutes * 60 + t.sc
  return seconds

def int_to_time(seconds):
  tm = time()
  minutes,tm.sc = divmod(seconds,60)
  tm.hr,tm.mt = divmod(minutes,60)
  return tm

#increment could be written using add_time
def add_time(timea,timeb):
  seconds = time_to_int(timea) + time_to_int(timeb)
  return int_to_time(seconds) 

#increment without add_time
def increment(tm,seconds):
  total_sec = time_to_int(tm) + seconds
  return int_to_time(total_sec)
  
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
