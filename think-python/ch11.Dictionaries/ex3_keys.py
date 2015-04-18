'''

ex 11.3 Use keys method of dict to print the keys and values in alphabetical order of the keys

'''
def hystogram(string):
  ddict =  dict()
  for char in string:
    ddict[char] = ddict.get(char,0) + 1
  return ddict

def print_hyst(hyst):
  keys=sorted(hyst.keys())
  for key in keys:
    print '{:^20} : {:^20}'.format(key,hyst[key])

def repeat():
  while True:
    string=raw_input('Enter the string:')
    hyst=hystogram(string)
    print 'hystogram of {}:\n{}'.format(string,hyst)
    print 'hystogram in alphabetical order:'
    print_hyst(hyst)
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
