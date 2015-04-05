'''
exercise:7.1 print the given string n times

'''

def print_n(string,num):
  while num > 0:
    print string
    num-=1

def get_input(prompt):
  num=raw_input(prompt)
  return num
  
def main():
  prompt="enter the string:"
  string=get_input(prompt)
  prompt="enter the number of times string should be printed:"
  num=int(get_input(prompt))
  print_n(string,num)

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
