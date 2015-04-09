'''exercise 9.5 Counts the number of words in the file which uses all the letters in the given string at least once
'''
def uses_all(letters,word):
  for letter in letters:
    if not letter in word:
      return False
  return True
  
def count_words(filename,letters):
  choice=raw_input('Do you want to print words using all of {} in this file?yes/no:'.format(letters))
  fin=open(filename)
  count_incl=0
  for word in fin:
    if uses_all(letters,word.strip()):
      if choice == 'yes':
        print word.strip()
      count_incl+=1
  fin.close()
  return count_incl


def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    letters=raw_input('enter the letters to be used at least once(enter continous string):')
    count=count_words(filename,letters)
    print "The number of words in the file '{}' which uses all of the letters in '{}' is '{}.'".format(filename,letters,count)
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
