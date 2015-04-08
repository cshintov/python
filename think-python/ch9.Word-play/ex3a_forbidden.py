'''exercise 9.3a prints the number of words which doesn't have any letter of the given string
'''
def has_no(letters,word):
  for letter in letters:
    if letter in word:
      print '{} excluded ; contains {}'.format(word,letter)
      return False
  print '{} included'.format(word)
  return True

  
def exclude_letters(fin,letters):
  count_e=0
  total=0
  for word in fin:
    total+=1
    if has_no(letters,word.strip()):
      count_e+=1
  return count_e


def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    fin=open(filename)
    letters=raw_input('enter the letters to exclude(enter continous string):')
    count=exclude_letters(fin,letters)
    print "The number of words in the file '{}' without any of the letter in'{}' is {} :".format(filename,letters,count)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string=='no': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
