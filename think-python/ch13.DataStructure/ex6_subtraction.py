'''
exercise 13.4 given a word list and a text file prints all the words in the book that are not in the word list
using set 

'''
from string import punctuation

def remove_head(filename):
  fin=open(filename)
  while True:
    line = fin.readline()  
    if line.startswith('Produced by'):
      break
  return fin

def build_set(filename,remove_header=False):
  if remove_header:
    fin = remove_head(filename)
  else:
    fin = open(filename)
  fstring = fin.read().lower()
  for char in punctuation:
      fstring = fstring.replace(char,' ')
  wrdlist = fstring.split()
  return set(wrdlist)
#set difference of seta - setb ; set such that elements in seta but not in setb
def subtract(seta,setb):
  return seta-setb

def repeat():
  while True:
    filename=raw_input('enter the filename(a file from project gutenberg):')
    if filename=='':
      filename='sherlock'
    file_words = build_set(filename,remove_header=True)
    print '\nthere are {} the words in the file'.format(len(file_words))
    words=raw_input('enter the filename:')
    if words=='':
      words='words'
    words = build_set(words)
    diff = subtract(file_words,words)
    #to print the difference set uncomment the following statement
    #print diff
    print '\nthere are {} words in the file not in the given word list'.format(len(diff)) 
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
