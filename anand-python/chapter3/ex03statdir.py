'''posix.stat_result(st_mode=16893, st_ino=171882, st_dev=2056L, st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime=1427359536, st_mtime=1427359558, st_ctime=1427359558)
'''

import time
import sys
import os

def get_stat(_file):
  stat_list=[]
  stat_list.append(int(os.stat(_file).st_size))
  epoch_time=os.stat(_file).st_mtime
  time_struct=time.gmtime(epoch_time)
  human_time=time.strftime("%m/%d/%Y %H:%M:%S",time_struct)
  stat_list.append(human_time)
  return stat_list


def dir_stat(_dir):
  stat_dict={}
  _files=os.listdir(_dir)
  for _file in _files:
    stat_dict[_file]=get_stat(_dir+'/'+_file)
  return stat_dict

def print_dict(stat_dict):
  for _file in stat_dict:
    print "%25s : %10d B : %25s" % (_file,stat_dict[_file][0],stat_dict[_file][1])


def main():
  if len(sys.argv)==2:
    _dir=sys.argv[1]
    
  else:
    print "usage: python ex03statdir.py directory"
    sys.exit(1)
  print "the result:\n"
  print_dict(dir_stat(_dir))
  #pd(dir_stat(_dir))
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
