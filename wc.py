#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
#returns sorted list of (word,count) tuples

def sortlist(di):
  #print "\n\n printing the dict\n"
  #print di
  dictlst = di.items()
  #print "\n\n printing the list\n"
  #print dictlst
  dictlst.sort()
  #print "\n\n printing the sorted list\n"
  #print dictlst
  return dictlst
  
def srtdlst(fname):
  fhandle=open(fname,'rU')
  filestring = fhandle.read().lower()
  #print filestring
  wordlist = filestring.split()
  wordlist = sorted(wordlist)
  #print wordlist
  
  dictf = {}
  
  for w in wordlist:
    cnt=0
    # To avoid repeated counting of a word
    if w in dictf: continue 
    
    for wrd in wordlist:
      if w == wrd :
        cnt += 1
    dictf[w] = cnt
  print '\n'
  #print dictf  
  return sortlist(dictf)
  """
  dictf = dictf.items()
  print sorted(dictf)
  return dictf
      
  print "\n\n printing the dict\n"
  print dictf
  dictflst = dictf.items()
  print "\n\n printing the list\n"
  print dictflst
  dictflst.sort()
  print "\n\n printing the sorted list\n"
  print dictflst
  return dictflst
  """  
###
def getkey(tup):
  return tup[1]

def myprint(lst,flag):
  if flag=="count":
    print "\n The Answer \n"
    #print lst
    for tup in lst:
      #print "(%s %d) " % (tup[0],tup[1]),      #to print without the newline and hence the whole result for large files
      print "\n %s   %d" % tup
  if flag=="topcount":
    print "\n The Answer Topcount \n"
    lst.sort(key = getkey, reverse = True)
    if len(lst) > 20:
      del lst[20:]
    for tup in lst:
      print "\n %s   %d" % tup
    #print lst
    
###
def print_words(fname):
  flag = "count"
  print '  printing words!  '
  lst=srtdlst(fname)
  myprint(lst,flag)
###  
def print_top(fname):
  flag = "topcount"
  print '  printing topwords!  '
  lst=srtdlst(fname)
  myprint(lst,flag)
###    
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  print filename
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
