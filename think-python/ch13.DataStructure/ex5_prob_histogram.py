'''exercise 13.5 Write a function that returns a character from a string according to its frequency in the string (its histogram)
   returns random character proportional to its frequency in the string
'''
from random import *

#pretty-printing the dictionary d
def print_d(d):
  for key,val in d.items():
    print '{:-<15s}----> {}'.format(key+' ',val)   
#returns the char --> count dict of the string    
def histogram(string):
  hist = {}
  for char in string:
    hist[char] = hist.setdefault(char,0) + 1
  return hist
  
#creates a list of characters according to their frequency in the string
lst = []
def create(hist_d):
  for key,val in hist_d.items():
    lst.extend([key]*val)
  return
#choose_from_hists from the characters proportional to the frequency of the char in the histogram
def choose_from_hist(hist_d):
  return choice(lst)

#transforms the count to probability
def probability(d,total):
  for key in d:
    d[key] = float(d[key])/total
  return d

def repeat():
  while True:
    global rang
    string=raw_input('enter the string:')
    hist_d = histogram(string)
    print '\nthe histogram of the string'
    print_d(probability(dict(hist_d),len(string)))
    create(hist_d )
    print '\nthe probability of each character in the string'
    prob = {}
    rang=randint(10000,15000)
    print 'count',rang
    for i in range(rang):
      char = choose_from_hist(hist_d)
      prob[char] = prob.setdefault(char,0) + 1
    print prob
    print_d(probability(prob,rang))
    
    lst = []
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
