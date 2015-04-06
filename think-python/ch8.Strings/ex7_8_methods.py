'''exercise 8.7 and 8.8 invoke str.count and use str.strip and str.replace '''

def function(choice):
  string=get_input('enter the string:')
  
  if choice == 'c':
    sub=get_input('enter the substring:')
    count=string.count(sub)
    print 'There are {} instances of {} in {}'.format(count,sub,string)
  if choice == 'r':
    sub=get_input('enter the substring:')
    replacement=get_input('enter the replacement:')
    newstring=string.replace(sub,replacement)
    print 'The new string is {}'.format(newstring)
    
  if choice == 's':
    charset=get_input('enter characters to strip:')
    newstring=string.strip(charset)
    print 'The new string is {}'.format(newstring)

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    prompt="Enter choice(c:count,s:strip,r:replace):"
    function(get_input(prompt))
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
