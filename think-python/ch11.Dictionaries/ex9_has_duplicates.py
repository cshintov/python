'''

ex 11.9 Implement has_duplicate function with dictionaries
        It returns true if the parameter list has elements repeating
        else false

'''

def has_dup(llist):
  ddict =  dict()
  for item in llist:
    ddict[item]=ddict.setdefault(item,0)+1
    if ddict[item]>1:
      return True
  return False
  
def repeat():
  while True:
    string=raw_input('Enter the string:')
    llist=list(string)
    print llist
    if has_dup(llist):
      print 'The given list has duplicates in It!"'
    else:
      print 'The given list has NO duplicates in It!"'
    choice=raw_input('Continue? y:yes / n:no :')
    if choice in ('n','no'):
      print 'Bye!'
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*50
  main()
  print '*'*50  
