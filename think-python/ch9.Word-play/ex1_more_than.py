'''exercise 9.1 Print all the words having length more than the specified length'''

def more_than(fin,min_length):
  for line in fin:
      word=line.strip()
      if len(word) > min_length:
        print word
      
def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    filename=get_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    fin=open(filename)
    prompt="Enter the minimum length:"
    min_length=int(get_input(prompt))
    more_than(fin,min_length)
    prompt="continue?yes/no:"
    string=get_input(prompt)
    if string=='no': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
