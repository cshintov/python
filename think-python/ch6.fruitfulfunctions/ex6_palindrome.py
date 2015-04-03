'''
exercise:6.6 check whether a given string is palindrome or not

'''

import os

def is_palindrome(string):
  if first(string) != last(string):
    return False
  if len(middle(string)) < 2:
    return True
  if is_palindrome(middle(string)):
    return True


def first(string):
  #print 'first:',string[0]
  return string[0]

def last(string):
  #print 'last:',string[-1]
  return string[-1]

def middle(string):
  #print 'middle:',string[1:-1]
  return string[1:-1]

def get_input(prompt):
  string=raw_input(prompt)
  if string == '':
    print "please enter a string with at least one character!"
    string=get_input(prompt)
  return string
  
def main():
  prompt="enter the input string:"
  string=get_input(prompt)
  result=is_palindrome(string)
  if result:
    print "The string {0} is a Palindrome!".format(string)
  else:
    print "The string {0} is NOT a Palindrome!".format(string)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
