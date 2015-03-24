def my_zip(list_a,list_b):
  length=len(list_a)
  list_c=[(list_b[j],list_a[i]) for i in range(length) for j in range(length) if i==j]
  return list_c

def enumer(seq):
  return my_zip( seq, range( len(seq) ) )

for index,value in enumer(['a','b','c']) :
  print index, ":", value
