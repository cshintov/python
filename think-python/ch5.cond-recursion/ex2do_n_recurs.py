import sys
import os

def do_n(func,func_arg,num):
  if num<=0:
    return
  print num
  func(func_arg)
  do_n(func,func_arg,num-1)
def sim_fun(string):
  print string
def main():
  print "prints the given string , number times"
  prompt="the string?:"
  string=raw_input(prompt)
  prompt="how many times?(in digits):"
  num=int(raw_input(prompt))
  
  do_n(sim_fun,string,num)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
