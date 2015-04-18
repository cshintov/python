'''

ex 11.2 Counting number of occurrences of a character in a string using get method

'''
def hystogram(string):
  ddict =  dict()
  for char in string:
    ddict[char] = ddict.get(char,0) + 1
  return ddict

def repeat():
  while True:
    string=raw_input('Enter the string:')
    print 'hystogram of {}:\n{}'.format(string, hystogram(string))
    choice=raw_input('Continue? y:yes / n:no :')
    if choice in ('n','no'):
      print 'Bye!'
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*50
  main()
  print '*'*50  
