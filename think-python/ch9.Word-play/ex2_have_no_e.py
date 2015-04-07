'''exercise 9.2 Print all the words not having e in it and computes the percentage of such words
file must have one word per line
'''

def has_no_e(word):
  return not 'e' in word

def print_no_e(fin):
  choice=get_input('Do you want to print words without e in this file?:yes/no')
  count_e=0
  total=0
  for line in fin:
    total+=1
    if has_no_e(line.strip()):
      if choice == 'yes':
        print line.strip()
      count_e+=1
  return count_e,total
  
def get_input(prompt):
  _input=raw_input(prompt)
  return _input

def repeat():
  while True:
    filename=get_input('enter the filename:')
    if filename=='':
      filename='words.txt'
    fin=open(filename)
    counts=print_no_e(fin)
    percentage=float(counts[0])/counts[1]*100
    print "The percentage of words without e in file '{}' is {} :".format(filename,percentage)
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
