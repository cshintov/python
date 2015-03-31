#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def prt(lst):
  for l in lst:
    print l,"\n"
    

def files(dr):
  fls=os.listdir(dr)
  return fls

def spfiles(dr):
  fls=files(dr)
  spfls=[]
  for f in fls:
    if re.search(r'__\w+__',f):
      spfls.append(f)
  return spfls  
def relpath(dr):
  fls=spfiles(dr)
  rel=[]
  for f in fls:
    rel.append(os.path.join(dr,f))
  return rel
def abspath(dr):
  path=relpath(dr)
  ab=[]
  for p in path:
    ab.append(os.path.abspath(p))
  return ab

def create(d):
  try:
    os.makedirs(d)
    print "creating %s directory\n"% d
    os.system("ls")
  except OSError:
    sys.stderr.write(" Directory \"%s\" already Exist! "% d)
  print "\n"
    
def copy(s,d):
  for f in s:
    shutil.copy(f,d)
  print "showing the contents of the destination directory:\n"
  cmd="ls " + d
  os.system(cmd)

def myzip(s,d):
  for f in s:
    cmd="zip -j "+d+" "+f
    os.system(cmd)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--copy dir][--zip zipfile] dir [dir ...]";
    sys.exit(1)
  
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  
  opt=''
  des = ''
  if args[0] == '--copy':
    opt='copy'
    des = args[1]
    del args[0:2]

  deszip = ''
  if args[0] == '--zip':
    opt='zip'
    deszip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  # +++your code here+++
  # Call your functions
  print "*********************\n"
  sr=args[:]
  prt(sr)
  #des=args[0]
  ab=[]
  print "these are the absolute paths of the special files:\n"
  for d in sr:
    ab.extend(abspath(d))
  prt(ab)
  if opt =='copy':    #copy
    create(des)
    copy(ab,des)
  else:               #zip
    myzip(ab,deszip)
  print "\n*********************"
if __name__ == "__main__":
  main()
