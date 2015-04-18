'''exercise 12.3 Computes the frequency of letters in a string'''
import string as s

def filestring(filename):
  return open(filename).read()

#sorts on length (break ties in random order)
def frequency(string):
  freq = []
  length = float(len(string))
  for char in s.lowercase:
    fr = string.count(char) / length * 100
    freq.append((fr,char))
  return freq
#freq is a list of tuples (frequeny,character)

def print_freq(freq):
  for frq,char in freq:
    print char,':',frq

def repeat():
  while True:
    filename = raw_input("enter the filename:")
    string = open(filename).read()
    freq = frequency(string)
    freq.sort(reverse=True)
    print 'letter frequency : '
    print_freq(freq)
    prompt="continue? y:yes / n:no:"
    string=raw_input(prompt)
    if string=='n': 
      print "Bye!"
      break

def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
