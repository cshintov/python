'''
exercise 16.7  Find the n_day of two persons (the day in which one is n times older than the other) 
               
'''
from ex7_birthday import *

def younger(bda,bdb):
  
  if bda < bdb:
    return bdb

  return bda

def n_day(bda,bdb,n):
  s = younger(bda,bdb)
  old = abs(bda - bdb)
  old = old.days
  if old % (n-1)!=0: return False
  young = 0
  while True:
    if n*young == old:
      inc = timedelta(days=young)
      break
    young += 1
    old += 1
  return s + inc

def main():
  
  while True:
    print "enter the first person's birthday :"
    bda = get_birthday()
    print "enter the second person's birthday :"
    bdb = get_birthday()
    print 'I can compute the day on which one is n times older than the other!'
    n = int(raw_input('enter n :'))
    dd = n_day(bda,bdb,n)
    if dd:
      print 'Their {}_day is :'.format(n),
      try:
        print dd.strftime('%Y %B %d')
      except:  
        print dd
    else:
      print 'There is no {}_day for the given persons!'.format(n)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
