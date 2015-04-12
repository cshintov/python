'''exercise 9.11 Check whether an item is in a (sorted) list or not and returns the position if it exists'''

num=0
#builds a list of words from a file ,should contain one word per line
def build_list(filename):
  fin=open(filename)
  _list = []
  for line in fin:
    word=line.strip()
    _list.append(word)
  fin.close()
  return _list

#helper function(uses binary search) of search function, return position if it exists else None
def helper(word,start,end,_list):
  global num
  num +=1
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
  global num
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    _list=build_list(filename)
    _list.sort()
    word=raw_input('Enter the word to search:')
    position=search(word,_list)
    print position
    if position != None:
      print "The word {} is at {}th position in the list".format(word,position)
    else:
      print "There is no such word in the list!"
    print 'took {} steps!'.format(num)
    num=0
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
