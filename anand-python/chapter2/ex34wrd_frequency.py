import sys

#Returns the list of words in the _file
def get_words(_file):
  fh=open(_file,'r')
  word_list=fh.read().lower().split()
  fh.close()
  return word_list
#Returns the {word:count} dictionary of the _file
def word_frequency(_file):
  word_list=get_words(_file)
  freq_dict={}
  for word in word_list:
    freq_dict[word]=freq_dict.get(word,0)+1
  return freq_dict
#prints the dictionary in high-frequency-word first fashion
def print_sort(freq_dict):
  _list=freq_dict.items()
  count=lambda word: word[1]
  _list.sort(key=count,reverse=True)
  for word in _list:
    print word[0],'------------------>', word[1]
  return
#This is the main function

def main():
  if len(sys.argv) ==2:
    _file=sys.argv[1] #command line arguments as list of strings
  else:
    print "usage: python module.py file "
    sys.exit(1)  
  freq_dict=word_frequency(_file)
  print_sort(freq_dict)
  '''for word,count in freq_dict.items():
    print word,':',count
  #print "The result : \n", result '''
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
