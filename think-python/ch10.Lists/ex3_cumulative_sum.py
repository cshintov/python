'''exercise 10.3 returns a list of cumulative sums, up to that item
  for example cumulative sum list of [1,2,3] is [1,3,6]
'''

def cumulative(_list):
  result = []
  for index in range(len(_list)):
      result.append(sum(_list[:index + 1]))
  return result

        
def main():
  _list=[1,2,3,4]
  print 'the cumulative sum list: {}'.format(cumulative(_list))
  
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
