'''
exercise 16.6 Calculate average pace of the runner given the finishing time and the total distance

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

#multiplies the float number with the time 
def mul_time(timea,fnum):
  seconds = time_to_int(timea) * fnum
  return int_to_time(seconds) 

def main():
  while True:
    print 'The finishing time is ?:'
    time_a = create_time()
    mul = float(raw_input('the distance in kilometre? : ')) 
    print 'The average pace in time per kilometre is:'
    print_time(mul_time(time_a,mul**-1))
    
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
