'''exercise 9.2 Print all the words not having the specified character in it and computes the percentage of such words
file must have one word per line
'''

def has_no_char(char,word):
  return not char in word

def print_no_char(char,fin):
  choice=get_input('Do you want to print words without {} in this file?:yes/no'.format(char))
  count_incl=0
  total=0
  for line in fin:
    total+=1
    if has_no_char(char,line.strip()):
      if choice == 'yes':
        print line.strip()
      count_incl+=1
  return count_incl,total
  
def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    filename=get_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    char=get_input('enter the character to exclude:')
    fin=open(filename)
    counts=print_no_char(char,fin)
    percentage=float(counts[0])/counts[1]*100
    print "The percentage of words without {} in file '{}' is {} :".format(char,filename,percentage)
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
