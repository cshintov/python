"""
exercise 18.1 Implement cmp method for time object

"""

class Time(object):
  """
  Represents the time of day.

"""
  #cmp using tuple comparison
  '''
    def __cmp__(self,other):

      t1 = self.hr,self.mt,self.sc
      t2 = other.hr,other.mt,other.sc
      return cmp(t1,t2)'''
  #cmp using integer subtraction
  def __cmp__(self,other):
    if self.hr - other.hr < 0: return -1
    if self.hr - other.hr > 0: return 1

    if self.mt - other.mt < 0: return -1
    if self.mt - other.mt > 0: return 1

    if self.sc - other.sc < 0: return -1
    if self.sc - other.sc > 0: return 1
    
    return 0
  
def create_time():
  t = Time()
  t.hr = int(raw_input('hours:')) 
  t.mt = int(raw_input('minutes:')) 
  t.sc = int(raw_input('seconds:')) 
  return t

def main():
  print 'first time:'
  t1 = create_time()
  print 'second time:'
  t2 = create_time()
  
  if t1 < t2:
    print t1,' is less than',t2
  elif t1 > t2:
    print t1,' is greater than',t2
  elif t1 == t2:
    print t1,'is equal to ',t2

if __name__ == '__main__':
  main()
