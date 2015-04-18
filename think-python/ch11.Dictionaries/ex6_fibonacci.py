'''

ex 11.6 Compare fibonacci standard recursive algorithm with fibonacci using memoized dictionary

'''
import time
def fib_std(num):
  if num < 2:
    return num
  fib = fib_std(num-1) + fib_std(num-2)
  return fib
known = {0:0,1:1}
def fib_memo(num):
  if num in known:
    return known[num]
  else:
    fib = fib_memo(num-1) + fib_memo(num-2)
    known[num]=fib
  return fib
  
def repeat():
  while True:
    num=raw_input('Enter the num:')
    start=time.clock()
    fib=fib_std(int(num))
    end=time.clock()
    print 'fibonacci of {}:\n{}'.format(num,fib)
    print 'standard algorithm took {} seconds'.format((end-start)*1000)
    print
    start=time.clock()
    fib=fib_memo(int(num))
    end=time.clock()
    print 'fibonacci of {}:\n{}'.format(num,fib)
    print 'memoized algorithm took {} seconds'.format((end-start)*1000)
    print

    choice=raw_input('Continue? y:yes / n:no :')
    if choice in ('n','no'):
      print 'Bye!'
      break
      
def main():
  print (1000*1000)**2
  repeat()

if __name__=='__main__':
  print '*'*50
  main()
  print '*'*50  
