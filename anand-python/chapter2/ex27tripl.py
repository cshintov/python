def triplet(num):
  trip_list=[(a,b,c) for a in range(1,num) for b in range(a,num) for c in range(b,num) if a+b==c]
  return trip_list
print triplet(5) 
