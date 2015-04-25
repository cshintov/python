'''
exercise 14.1 walks a directory printing all the files in it and subdirectories

'''
import os

def oswalk(dirname):
  for curnt,dir_list,file_list in os.walk(dirname):
    for file in file_list:
      print '{}'.format(file)
    
def walk(dirname):
  content=os.listdir(dirname)
  for item in content:
    path = os.path.join(dirname,item)
    if os.path.isdir(path):
      walk(path)
    else:
      print item
 
def repeat():
  while True:
    dirname=raw_input('enter the dirname:')
    if dirname=='':
      dirname='.'
    print 'files in this directory tree'
    walk(dirname)
    print 'now the os walk'
    oswalk(dirname)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
