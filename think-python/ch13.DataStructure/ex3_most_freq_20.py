'''exercise 13.3 counts the frequency of each word in a file and prints the most frequently used 20 words in the given file
   in decreasing order
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
    wd_count = wdict.setdefault(word,0)  + 1
    wdict[word] = wd_count
  return wdict,count   

def most_freq_20(wdict):
  decor = []
  for word,count in wdict.items():
    decor.append((count,word))

  decor.sort(reverse=True)

  if len(decor)<20:
    for tup in decor:
      print '{1:20}:{0:3}'.format(*tup)  
  else:
    for index in range(20):
      print '{1:20}:{0:3}'.format(*decor[index])
  return 
  
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='sample'
    word_dict,count = build_dict(filename)
    #print word_dict
    print 'The most frequently used 20 words:'
    most_freq_20(word_dict)
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
