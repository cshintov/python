'''exercise 9.7 Counts the number of words in the file consisting of three consecutive double letters
'''
def is_double_letters(word):
  count_six=len(word)-6

  if count_six < 0:
    return False
  
  if count_six == 0:
    include = word[0]==word[1] and word[2]==word[3] and word[4]==word[5]
    return include
      
  for i in range(count_six+1):
    include=is_double_letters(word[i:i+6])
    if include : return include
  
  return False
    
def count_words(filename):
  choice=raw_input('Do you want to print all three consecutive double letter words in this file?yes/no:')
  fin=open(filename)
  count_incl=0
  for word in fin:
    include=is_double_letters(word.strip())
    if include:
      if choice == 'yes':
        print word.strip()
      count_incl+=1
  fin.close()
  return count_incl

def repeat():
  while True:
    filename=raw_input('enter the filename:')
    if filename=='':
      filename='my.txt'
    count=count_words(filename)
    print "The number of words in the file '{}' which contains three consecutive pairs {}.".format(filename,count)
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
