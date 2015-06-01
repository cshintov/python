'''
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
'''

import sys
class zrange:
  def __init__(self,n):
    self.value=n
  def __iter__(self):
    return reverse_iter(self.value)
    
class reverse_iter:
  def __init__(self,n):
    #print "In the iterator"
    self.cur=n
    self.val=0
  def __iter__(self):
    return self
  def next(self):
    if self.cur > self.val:
      temp=self.cur
      self.cur -= 1
      return temp
    else:
      raise StopIteration()
  

#If both iteratable and iterator are the same object, it is consumed in a single iteration.
print "Both iteratable and iterator are the same object"
x=reverse_iter(int(sys.argv[1]))
print list(x)
print list(x) #will print empty list, since x consumed once

#If iteratable and iterator are not the same object, the iterator object can be used many times
print "Using different iterable and iterator"
x=zrange(int(sys.argv[1]))
print list(x)
print list(x) #will print list many times, no empty list

