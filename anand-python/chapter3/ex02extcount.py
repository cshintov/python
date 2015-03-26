import sys
import os

def get_ext(contents):
  ext_list=[]
  for content in contents:
    if '.' in content:
      ext_list.append(content[content.index('.')+1:])
  return ext_list

def count_ext(_dir):
  ext_dict={}
  contents=os.listdir(_dir)
  ext_list=get_ext(contents)
  for ext in ext_list:
    ext_dict[ext]=ext_dict.setdefault(ext,0)+1
  return ext_dict

def print_dict(_dict):
  for key in _dict:
    print _dict[key],' : ',key


def main():
  if len(sys.argv)==2:
    _dir=sys.argv[1]
  else:
    print "usage: python exn.py [argument list]"
    sys.exit(1)
  result=count_ext(_dir)
  print "the result:\n"
  print_dict(result)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
