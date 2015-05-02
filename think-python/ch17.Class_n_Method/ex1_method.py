'''
exercise 17.1 Implement increment time program with class methods

'''

class time(object):
  '''time in the format hour:minute:second'''

  #creates a time object with given values
  def __init__(self,hr=0,mt=0,sc=0):
    self.hr = hr
    self.mt = mt
    self.sc = sc

  def valid(self):
    if self.hr < 0 or self.mt < 0 or self.sc < 0:
      print 'Negative values not allowed! ',self.hr,self.mt,self.sc
      return False
    if self.mt >= 60 or self.sc >= 60:
      print 'minutes and seconds can not be greater than or equal to 60!',self.hr,self.mt,self.sc
      return False
    
    return True

  #converts time object to number of seconds
  def time_to_int(self):
    minutes = self.hr * 60 + self.mt
    seconds = minutes * 60 + self.sc
    return seconds

  #prints the time object
  def print_time(tim):
    print 'hour:minute:seconds ==> {:02.0f}:{:02.0f}:{:06.4f}'.format(tim.hr,tim.mt,tim.sc) 
  
  #increment without add_time
  def increment(self,seconds):
    total_sec = self.time_to_int() + seconds
    return int_to_time(total_sec)

#creates a time object with given values
def create_time():
  hr = int (raw_input('enter the hour : '))
  mt = int (raw_input('enter the minutes : '))
  sc = float (raw_input('enter the seconds : '))
  t = time(hr,mt,sc)
  try :
    assert t.valid()
  except AssertionError:
    t = create_time()
  return t

#converts seconds to time object
def int_to_time(seconds):
  tm = time()
  minutes,tm.sc = divmod(seconds,60)
  tm.hr,tm.mt = divmod(minutes,60)
  return tm

  
def main():
  while True:
    time_a = create_time()
    print 'The time is :'
    time_a.print_time()
    incr = float(raw_input('how many seconds to increment? : ')) 
    print 'The time after increment is:'
    time_a.increment(incr).print_time()
    
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
