'''exercise 12.2 Sorting words in a list in descending order of length , breaking ties in random order'''
from ex1_sumall import create_tuple
from random import random as rd
#sorts on length (break ties in descending order alphabet)
def sort_descending(words):
  decor=[]
  for word in words:
    decor.append((len(word),word))
  
  decor.sort(reverse=True)
  
  undecor = []
  for length,word in decor:
    undecor.append(word)
  
  return undecor

#sorts on length (break ties in random order)
def sort_random(words):
  decor=[]
  for word in words:
    decor.append((len(word),rd(),word))
  
  decor.sort(reverse=True)
  
  undecor = []
  for length,random,word in decor:
    undecor.append(word)
  
  return undecor

          
def main():
  tup=create_tuple()
  print 'sorted list in descending order of length (break ties descending alphabet) : \n',sort_descending(tup)
  while True:
    print 'sorted list in descending order of length (break ties random) : \n',sort_random(tup)
    if raw_input('continue?:') in ('n','no'):
      print  'bye!'
      break
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
