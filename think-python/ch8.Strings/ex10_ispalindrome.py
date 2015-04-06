'''exercise 8.10 implement is_palindrome using slice step size'''

def is_palindrome(word):
  return word == word[::-1]

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    prompt="Enter the word:"
    word=get_input(prompt)
    if is_palindrome(word):
      print "Indeed! {} is a Palindrome!".format(word)
    else:
      print "NO! {} is NOT a Palindrome!".format(word)
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
