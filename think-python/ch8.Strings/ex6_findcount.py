''' exercise 8.6 Counts number of occurrences of a letter in a word using find function from pr '''


def find(word,letter,start):
  index=start
  while index < len(word):
    if word[index] == letter:
      return index
    index+=1
  return -1

def count(word,letter):
  count=0
  position=find(word,letter,0)
  while position != -1:
    count+=1
    position=find(word,letter,position+1)
  return count

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  string=''
  while string != 'yes':
    prompt="Enter the word:"
    word=get_input(prompt)
    prompt="Enter the letter to count:"
    letter=get_input(prompt)
    _count=count(word,letter)
    if _count!=0:
      print '{} occurs {} times in {}!'.format(letter,_count,word)
    else:
      print '{} Not found in {}!'.format(letter,word)
    prompt="exit?yes/no:"
    string=get_input(prompt)
    if string=='yes': 
      print "Bye!"
      break

def main():
  print "new"
  repeat()
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
