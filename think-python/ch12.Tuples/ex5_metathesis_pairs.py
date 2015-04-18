'''exercise 12.5 finds all the metapairs in the file
  a metapair is two words when swapping two characters gives the other'''

def is_anagram(worda,wordb):
  for char in worda:
    if worda.count(char) !=  wordb.count(char) or worda == wordb:
      return False
  return True

def build_list(filename):
  fin = open(filename)
  words = fin.read().split()
  return words

def signature(word):
  charset=list(word.lower())
  charset.sort()
  return ''.join(charset)
  
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

def is_meta(worda,wordb):
  changes=0
  for c,d in zip(worda,wordb):
    if c != d:
      changes +=1
  return changes == 2
  
def meta_pairs(llist):
  result = []
  for item in llist:
    for index in range(llist.index(item)+1,len(llist)):
      if is_meta(item,llist[index]):
        result.append((item,llist[index]))
  return result
  
def find_meta(result):
  meta = {}
  for key in result:
    meta[key]  = meta_pairs(result[key])
  print_meta(meta)

def print_meta(meta):
  for key in meta:
    if meta[key] != []:
      print meta[key]    
    
def repeat():
  while True:
    filename=raw_input("Enter the filename:")
    result=anagrams(filename)
    string='list of all metathesis pairs in the file\n'
    print string
    find_meta(result)
    if raw_input("\ncontinue?yes/no:") in ('n','no'):
      print "Bye!"
      break

def main(): 
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
