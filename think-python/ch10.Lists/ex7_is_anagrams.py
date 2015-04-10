'''exercise 10.7 checks whether two strings are anagrams'''


def is_anagrams(word_a,word_b):
  if len(word_a) != len(word_b):
    return False
  if word_a == word_b:
    return False
  for char in word_a:
    if word_a.count(char) != word_a.count(char):
      return False
  return True
  
def repeat():
  while True:
    prompt = 'enter the first word:'
    word_a=raw_input(prompt)
    prompt = 'enter the second word:'
    word_b=raw_input(prompt)
    if is_anagrams(word_a,word_b):
      print 'They are Anagrams!'
    else:
      print 'They are NOT Anagrams!'
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
