def my_zip(list_a,list_b):
  length=len(list_a)
  list_c=[(list_a[i],list_b[j]) for i in range(length) for j in range(length) if i==j]
  return list_c
print my_zip([1,2,3],['a','b','c','d'])
