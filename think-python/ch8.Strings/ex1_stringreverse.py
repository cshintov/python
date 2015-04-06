'''exercise 8.1 Print letters of a string backwards each on a new line'''

def backward(string):
  index=len(string)-1
  while index >=0 :
    print string[index]
    index-=1

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  string='start'
  print 'enter quit to exit'
  while string != 'quit':
   prompt="Enter the string:"
   string=get_input(prompt)
   if string=='quit': 
    print "Bye!"
    break
   backward(string)
  
def main():
  repeat()  
  
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
