'''exercise 12.4 prints the anagram lists in descending order of number of anagrams
'''

def is_anagram(worda,wordb):
  if len(worda)!=len(wordb)or worda == wordb:return False
  for char in worda:
    if worda.count(char) !=  wordb.count(char):
      return False
  return True

def build_list(filename):
  fin = open(filename)
  words = fin.read().split()
  return words

def build_dict(filename):
  wdict = dict()
  words = build_list(filename)
  for word in words:
    wdict[word] = word
  return wdict
  
def anagrams(filename):
  count = 0
  words = build_dict(filename)
  angm_dict = {}
  for worda in words:
    visited = False
    angm_dict[worda] = [worda]
    for key in angm_dict:
      if is_anagram(worda,key):
        visited = True
    if visited:
      angm_dict.pop(worda)
      continue
    for wordb in words:
      if is_anagram(worda,wordb):
        count = len(angm_dict[worda]) + 1
        angm_dict[worda].append(wordb)
        
    angm_dict[worda].insert(0,count)
    if angm_dict[worda][0]==0:
      angm_dict.pop(worda)
    count = 0
  return angm_dict

def print_sort(result):
  counts = []
  for key,val in result.items():
    counts.append((val[0],key))
  counts.sort(reverse=True)    
  for item in counts:
    print result[item[1]][1:]

def print_result(result):
  for val in result.values():
    print val[1:]
    
def repeat():
  while True:
    filename=raw_input("Enter the filename:")
    result=anagrams(filename)
    print_sort(result)
    if raw_input("continue?yes/no:") in ('n','no'):
      print "Bye!"
      break

def main(): 
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
