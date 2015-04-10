'''exercise 10.4 returns a list barring the first and last elements
  for example middle list of [1,2,3,4] is [2,3]
  exercise 10.5 chop modifies the incoming list by removing the first and last elements of the list
  and returns none
'''

def chop(_list):
  _list.pop(0)
  _list.pop()
  
def middle(_list):
  return _list[1:-1]

        
def main():
  _list=[1,2,3,4]
  print 'the middle of the list: {} is {}'.format(_list,middle(_list))
  chop(_list)
  print 'the list after chop:',_list
  
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
