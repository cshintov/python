'''exercise 13.7 Write a function that returns a word from a text file according to its frequency (its histogram value)
Uses an efficient algorithm in the tutorial
'''
from string import punctuation
from random import *
#removes header of the gutenberg text file
def remove_head(filename):
  fin=open(filename)
  while True:
    line = fin.readline()  
    if line.startswith('Produced by'):
      break
  return fin
#builds the dictionary word-->count from the given text file
def histogram(filename,remove_header=False):
  if remove_header:
    print 'here'
    fin = remove_head(filename)
  else:
    fin = open(filename)
  fstring = fin.read().lower()
  for char in punctuation:
      fstring = fstring.replace(char,' ')
  wrdlist = fstring.split()
  hist_d = {}
  for word in wrdlist:
    hist_d[word] = hist_d.get(word,0)+1
  return hist_d
#builds the dict of most frequent n words from histogram dict   
def most_freq(hist_d,n=5):
  res_d = {}
  lst = zip(hist_d.values(),hist_d.keys())
  lst.sort(reverse=True)
  lst = lst[:n]
  for val,key in lst:
    res_d[key] = val
  return res_d
#transforms the count to probability
def probability(dct):
  d = dict(dct) 
  total = sum(d.values())
  print '\ntotal:',total
  for key in d:
    d[key] = float(d[key])/total
  return d
#pretty-printing the dictionary d
def print_d(d):
  for key,val in d.items():
    print '{:-<15s}----> {}'.format(key+' ',val)   
#uses binary search to search for the position of the random number generated between 1 and total number of words
def binary(tuplist,num,start,end):
  if tuplist[start][0]> num: 
    return start 
  position = (start+end)/2
  if tuplist[position][0] == num:
    return position
  
  if tuplist[position][0] > num:
    return binary(tuplist,num,start,position)
  if tuplist[position][0] < num:
    return binary(tuplist,num,position+1,end)
#returns the word at the position returned from the binary function    
def search(tuplist,num):
  start = 0
  end = len(tuplist)-1
  position = binary(tuplist,num,start,end)
  return tuplist[position][1]
#returns the word at the position returned from the search function  
def choose(hist_d):
  words = hist_d.keys()
  cumulative_sum = []
  s = 0
  for word in words:
    s += hist_d[word]
    cumulative_sum.append((s,word))
  cumulative_sum.sort()
  rand_num = randint(1,sum(hist_d.values()))
  word=search(cumulative_sum,rand_num)
  return word

def repeat():
  while True:
    global rang
    filename=raw_input('enter the filename:')
    hist_d = histogram(filename)
    print '\nthe probability histogram of the file {}'.format(filename)
    print_d(probability(dict(hist_d)))
    
    print '\nthe probability of each word in the file'
    prob = {}
    rang= randint(10000,15000)
    for i in range(rang):
      word = choose(hist_d)
      prob[word] = prob.setdefault(word,0) + 1
    print_d(probability(prob))
    
    prompt="continue?yes/no:"
    lst = []
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!\n"
      break
    
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
