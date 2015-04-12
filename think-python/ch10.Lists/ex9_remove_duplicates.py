'''exercise 10.9 remove duplicates from a list and return the new list'''
from random import randint

#returns true if a list has duplicate items in it , else false
def has_duplicates(_list):
  for item in _list:
    if _list.count(item) > 1:
      return True
  return False
#generates a class of 23 students with their birthdays as elements
def get_list():
  _list= []
  while True:
    prompt='''enter the next item of the list:
            (enter "list" for nested list)
            (enter done when finished)
            >>>'''
    item=raw_input(prompt)
    if item == 'done':
      return _list
    if item.isdigit():
      item=int(item)
    elif item == 'list':
      item=get_list()
    elif item.isalpha() or item.isalnum():
      item=item
    else:
      print 'Unknown type item!'
      continue
    _list.append(item)
#returns a new list of unique items in the input lsit
def remove_duplicates(_list):
  new_list = []
  for item in _list:
    if not item in new_list:
      new_list += [item]
  return new_list
  
def repeat():
  while True:
    print 'enter the list:'
    _list=get_list()
    print 'Here is your List'
    print _list
    print 'the unique element list is'
    print remove_duplicates(_list)
    prompt="continue? y:yes / n:no:"
    string=raw_input(prompt)
    if string == 'n': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
