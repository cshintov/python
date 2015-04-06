'''exercise 8.4 Finds the position of a letter in a word if it exists starting from the specified position '''

def find(word,letter,start):
  index=start
  while index < len(word):
    if word[index] == letter:
      return index
    index+=1
  return -1
def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  string=''
  while string != 'yes':
    prompt="Enter the word:"
    word=get_input(prompt)
    prompt="Enter the letter to search:"
    letter=get_input(prompt)
    prompt="Enter from where to search(1 for first letter):"
    start=int(get_input(prompt))
    position=find(word,letter,start-1)+1
    if position!=0:
      print '{} is found at {} th position!'.format(letter,position)
    else:
      print '{} Not found in {} from {} th position onwards!'.format(letter,word,start)
    prompt="exit?yes/no:"
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
