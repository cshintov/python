'''exercise 9.4 prints the sentence with words in the file which uses only the letters of the given string
'''
def uses_only(letters,word):
  for letter in word:
    if not letter in letters:
      #print '{} excluded ; contains {}'.format(word,letter)
      return False
  #print '{} included'.format(word)
  return True

  
def include_letters(filename,letters):
  fin=open(filename)
  sentence=''
  for word in fin:
    if uses_only(letters,word.strip()):
      sentence+=word.strip()+' '
      
  sentence=sentence.strip()
  fin.close()
  return sentence


def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    letters=raw_input('enter the letters to include(enter continous string):')
    sentence=include_letters(filename,letters)
    print "The sentence made only of the letters in '{}' from the file '{}' is '{}.' :".format(letters,filename,sentence)
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
