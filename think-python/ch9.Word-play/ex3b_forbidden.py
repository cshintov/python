'''exercise 9.3b Find a combination of 5 letters that excludes the smallest number of words
file must have one word per line
'''
import string
import sys

#returns true if the word doesn't have the given character else false
def has_no_char(char,word):
  return not char in word

#returns the percentage of included words(words not having the specified character in them)
def count_included(char,filename):
  fin=open(filename)
  count_incl=0.0
  total=0
  for word in fin:
    total+=1
    if has_no_char(char,word.strip()):
      count_incl+=1
  fin.close()
  return (count_incl/total)*100  

#returns the the character in current string which includes minimum number of words along with that number
def min_included(current,filename):
  min_count=100.0
  for char in current:
    count=count_included(char,filename)
    if count < min_count :
      min_count=count
      min_letter=char
  if min_count == 100.0: 
    return 'stop',0
  return min_letter,min_count

#finds the 5 character string combination which includes maximum number of words or excludes smallest number of words      
def find_comb(filename):
  alphabet=string.lowercase
  current='abcde'
  min_letter,min_count=min_included(current,filename)
  if min_included(current,filename)[0] == 'stop':
        print "The required combination is '{}' ".format(current)
        sys.exit(1)
  print current
  for char in alphabet[5:]:
    count=count_included(char,filename)
    if count > min_count:
      current=current.replace(min_letter,char)
      print current
      if min_included(current,filename)[0] == 'stop':
        print "The required combination is '{}' ".format(current)
        sys.exit(1)
      min_letter,min_count=min_included(current,filename)
  return current
  
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='my.txt'
    combination=find_comb(filename)
    print "The required combination is '{}'".format(combination)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string=='no': 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
