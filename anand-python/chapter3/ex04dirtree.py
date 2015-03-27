import sys
import os


def list_dir(_dir):
  contents=os.listdir(_dir)
  return contents

def get_tree(_dir,depth=0):
  dir_tree={}
  list_content=[]
  for content in list_dir(_dir):
    rel_path=os.path.join(_dir,content)
    abs_path=os.path.abspath(rel_path)
    if os.path.isfile(abs_path):
      list_content.append(content)
    else:
      list_content.append(get_tree(abs_path,depth+1))
  dir_tree[_dir]=(list_content,depth)
  
  return dir_tree

def count_ext(_dir):
  ext_dict={}
  contents=os.listdir(_dir)
  ext_list=get_ext(contents)
  for ext in ext_list:
    ext_dict[ext]=ext_dict.setdefault(ext,0)+1
  return ext_dict


def print_list(_content_list,depth):
  _content_list.sort()
  for content in _content_list:
    print "|   "*depth+"|--",
    if type(content)== str :
      print content
    else:
      print_tree(content)
  
  return

def print_tree(_dict):
  _dir=_dict.keys() #a list with one key: the directory
  _dir_base=os.path.basename(_dir[0])
  _dir_path=_dir[0]
  tup=_dict[_dir_path]
  print _dir_base,' :\n',
  print_list(tup[0],tup[1])
  return 
#This is the main function

def main():
  if len(sys.argv) ==2:
    _dir=sys.argv[1] #command line argument the input directory 
  else:
    print "usage: python ex04dirtree.py directory "
    sys.exit(1)  
  if os.path.exists(_dir):
    dir_tree=get_tree(_dir)
  else:
    print "This directory does not exist! "
    print "\n**************************"
    sys.exit(1)  
  print "The Directory Tree : \n",
  print_tree(dir_tree) 
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
