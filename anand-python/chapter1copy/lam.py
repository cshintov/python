import funarg #contains sqr(num) and fxy(func,arg1,arg2) returns func(arg1)+func(arg2)

cube=lambda x:x**3


def main():
  #print cube(2)
  #print funarg.sqr(4)
  y=funarg.fxy(cube,2,3)
  print y
if __name__=="__main__":
  main()

