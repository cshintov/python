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
    
#prints the reverse pairs in a list
def reverse_pairs(_list):
  num=0
  rlist=[]
  for word in _list:
    if search(word[::-1],_list) != None:
      rlist.append(word[::-1])
      if not word in rlist:
        num+=1
        print '{:^20}--{:^20}'.format(word,word[::-1])
  
  print 'there are {} reverse pairs in the list'.format(num)
  return
  
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    print
    if filename=='':
      filename='words.txt'
    _list=build_list(filename)
    _list.sort()
    reverse_pairs(_list)
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
