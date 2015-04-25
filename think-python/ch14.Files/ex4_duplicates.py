'''
exercise 14.2 Finds the duplicate files in a directory and subdirectories based on their md5 checksum 

'''
import os

def walk(dirname,ext,files):
  content=os.listdir(dirname)
  for item in content:
    path = os.path.join(dirname,item)
    if os.path.isdir(path) :
      files = walk(path,ext,files)
    else:
      flname,typ = os.path.splitext(path)
      if typ == '.'+ext:
        fl = flname +'.'+ext
        files.append(fl)
  return files

def checksum(file_lst):
  mdlst = {}
  cmd = 'md5sum '
  for fl in file_lst:
    fp = os.popen(cmd+fl) 
    out = fp.read().split()[0]
    mdlst[fl] = out
  fp.close()
  return mdlst

def duplicates(chlist):
  values = chlist.values()
  dup={}
  for key,val in chlist.items():
    dup.setdefault(val,[]).append(key)
  return (dup)

def print_d(d):
  for key,val in d.items():
    if len(val)>=2:
      print val
      
def repeat():
  while True:
    dirname=raw_input('enter the dirname:')
    ext=raw_input('enter the extension:')
    print 'files in this directory tree whith the extension {}'.format(ext)
    files = walk(dirname,ext,[])
    ch = checksum(files)
    print 'These files are the duplicates in this directory!'
    dup = duplicates(ch)
    print_d(dup)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
def main():
  print globals
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
