'''exercise 12.5 finds all the metapairs in the file
  a metapair is two words when swapping two characters gives the other'''

#builds the word list from the text file
def build_list(filename):
  fin = open(filename)
  words = fin.read().split()
  return words
#gets teh signature of the word , character set of the string in sorted order
def signature(word):
  charset=list(word.lower())
  charset.sort()
  return ''.join(charset)
#creates the signature-->anagram_list dictionary
def anagrams(filename):
  words = build_list(filename)
  angm_dict = {}
  for word in words:
    sig = signature(word)
    if not sig in angm_dict:
      angm_dict[sig] = [word]
    else :
      angm_dict[sig].append(word)
  return angm_dict    
#returns true if worda and wordb are metapairs else False
def is_meta(worda,wordb):
  changes=0
  for c,d in zip(worda,wordb):
    if c != d:
      changes +=1
  return changes == 2
#returns the list of metapairs in a anagram_list(value of a signature)
def meta_pairs(llist):
  result = []
  for item in llist:
    for index in range(llist.index(item)+1,len(llist)):
      if is_meta(item,llist[index]):
        result.append((item,llist[index]))
  return result
#transforms the signature --> anagram_list dictionary to signature-->meta_pair_list dictionary  
def find_meta(result,prnt=True):
  meta = {}
  for key in result:
    meta[key]  = meta_pairs(result[key])
  if prnt:
    return print_meta(meta,True)
  else:
    return print_meta(meta,False)
#prints the meta pair list if prnt is True else just computes teh number of meta pairs in the file
def print_meta(meta,prnt):
  count = 0
  for key in meta:
    if meta[key] != []:
      if prnt:
        print meta[key]    
      count += 1
  return count
  
def repeat():
  while True:
    filename=raw_input("Enter the filename:")
    result=anagrams(filename)
    if raw_input('print meta pairs? n:no y:yes :') in ('y','yes'):
      string='metathesis pairs in the file\n'
      print string
      count = find_meta(result,True)
      print 'the number of meta pairs in the file {}:'.format(count)
    else:
      print 'the number of meta pairs in the file {}:'.format(find_meta(result,False))
    
    if raw_input("\ncontinue?yes/no:") in ('n','no'):
      print "Bye!"
      break

def main(): 
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
