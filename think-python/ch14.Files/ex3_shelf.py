'''
exercise 14.2 implements sed , replacing all the occurrences of a word with another word in a file 
write that word to another file

'''
import shelve
from anagram_sets import *
def store_anagrams(sh,agrams):
  for key in agrams:
    sh[key] = agrams[key]
    
def read_anagrams(sh,word):
  sig = signature (word)
  anagram_lst = sh[sig]
  anagram_lst.remove(word)
  return anagram_lst

def main():
  agrams = all_anagrams('words')
  sh = shelve.open('anagrams.db')
  store_anagrams(sh,agrams)
  while True:
    word = raw_input('enter the word to lookup for anagrams: ')
    print read_anagrams(sh,word)
    word = raw_input('continue?: y/yes n/no ')
    if word in ('n','no'):
      sh.close()
      print 'Bye!'
      return            
    
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
