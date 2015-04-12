'''exercise 9.12 prints all the reverse pairs in the given list'''

#builds a list of words from a file ,should contain one word per line
def build_list(filename):
  fin=open(filename)
  _list = []
  for line in fin:
    word=line.strip()
    _list.append(word)
  fin.close()
  return _list

#helper function(uses binary search) of search function
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

#returns True if the 'n-split' words are in the list else False
def split(word,_list,n):
  for i in range(n):
    sub = word[i::n]
    if not search(sub,_list):
      return False
  return True
  
#prints the interlocked word along with its sub-words
def interlock_pairs(_list,at):
  num = 0
  for word in _list:
    if split(word,_list,at):
      num += 1
      for i in range(at):
        print '{:^20}--'.format(word[i::at]),
      print '{:^30}'.format(word)
  print 'there are {} interlocking pairs in the list'.format(num)
  return
  
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    at=int(raw_input('split at:'))
    if filename=='':
      filename='words.txt'
    _list=build_list(filename)
    _list.sort()
    interlock_pairs(_list,at)
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
