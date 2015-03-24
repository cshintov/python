def count_digit(num):
  strnum=str(num)
  return len(strnum)

def main():
  print "length of 123:", count_digit(123)
  print "length of 12345:", count_digit(12345)
  print "length of '12345':", count_digit('12345')
if __name__=="__main__":
  main()
