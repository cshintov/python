'''
exercise 16.7 computes ones age given ones birthday, and the number of days,hours,minutes,seconds till the next birthday 

'''
from datetime import *

class mytime(object):
  '''time in the format hour:minute:second'''

def int_to_time(seconds):
  tm = mytime()
  minutes,tm.sc = divmod(seconds,60)
  tm.hr,tm.mt = divmod(minutes,60)
  return tm

def get_birthday():
  yr = int(raw_input('year: '))
  mt = int(raw_input('month(number): '))
  dy = int(raw_input('day: '))
  d = datetime(yr,mt,dy)
  return d

#computes age
def age(bday):
  ag = datetime.today() - bday
  ag = datetime.min + ag
  ag = ag.replace(ag.year-1)
  return ag

#computes time till next birthday
def next_bday(bday):
  today = datetime.today()
  nxt = bday.replace(year=today.year)
  diff = nxt - today
  hms = int_to_time(diff.seconds)
  if diff.days >= 0:
    print '{} days {} hours {} minutes {} seconds'.format(diff.days,hms.hr,hms.mt,hms.sc)
  else :
    print '{} days {} hours {} minutes {} seconds'.format(diff.days+365,hms.hr,hms.mt,hms.sc)
    
def main():
  while True:
    a = get_birthday()
    ag = age(a).year
    print "your age is : ",ag
    print 'next birthday comes in : ',
    next_bday(a)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
