'''exercise 10.6 checks whether a list is sorted in ascending order or not'''


def is_sorted(_list):
  for index in range(len(_list)-1):
    if _list[index] > _list[index+1]:
      return False
  return True
  
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

def repeat():
  while True:
    print 'enter the list:'
    _list=get_list()
    print 'Here is your List'
    print _list
    if is_sorted(_list):
      print 'Your list is a sorted list!'
    else:
      print 'Your list is NOT a sorted list!'
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
