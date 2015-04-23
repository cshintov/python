'''exercise 12.4 finds list of anagrams of a word  in a file
a. prints them sorted in descending order of number of anagrams of character set
b. finds the set of 8 letters which has most possible anagrams in the english language'''

#returns True if the given words are anagrams
def is_anagram(word_a,word_b):
  if len(word_a) != len(word_b):
    return False
  if word_a == word_b:
    return False
  for char in word_a:
    if word_a.count(char) != word_a.count(char):
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
  
#solution from the tutorial(my solution in ex4a_anagrams takes very long time to compute)
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
