import sys
import string
def insert(word,alpha):
  _list=[]
  for c in alpha:
    for pos in range(len(word)+1):
      mute_word=list(word)
      mute_word.insert(pos,c)  
      _list.append(''.join(mute_word))
  return _list

def rem_char(word,i):
  word=list(word)
  word.remove(word[i])
  mute_word=''.join(word)
  return mute_word

def delete(word):
  _list=[rem_char(word,i) for i in range(len(word))]
  return _list

def replace(word,alpha):
  _list=[]
  for c in alpha:
    for pos in range(1,len(word)+1):
      mute_word=list(word)
      mute_word.insert(pos,c)  
      mute_word.remove(mute_word[pos-1])
      _list.append(''.join(mute_word))
  return _list

def swap(word,pos):
  word=list(word)
  word[pos],word[pos+1]=word[pos+1],word[pos]
  word=''.join(word)
  return word

def swap_adj(word):
  _list=[swap(word,pos) for pos in range(len(word)-1)]
  return _list
  
#mutates the word
def mutate(word):
  mute_list=[]
  alpha=string.lowercase
  mute_list.extend(insert(word,alpha))
  #print mute_list
  #print len(mute_list)'''
  mute_list.extend(delete(word))
  #print mute_list
  mute_list.extend(replace(word,alpha))
  #print mute_list
  mute_list.extend(swap_adj(word))  
  return mute_list

#This is the main function

def main():
  if len(sys.argv) ==2:
    word=sys.argv[1] #command line arguments as ___list of strings
  else:
    print "usage: python ex32mutate.py [alphabetic-word] "
    sys.exit(1)  
  result=mutate(word)
  print "The result : \n", result 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
