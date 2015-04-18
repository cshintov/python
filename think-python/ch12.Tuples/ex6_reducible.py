'''exercise 12.6 find the longest reducible word'''

wdict = {}
lreducible=[]
def build_list(filename):
  fin = open(filename)
  words = fin.read().split()
  return words

def build_dict(filename):
  words = build_list(filename)
  for word in words:
    wdict[word] = word
  return wdict
  
def children(word):
  child_list = []
  for index in range(len(word)-1):
    child = word[:index]+word[index+1:]
    if child in wdict:
      child_list.append(child)
     
  child = word[:-1]
  if child in wdict:
      child_list.append(child)
  return child_list

d={}
def is_reducible(word):
  if word in lreducible or word in ('a','i') : return True
  llist = children(word)  
  for child in llist:
    if is_reducible(child):
      lreducible.append(child)
      return True
  
  return False

def reducible(wdict):
  result = []
  for word in wdict:
    if is_reducible(word):
      result.append(word)
  return result

def largest(llist):
  large=''
  for item in llist:
    if len(item) > len(large):
      large = item
  return large

def repeat():
  while True:
    global wdict,lreducible
    wdict = {}
    lreducible = []
    filename=raw_input("Enter the filename:")
    wdict=build_dict(filename)
    llist = reducible(wdict)
    result = largest(llist)
    print 'largest reducible word:',result
    if raw_input("\ncontinue?yes/no:") in ('n','no'):
      print "Bye!"
      break 

def main(): 
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
