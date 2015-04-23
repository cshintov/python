'''exercise 12.1 Implements variable argument sum method'''


#Creates a tuple out of the user input elements
def create_tuple():
  tup = ()
  index = 0
  while True:
    item=raw_input('Enter the next item(prefix n for integers)(s for strings)(tuple for nested tuple)(enter done when done!):')
    if item == 'done': 
      return tup
    if item == 'tuple': 
      item = create_tuple()
    if item[0] == 's':
      item = item[1:]
    if item[0] == 'n':
      item=int(item[1:])
    tup = tup[:] + (item,)

#Implements variabble argument sum
def sumall(*args):
  return sum(args)
      
def repeat():
  while True:
    choice = raw_input('Create a tuple?: y:yes n:no -- ')
    if not choice in ('n','no'):
      tup = create_tuple()
      print 'the tuple:\n',tup
    print 'sum of {} is {} '.format( tup, sumall(*tup) )
    prompt="continue? y:yes / n:no:"
    string=raw_input(prompt)
    if string=='n': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
