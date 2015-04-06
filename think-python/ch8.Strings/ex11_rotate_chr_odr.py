'''exercise 8.11 rotates a word by the given number
a rotated by 3 is d
z rotated by 1 a
az rotated by 1 is ba

Implementation using chr and odr builtin functions
'''

import string

def rotate_char(char,rotation_size):
  if char.isupper():
    begin = ord('A')
    end = ord('Z')
  else:
    begin = ord('a')
    print begin
    end = ord('z')
    print end
  
  difference = ord(char) + rotation_size
  if difference > end:
    rotated_char = chr(difference - 26)
  elif difference < begin:
    rotated_char = chr(difference + 26)
  else:
    rotated_char = chr(difference)
  return rotated_char

def rotate_word(word,rotation_size):
  word_rotated=''
  for char in word:
    word_rotated+=rotate_char(char,rotation_size)
  return word_rotated

def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    prompt="Enter the word:"
    word=get_input(prompt)
    prompt="Enter the rotation size:"
    rotation_size=int(get_input(prompt))%26
    rotated_word=rotate_word(word,rotation_size)
    print "The rotated word is '{}'".format(rotated_word)
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
