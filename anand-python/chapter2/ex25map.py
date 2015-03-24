def my_fun(item):
  return item+item
def my_map(func,seq):
  list_c=[my_fun(item) for item in seq]
  return list_c
print my_map(my_fun,['a','b','c','d'])
print map(my_fun,['a','b','c','d'])
print my_map(my_fun,[1,'b',3,'d'])
print map(my_fun,[1,'b',3,'d'])
