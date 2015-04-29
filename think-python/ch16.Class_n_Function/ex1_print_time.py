'''
exercise 16.1 Prints the time in hour:minute:second format

'''

class time(object):
  '''time in the format hour:minute:second'''

def create_time():
  t = time()
  t.hr = int (raw_input('enter the hour : '))
  t.mt = int (raw_input('enter the minutes : '))
  t.sc = int (raw_input('enter the seconds : '))
  return t

def print_time(tim):
  print '\nhour:minute:seconds ==> {:02d}:{:02d}:{:02d}'.format(tim.hr,tim.mt,tim.sc) 
        
def main():
  while True:
    time_a = create_time()
    print 'The time is :'
    print_time(time_a)

    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
