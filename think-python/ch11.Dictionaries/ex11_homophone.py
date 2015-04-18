'''exercise 11.11 Finds the five letter words which gives two homophones when the first and second letter is removed in turn'''
from pronounce import *
#builds a list of words from a file ,should contain one word per line
def build_list(filename):
  fin=open(filename)
  _list = []
  for line in fin:
    word=line.strip()
    _list.append(word)
  fin.close()
  return _list

#builds a dictionary of words from a file(should contain one word per line)
def build_dict(filename):
  fin=open(filename)
  _dict = {}
  for line in fin:
    word=line.strip()
    _dict[word]=word
  fin.close()
  return _dict
#finds the five letter words which produces two homophones when the first and second letter is removed in turn
def homophone(words):
  pron_dict = read_dictionary()  
  for word in words.keys():
    if len(word) == 5:
      worda=word[1:]
      wordb=word[0]+word[2:]
      try :
        cond = pron_dict[word] == pron_dict[worda] and pron_dict[word] ==pron_dict[wordb]
        if  cond:
          print '{}--{}--{}'.format(word,worda,wordb)
      #avoids keys which are not in the pronounce dictionary (absurd character combinations)
      except KeyError:
        pass
      
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    words=build_dict(filename)
    homophone(words)
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
