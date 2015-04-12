'''exercise 9.10 Create a list of words from the given file
   file should contain one word per line(use both list building methods)
   which one is faster?
   Answer:append is faster
   why?: + copies the whole right hand side list to the left handside list
         while append just add the element at the end of the list'''

import time

def build_list_a(filename):
  fin=open(filename)
  _list = []
  start=time.clock()
  for line in fin:
    word=line.strip()
    _list += [word]  #slower
  end=time.clock()
  print 'Time taken by + operator to build the list:{} seconds'.format(end-start)
  fin.close()
  
def build_list_b(filename):
  fin=open(filename)
  _list = []
  start=time.clock()
  for line in fin:
    word=line.strip()
    _list.append(word) #faster
  end=time.clock()
  print 'Time taken by append method to build the list:{} seconds'.format(end-start)
  fin.close()

def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='my.txt'
    build_list_a(filename)
    build_list_b(filename)
    prompt="continue? y:yes / n:no:"
    string=raw_input(prompt)
    if string=='n': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
  
