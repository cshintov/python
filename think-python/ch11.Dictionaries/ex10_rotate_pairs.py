'''
exercise 12.10 Finds all the rotate-pairs by the given rotation length in the given file
'''
import string

def build_list(filename):
  fstring=open(filename).read()
  _list = fstring.split()
  return _list

def build_dict(filename):
  words = build_list(filename)
  for word in words:
    wdict[word] = word
  return wdict
#finds the character after rotating the given char by the rotation size
def rotate_char(char,rotation_size):
  if char.isupper():
    alphabet = string.uppercase
  else:
    alphabet = string.lowercase
  difference = alphabet.index(char) + rotation_size - 26
  if difference >= 0:
    rotated_char = alphabet[difference]
  else :
    rotated_char = alphabet[difference + 26]
  return rotated_char
#finds the word after rotating the given word by the rotation size
def rotate_word(word,rotation_size):
  word_rotated=''
  for char in word:
    word_rotated+=rotate_char(char,rotation_size)
  return word_rotated
#prints the word - rotate word pairs in the given dictionary
def rotate_pairs(wdict,size):
  ddict={}
  for item in wdict:
    rword=rotate_word(item,size)
    if rword in wdict:
      ddict[item] = rword
  #print 'dict',ddict
  for item in ddict.items():
    print item[0],'-----',item[1]
  
def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='my.txt'
    wdict=build_list(filename)
    rot_size=int(raw_input('enter the rotation size:'))
    rotate_pairs(wdict,rot_size)
    prompt="continue? y:yes / n:no:"
    choice=raw_input(prompt)
    if choice in ('n','no'): 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
