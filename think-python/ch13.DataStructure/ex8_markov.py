'''
exercise 13.9 Do markov analysis on a text file

'''
from random import choice
from string import punctuation
#pretty printing the dictionary
def print_d(d):
  for prefix,suffix_l in d.items():
    print '{} ---- {}'.format(prefix,suffix_l)   
    
#removes header of the gutenberg text file
def remove_head(filename):
  fin=open(filename)
  while True:
    line = fin.readline()  
    if line.startswith('Produced by'):
      break
  return fin

#builds the word list from the given file
def word_list(filename,remove_header=False):
  if remove_header:
    fin = remove_head(filename)
  else:
    fin = open(filename)
  fstring = fin.read().lower()
  wordlist = fstring.split()
  return wordlist


#builds the prefix_tuple --> suffix_list dictionary
def build_markov(file_a,size=2):
  wordlist = word_list(file_a,remove_header=False)
  markov_d = {}
  for i in range(len(wordlist)-size):
    pref = ()
    for n in range(size):
      pref = pref + (wordlist[i+n],)
    markov_d.setdefault(pref,[]).append(wordlist[i+size])
  return markov_d

#generate random text from the markov dictionary
def rand_text(markov,size=30):
  text = ''
  prefixes = markov.keys()
  pref_len = len(prefixes[0])
  num,pad = divmod(size , (pref_len+1))
  for i in range(num):
    prefix = choice(prefixes)
    
    prefix_txt = ''
    for j in range(pref_len):
      prefix_txt += prefix[j] + ' '
    suffix = choice(markov[prefix])
    text += prefix_txt + suffix + ' '
  
  for i in range(pad):
    text += choice(choice(prefixes)) + ' '
  text = text.strip() + '.'
  
  return text    

def mash_up(d,e):
  return dict(d.items()+e.items())
  
def repeat():
  while True:
    choice="for mashup enter m : "
    choice=raw_input(choice)
    file_a=raw_input('enter the filename:')
    size = int(raw_input("enter the size of the prefix: "))
    size_txt= int(raw_input("Enter the expected size of the random text: "))
    markov_a = build_markov(file_a,size)
    if choice in('m','mashup'): 
      file_b=raw_input('enter the second filename :')
      markov_b = build_markov(file_b,size)  
      print rand_text(mash_up(markov_a,markov_b),size_txt)
    else:
      print rand_text(markov_a,size_txt)
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
