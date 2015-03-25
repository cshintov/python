import sys

#comment ur function here
def function(arg):
  return result
  
def swap(word,pos):
  _list=[]
  for i in range(pos+1,len(word)):
    char_list=list(word)
    char_list[pos],char_list[i]=char_list[i],char_list[pos]
    _list.append(''.join(char_list))
  return _list

'''def swap(word):
  for pos in range(len(word)-1):
  _list=[swap(word,pos) for pos in range(len(word)-1)]
  return _list'''

def list_o_anagrams(word):
  _anagram_list=[]
  for pos in range(len(word)-1):
    _anagram_list.extend(swap(word,pos))
  #print _anagram_list
  for wd in _anagram_list:
    new_word=wd[::-1]
    if new_word not in _anagram_list and new_word!=word:
      _anagram_list.append(new_word)
  #print _anagram_list
  return _anagram_list
  
def dict_o_anagrams(word_list):
  _dict_anagrams={}
  for word in word_list: 
    _dict_anagrams[word]=list_o_anagrams(word) #adding word:list[its anagrams] pair
  #print _dict_anagrams
  return _dict_anagrams

def group_o_anagrams(word_list):
  print "These are the given words:",word_list
  _dict_anagrams=dict_o_anagrams(word_list) # {word1:[w11,w12..], word2:[w21,w22..], ...}
  _groups={}
  for word in word_list:
    flag='absent'
    for key in _groups:
      if word in _groups[key]: flag='present'
    if flag=='present': continue
    _groups.setdefault(word,[word])
    for i in range(len(word_list)):
      #print word_list[i],':',_dict_anagrams[word]
      if word_list[i] in _dict_anagrams[word] and word_list[i]!=word:
        _groups[word].append(word_list[i])
        #del word_list[i]  

  return _groups
#_groups[word].extend([ word_list[i] for i in range(word_list.index(word)+1,len(word_list)) if ])
#if word_list[i]!=word
#This is the main function
def main():
  #_list_angrm=list_o_anagrams('abc')
  #_dict_angrm=dict_o_anagrams(['abc','abcd','cba'])
  #print _list_angrm
  #print _dict_angrm
  #print _group_angrm
  _group_angrm=group_o_anagrams(['abc','bac','123','321','abcd','cab'])
  print "\n\nThese are the anagrams in the given words:"
  for value in _group_angrm.values():
    print value
  '''if len(sys.argv) >=2:
    args=sys.argv[1:] #command line arguments as list of strings
  else:
    print "usage: python module.py [numlist] "
    sys.exit(1)  
  result=function(args)
  print "The result : \n", result 
  '''
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
