'''exercise 12.4 anagrams  in a file
a. print them sorted in descending order 
b. find the set of 8 letters which has most possible anagrams in the english language'''

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
  
#solution from the tutorial
def anagrams(filename):
  words = build_list(filename)
  angm_dict = {}
  for word in words:
    sig = signature(word)
    if not sig in angm_dict:
      angm_dict[sig] = [word]
    else :
      angm_dict[sig].append(word)
  #print 'dict',angm_dict
  return angm_dict    

def print_result(result):
  for val in result.values():
    if len(val) > 1:
      print val

def print_sort(result):
  counts = []
  for val in result.values():
    if len(val) > 1:
      counts.append((len(val),val))
  counts.sort(reverse=True)    
  for count,val in counts:
    print val

def find_largest_eight(anagrams):
  large = 'abc'
  for key in  anagrams:
    if len(key) == 8:
      if len(anagrams[key]) > len(anagrams[large]):
        large = key
  return large,len(anagrams[large])
  
def repeat():
  while True:
    filename=raw_input("Enter the filename:")
    result=anagrams(filename)
    print 'anagram list'
    print_result(result)
    print 'sorted anagram list'
    print_sort(result)
    largest_8 = find_largest_eight(result)
    string='character set with length 8 "{}" which has largest (size:{}) number of anagrams in English!\n{}'
    print string.format(largest_8[0],largest_8[1],result[largest_8[0]])
    if raw_input("continue?yes/no:") in ('n','no'):
      print "Bye!"
      break

def main(): 
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
