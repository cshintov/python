#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"

second puzzle
10.254.254.74 - - [06/Aug/2007:00:12:19 -0700] "GET /edu/languages/google-python-class/images/puzzle/p-bfhj-badc.jpg HTTP/1.0" 200 18124 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"

10.254.254.29 - - [06/Aug/2007:00:06:01 -0700] "GET /edu/languages/google-python-class/images/puzzle/p-bjhh-bbdh.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def prt(lst):
  for s in lst:
    print s

def myfn(s):
  print s[-8:-4]
  return s[-8:-4]
  
def jpg(ll,host):
  print host
  result=[]
  for l in ll:
    match=re.search(r'/[\w/.-]+jpg',l)
    if match:
      f="http://"+host+match.group()
      if f not in result:
        result.append(f)
  result=sorted(result,key=myfn)
  return result

def read_urls(logf):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  ufile=urllib.urlopen(logf)
  hostn=re.search(r'_(.*)',logf)
  #"hostname:",hostn.group(1)
  host=hostn.group(1)
  lns=ufile.readlines()
  jpgl=jpg(lns,host)
  return jpgl

def create(d):
  try:
    os.makedirs(d)
    print "creating %s directory\n"% d
    os.system("ls")
  except OSError:
    sys.stderr.write(" Directory \"%s\" already Exist! "% d)
  print "\n"  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  create(dest_dir)
  cmd=">"+dest_dir+"/index.html"
  os.system(cmd)
  fl=cmd[1:]
  print "Opening the file:"+fl
  f=open(fl,'w')
  content="<html><body>"
  #sys.exit(0)
  i=0
  for url in img_urls:
    
    name="img%d"%i
    content+="<img src=%s>"%name
    name=dest_dir+"/"+name
    try :
      print "Retrieving ... file:"+url+"\n"  
      urllib.urlretrieve(url,name)
    except IOError:
      print "Trying to retrieve ... file:"+url+"\n"
      
    i+=1
  content+="</body></html>"
  f.write(content)
  f.close()
  
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])  #args[0]=logfile

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
