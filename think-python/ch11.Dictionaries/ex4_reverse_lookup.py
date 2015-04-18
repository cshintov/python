'''

ex 11.4 Implement reverse lookup which returns  the list of keys having given value or empty list if it doesn't exist

'''
def hystogram(string):
  ddict =  dict()
  for char in string:
    ddict[char] = ddict.get(char,0) + 1
  return ddict

def reverse_lookup(ddict,value):
  keys = []
  for key in ddict:
    if ddict[key] == value: 
      keys.append(key)
  return keys
  
def repeat():
  while True:
    string=raw_input('Enter the string:')
    hyst=hystogram(string)
    print 'hystogram of {}:\n{}'.format(string,hyst)
    print
    value=int(raw_input('Enter the value to be searched:'))
    print 'the keys with value:',value
    print reverse_lookup(hyst,value)
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
