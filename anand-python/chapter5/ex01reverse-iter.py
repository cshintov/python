'''
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
'''
import sys
import os
class reverse:
  def __init__(self,_list):
    self._list=_list
  def __iter__(self):
    return reverse_iter(self._list)
    
class reverse_iter:
  def __init__(self,_list):
    self._list=_list
    self.current = len(_list)
    self.end = 0
  def __iter__(self):
    return self
  def next(self):
    if self.current > self.end :
      self.current -= 1
      return self._list[self.current]
    else:
      raise StopIteration()
  
def main():
  result = reverse(['shinto','shanto','varghese','sheela'])
  print "the result:",list(result)
  print "Calling second time:"
  print "the result:",list(result)
  print "Calling third time:"
  print "the result:",list(result)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
