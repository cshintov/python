'''
exercise 14.2 implements sed , replacing all the occurrences of a string with another string in a file 
write that string to another file

'''
import os,sys

def read(file_a):
  try:
    text = open(file_a).read()
    return text
  except IOError,e:
    print 'Read Error!!!!'
    print e
    sys.exit(1)
  
def write(file_b,text):
  try:
    fout = open(file_b,'w')
    fout.write(text)
    fout.close()
  except IOError,e:
    print 'Write Error!!!!'
    print e
    sys.exit(1)
  return 0    

def sed(string,replace,file_a,file_b):
  text = read(file_a)
  text = text.replace(string,replace)    
  write(file_b,text)
  os.system('cat {}'.format(file_b))
  
def main():
  if len(sys.argv) != 5: 
    print 'usage: python ex2_sed.py string replacement sourcefile targetfile'
    return
  sed(*sys.argv[1:])

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
