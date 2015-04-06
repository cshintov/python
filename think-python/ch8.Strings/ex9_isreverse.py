'''exercise 8.9 Checks whether two words are reverse of each other '''

def is_reverse(word1,word2):
  if len(word1)!=len(word2):
    return False
  j=len(word2)-1
  i=0
  while j >=0:
    if word1[i]!=word2[j]:
      return False  
    j-=1
    i+=1
  return True

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    prompt="Enter the first word:"
    word1=get_input(prompt)
    prompt="Enter the second word:"
    word2=get_input(prompt)
    if is_reverse(word1,word2):
      print "Indeed! They are the reverses of each other!"
    else:
      print "NO! They are Not the reverses of each other!"
    prompt="continue?yes/no:"
    string=get_input(prompt)
    if string=='no': 
      print "Bye!"
      break
      
def main():
  repeat()
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
