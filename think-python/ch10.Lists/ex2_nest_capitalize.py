'''exercise 10.2 Capitalize all strings in a nested list
'''

def capitalize_all(_list):
  result=[]
  for item in _list:
    result.append(item.capitalize())
  return result
  
def nested_capitalize(lists):
  result = []
  for item in lists:
    if type(item) == list:
      result.append(capitalize_all(item))
    else:
      result.append(item.capitalize())
  return result

      
def main():
  _list=[['ab','dD','kk'],['abcd','klmN'],['fn'],'shinto']
  print 'sum of the nested list: {}'.format(nested_capitalize(_list))
  
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
