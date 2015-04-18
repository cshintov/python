'''

ex 11.5 Implement invert dictionary using dict method setdefault
        Invert dictionary returns a new dictionary with values as keys and keylist as values

'''
#computes the frequency of each character in the string and returns the char-->frequency dictionary
def hystogram(string):
  ddict =  dict()
  for char in string:
    ddict[char] = ddict.get(char,0) + 1
  return ddict
#Invert dictionary returns a new dictionary with values as keys and keylist(keys with the same value in the original dict) as values
def invert_dict(ddict):
  inverse = {}
  for key in ddict:
    value = ddict[key]
    inverse.setdefault(value,[]).append(key)
  return inverse
  
def repeat():
  while True:
    string=raw_input('Enter the string:')
    hyst=hystogram(string)
    print 'hystogram of {}:\n{}'.format(string,hyst)
    print
    print invert_dict(hyst)
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
