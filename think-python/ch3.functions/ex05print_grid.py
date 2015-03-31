'''
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
2. Write a function that draws a similar grid with four rows and four columns.
'''
def do2(func):
  func()
  func()
def do4(func):
  do2(func)
  do2(func)  

def do_2(func,arg1,arg2):
  func(arg1,arg2)
  func(arg1,arg2)
def do_4(func,arg1,arg2):
  do_2(func,arg1,arg2)
  do_2(func,arg1,arg2)  

def print_line_cell(s1,s2):
  print s1,s2,
def print_line(s1='+',s2='- - - -'):
  do_2(print_line_cell,s1,s2)
  print s1

def print_row():
  print_line()
  do_4(print_line,'|','       ')
def print_grid_2():
    do2(print_row)
    print_line()

print_grid_2()
print "*"*110

def print_line_4(s1='+',s2='- - - -'):
  do_2(print_line_cell,s1,s2)
  do_2(print_line_cell,s1,s2)
  print s1
def print_row_4():
  print_line_4()
  do_4(print_line_4,'|','       ')
def print_grid_4():
  do4(print_row_4)
  print_line_4()

print_grid_4()

