'''exercise 10.8 birthday paradox'''
from random import randint

#returns true if a list has duplicate items in it , else false
def has_duplicates(_list):
  for item in _list:
    if _list.count(item) > 1:
      return True
  return False
#generates a class of 23 students with their birthdays as elements
def generate_class():
  _class=[]
  for i in range(23):
   _class.append(randint(1,365)) 
  return _class
#count the number of instances when a class has students with same birthdays in 1000 classes  
def count_duplicates():
  count = 0
  for index in range(1000):
    _class=generate_class()
    if has_duplicates(_class):
      count += 1
  return count
#Calculates the probability of birthday paradox by taking the average of 750 iterations
def birthday_paradox():
  _sum=0
  for i in range(750):
    count=count_duplicates()
    _sum += count
  average = _sum / 750
  probability = average/1000.0 * 100
  print 'The chance that in a class of 23 students two having the same birthday is {}!'.format(probability)
  
def repeat():
  while True:
    birthday_paradox()
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string=='no': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
