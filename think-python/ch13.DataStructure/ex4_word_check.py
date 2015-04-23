'''exercise 13.4 given a word list and a text file prints all the words in the book that are not in the word list
   counts typos
'''
from string import punctuation
from meta import *
#removes header which start with Produced from the gutenberg file
def build_dict(filename):
  fin=open(filename)
  while True:
    line = fin.readline()[:8]  
    if line == 'Produced':
      break
  return build_d(fin)
#builds a dictionary word==>count from the given file
def build_d(fin):
  fstring = fin.read().lower()
  wdict = {}
  for char in punctuation:
      fstring = fstring.replace(char,' ')
  wrdlist = fstring.split()
  count = 0
  for word in wrdlist:
    count += 1
    wd_count = wdict.setdefault(word,0)  + 1
    wdict[word] = wd_count
  return wdict,count   

word_lst={}
def not_in_list(file_words_d):
  not_lst_d={}
  for word in file_words_d:
    if not word in word_lst:
      not_lst_d[word] = 1
  return not_lst_d

#checks three types of typos, omission of one character,misspelling one character,swapping two characters(meta-pair)
def is_typo(worda,wordb):
  condition = [is_child(worda,wordb),is_meta(worda,wordb),is_fraud(worda,wordb)]
  if any(condition):
    return True
  return False
#filters the typos from the list of words in the file which are not in the word list
def typos(file_words_d):
  typo_words = []
  not_list = not_in_list(file_words_d)
  print len(not_list)
  for worda in not_list:
    for wordb in word_lst:
      if is_typo(worda,wordb):
        typo_words.append(worda)
        break
  return typo_words
  
def repeat():
  while True:
    global word_lst
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='sherlock'
    word_dict,count = build_dict(filename)
    print '\nthere are {} the words in the file'.format(len(word_dict))
    words=raw_input('enter the filename:')
    if words=='':
      words='words'
    word_lst,count=build_d(open(words))
    not_list = not_in_list(word_dict)
    print '\nthere are {} words in the file not in the given word list'.format(len(not_list)) 
    #counting typo words takes long time,for small files it works fine,else takes eternity 
    '''typo_words = typos(word_dict)
    print '\nthere are {} typos in the file'.format(len(typo_words))
    print '\nthese are the typos in the file'
    print typo_words'''
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
