'''exercise 9.9 Palindrome ages (most probably under 100)
'''

def is_palindrome(agecomb):
  return agecomb[::-1] == agecomb
  
def special(agecomb):
  
  age_str = str(agecomb).zfill(4)
  if not is_palindrome(age_str):
      return False
  #since it is a palindrome it is a candidate to be our answer
  cand=agecomb
  count = 0
  
  while cand < 10000:
    age_str = str(cand).zfill(4)
    if is_palindrome(age_str):
      son_age=int(age_str)/100
      mom_age=int(age_str)%100
      if mom_age - son_age > 10:
        #counting the number of times the age combination is palindrome (should be 8 to be the answer)
        count += 1
        if count == 6: 
          answer = son_age
    cand += 101
  
  if count == 8: 
    return answer


def current_age():
  #son's and mom's age are combined into one number and checked for the specialness
  # as any number before 0110 is trivially excluded loop starts from 110
  #It is the first possible starting point son 01 years and mom 10 years(although very rare)
  for age in range(110,10000):
    answer=special(age)
    if answer:
      return answer

      
def main():
  answer=current_age()
  print "The son's current age is {}.".format(answer)

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
