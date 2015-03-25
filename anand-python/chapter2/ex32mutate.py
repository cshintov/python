import sys
import string

#Inserts from [a-z] in each position of the string , returns the list of such words
def insert(word,alpha):
  _list=[]
  for c in alpha:
    for pos in range(len(word)+1):
      mute_word=list(word)
      mute_word.insert(pos,c)  
      _list.append(''.join(mute_word))
  return _list
  
#Removes the character from the word at the position i, returns the changed word
def rem_char(word,i):
  word=list(word)
  word.remove(word[i])
  mute_word=''.join(word)
  return mute_word
  
#Deletes the character from each position, returns the list of such words
def delete(word):
  _list=[rem_char(word,i) for i in range(len(word))]
  return _list
#Replaces each character of the word by a char from [a-z], returns the list of such words
def replace(word,alpha):
  _list=[]
  for c in alpha:
    for pos in range(1,len(word)+1):
      mute_word=list(word)
      mute_word.insert(pos,c)  
      mute_word.remove(mute_word[pos-1])
      _list.append(''.join(mute_word))
  return _list

#Given a position and the word, swaps the charaters at position and the next positions
def swap(word,pos):
  word=list(word)
  word[pos],word[pos+1]=word[pos+1],word[pos]
  word=''.join(word)
  return word

#Swaps adjacent characters of the word and returns the list of such words
def swap_adj(word):
  _list=[swap(word,pos) for pos in range(len(word)-1)]
  return _list
  
#mutates the word (insert with [a-z],delete a character,replace with [a-z],swap adjacent chars)
def mutate(word):
  mute_list=[]
  alpha=string.lowercase
  mute_list.extend(insert(word,alpha))
  mute_list.extend(delete(word))
  mute_list.extend(replace(word,alpha))
  mute_list.extend(swap_adj(word))  
  return mute_list

#This is the main function

def main():
  if len(sys.argv) ==2:
    word=sys.argv[1] 
  else:
    print "usage: python ex32mutate.py 'string' "
    sys.exit(1)  
  result=mutate(word)
  print "The result : \n", result 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
