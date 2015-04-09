'''exercise 9.8 Counts the number of numbers in the 6 digit odometer which satisfies the following conditions
first the last four digits should be a palindrome
one mile later last five digits should be a palindrome
one mile later middle four should be a palindrome
one mile later the entire number should be a palindrome
'''

def is_palindrome(word):
  return word[::-1] == word
  
def is_special(number):
  number_str = '{:06}'.format(number)
  #first check the last condition: whole 6 palindrome
  if not is_palindrome(number_str):
    return False
  #if yes then check middle four condition
  number-=1
  number_str='{:06}'.format(number)
  if not is_palindrome(number_str[1:5]):
    return False
  #if yes check last five condition
  number-=1
  number_str='{:06}'.format(number)
  if not is_palindrome(number_str[1:6]):
    return False
  #if yes check last four condition
  number-=1
  number_str='{:06}'.format(number)
  if not is_palindrome(number_str[2:6]):
    return False
  
  print number,'last four palindrome'
  print number+1,'last five palindrome'
  print number+2,'middle four palindrome'
  print number+3,'6 digit palindrome'
  
  return True
    
def count_numbers():
  choice=raw_input('Do you want to print the special numbers?yes/no:')
  count_special=0
  for number in range(1000000):
    include=is_special(number)
    if include:
      if choice != 'no':
        print '\nso {} is a special number!\n'.format(number-3)
      count_special+=1
  return count_special

      
def main():
  count=count_numbers()
  print "The number of words which satisfies the condition is {}.".format(count)
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
