'''exercise 10.1 nested sum to calculate the sum of all the elements in a nested list
'''

def nested_sum(lists):
  nest_sum = 0
  for item in lists:
    if type(item) == list:
      nest_sum += sum(item)
    else:
      nest_sum += item
  return nest_sum

      
def main():
  list1=[[1,2,3],[4,5],[6,7,8],[9],10]
  print 'sum of the nested list: {}'.format(nested_sum(list1))
  
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
