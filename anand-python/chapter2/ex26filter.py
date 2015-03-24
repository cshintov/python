def even(item):
  return item%2 == 0
def my_filter(func,seq):
  list_c=[item for item in seq if even(item)]
  return list_c
print my_filter(even,range(1,10))  
print filter(even,range(1,10))
