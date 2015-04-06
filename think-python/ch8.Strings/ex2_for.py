'''exercise 8.2 Prints the names of the ducklings in alphabetical order '''

def print_words(prefixes,suffix):
  for char in prefixes:
    if char == 'O' or char =='Q':
      word=char + 'u' + suffix
    else:
      word=char + suffix
    print word

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  string=''
  while string != 'yes':
    prompt="Enter the Prefixes:"
    prefixes=get_input(prompt)
    prompt="Enter the Suffix:"
    suffix=get_input(prompt)
    print_words(prefixes,suffix)
    print 'enter yes to exit no to continue'
    prompt="exit?:"
    string=get_input(prompt)
    if string=='yes': 
      print "Bye!"
      break

def main():
  repeat()
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
