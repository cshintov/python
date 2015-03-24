
def sqr(num):
  return num*num
def fxy(f,x,y):
  return f(x)+f(y)

def main():
  print 
  print "square of 2 is ",sqr(2)
  f=sqr
  print "square of 3 is ",f(3)
  print fxy(sqr,2,3)
  print fxy(f,3,4)
  print 
if __name__=="__main__":
  main()

