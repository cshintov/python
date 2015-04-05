'''
exercise:7.4 Prompts the user to input expressions , evaluates it, prints the result, continues 
the cycle until the user enter 'done' and returns the value of the last executed expression

'''
import math

def myeval():
  value='Done Already!'
  prompt="Enter the expression:"
  string=raw_input(prompt)
  while string != 'done':
    try:
      value = eval(string)
      print value
    except NameError:
      print string
    except SyntaxError:
      print 'A statement Can not be executed by eval()!'
    prompt="Enter the expression:"
    string=raw_input(prompt)
  return value
  
def main():
  result=myeval()
  print "The Result:",result
if __name__=='__main__':
  print '*'*55,'\n'
  main()
  print '\n','*'*55
