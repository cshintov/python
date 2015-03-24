import mylib as my
def array_2d(raw,col):
  array=[]
  for i in range(raw):      #adding raws
    column=[]
    for j in range(col):    #creating ith raw
      column.append(None)   #adding jth element in ith raw
    array.append(column)
  # array=[ array[i][j] for i in range(raw) for j in range(col) ]
  return array

def fun(var,val):
  var=val
  return var

def print_2d(array_2d):
  for i in range(len(array_2d)):
    my.print_list(array_2d[i])
    print     

  
print "\n***************\n"
a=array_2d(2,3)
print_2d(a)
print "\n***************\n"
a[0][0]=5555
print_2d(a)

print "\n-----------------\n"
a=array_2d(5,5)
print_2d(a)
print "\n-----------------\n"
a[4][4]='****'
print_2d(a)


def init(arr,val):
  raw=len(arr)
  col=len(arr[0])
  return [ [fun(arr[i][j],val) for i in range(raw)] for j in range(col) ]
  #return [ fun(arr[i][j],val)  for i in range(raw) for j in range(col) ]
  
n=init(a,'****')
#print n
print "Initialised all the elements of the matrix with ****"
print_2d(n)


