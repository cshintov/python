'''
exercise 13.9 Draw the function of zipf in a graph

'''
from matplotlib import pyplot
from math import log
from string import punctuation
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
  lst = zip(hist_d.values(),hist_d.keys())
  lst.sort(reverse=True)
  lst = lst[:n]
  res = []
  for index,item in enumerate(lst):
     res.append((item[1],item[0],index+1))
  return res

def plot_ranks(zip_lst,scale='log'):
    word,frq,rnk=zip(*zip_lst)
    #calculating the constant s in the zipf equation
    c = float(frq[0])
    rl = range(10,1000)
    sum = 0
    for r in rl:
      k = c/frq[r-1]
      s = log(k,r)
      sum += s  
    s = sum / 990
    
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('Zipf plot')
    pyplot.xlabel('rank')
    pyplot.ylabel('frequency')
    pyplot.plot(rnk,frq, 'b-')
    pyplot.show()
    return s

def zipf(hist_d):
  zip_lst=most_freq(hist_d,len(hist_d))
  print_l(zip_lst)
  s_constant = plot_ranks(zip_lst)
  return s_constant
#transforms the count to probability
def probability(dct):
  print 'prob in',dct
  for key in dct:
    dct[key] = float(dct[key])/total
  return dct

#pretty printing the list
def print_l(l):
  for word,frq,rnk in l:
    print '{:20s} ---- {:} ---- {:}'.format(word+' ',frq,rnk)   

def repeat():
  while True:
    global rang
    filename=raw_input('enter the filename:')
    hist_d = histogram(filename)
    s_constant = zipf(hist_d)
    print "The graph is an aproximate line in the middle portion!"
    print 'constant s:',s_constant
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!\n"
      lst = []
      break
    
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30

