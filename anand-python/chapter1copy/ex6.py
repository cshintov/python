a, b = 2, 3
c, b = a, c + 1 # a(2) but c(?)+1 can't be evaluated since c is not defined before:error 
print a, b, c
