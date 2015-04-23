'''
exercise 13.2 counts the frequency of each word in a file

'''
from string import punctuation,whitespace
def build_dict(filename):
  fin=open(filename)
  while True:
    line = fin.readline()[:8]  
    if line == 'Produced':
      break
  fstring = fin.read()  
  wdict = {}
  for char in punctuation:
      fstring = fstring.replace(char,'')
  wrdlist = list(fstring.split())
  count = 0
  for word in wrdlist:
    count += 1
    wdict[word] = wdict.setdefault(word,0)  + 1
  return wdict,count   

def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='sample'
    word_dict,count = build_dict(filename)
    print 'the total number of words in the book:',count
    print 'the number of different words used in the book:',len(word_dict)
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
