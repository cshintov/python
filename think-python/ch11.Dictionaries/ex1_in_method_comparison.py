'''exercise 11.1 Compares time taken by 'in' method to search an item in list and dict along with the bisect_search method'''
import time
#builds a list of words from a file ,should contain one word per line
def build_list(filename):
  fin=open(filename)
  _list = []
  for line in fin:
    word=line.strip()
    _list.append(word)
  fin.close()
  return _list

#builds a dictionaries of words from a file(should contain one word per line)
def build_dict(filename):
  fin=open(filename)
  _dict = {}
  for line in fin:
    word=line.strip()
    _dict[word]=0
  fin.close()
  return _dict


#helper function(uses binary search) of search function, return position if it exists else None
def helper(word,start,end,_list):
  if end < start:
    return None

  middle = ( start + end ) / 2
  if _list[middle] == word:
    return middle
  
  if word < _list[middle]:
    end = middle-1
    return helper(word,start,end,_list)
  
  start = middle +1
  return helper(word,start,end,_list)

#searches a word in a list, returns position if it exists else None
def search(word,_list):
  start=0
  end=len(_list)-1
  position = helper(word,start,end,_list)
  if position != None:
    return position + 1
    
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    _list=build_list(filename)
    _list.sort()
    word=raw_input('Enter the word to search:')
    start=time.clock()
    position=search(word,_list)
    end=time.clock()
    if position != None:
      print "The word {} is at {}th position in the sorted list".format(word,position)
    else:
      print "There is no such word in the list!"
    print 'took {} seconds'.format((end-start)*1000)
    start=time.clock()
    print word in _list
    end=time.clock()
    print 'in list:took {} seconds'.format((end-start)*1000)
    _dict=build_dict(filename)
    start=time.clock()
    print word in _dict
    end=time.clock()
    print 'in dict:took {} seconds'.format((end-start)*1000)
    prompt="continue? y:yes / n:no:"
    string=raw_input(prompt)
    if string=='n': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
