'''exercise 9.6 Counts the number of words in the file which is constructed in alphabetical order
'''
def is_abcderian(word):
  for letter in word[:-1]:
    if letter > word[word.index(letter)+1]:
      return False
  return True
  
def count_words(filename):
  choice=raw_input('Do you want to print all abcderian words in this file?yes/no:')
  fin=open(filename)
  count_incl=0
  for word in fin:
    if is_abcderian(word.strip()):
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
    count=count_words(filename)
    print "The number of words in the file '{}' which are constructed in alphabetical order is {}.".format(filename,count)
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
