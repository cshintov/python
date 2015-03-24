x=2
def f(a):
  x=a*a #should work fine, local x created
  return x
y=f(3)
print x,y #should print 2,9
