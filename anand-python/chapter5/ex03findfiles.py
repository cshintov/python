'''exercise 5.3 print all the files in a directory tree'''

import sys,os
def findfiles(dir_,dircontent):
    for item in dircontent:
        relpath = os.path.join(dir_,item)
        abspath = os.path.abspath(relpath)
        cond = os.path.isfile(abspath)
        if cond:
            yield abspath

def finddirs(dir_,dircontent):
    for item in dircontent:
        relpath = os.path.join(dir_,item)
        abspath = os.path.abspath(relpath)
        cond = os.path.isdir(abspath)
        if cond: 
            yield relpath

def filter_files(dir_):
    contents = os.listdir(dir_)
    files = findfiles(dir_,contents)
    dirs = finddirs(dir_,contents)

    for f in files:
        print f
    for d in dirs:
        filter_files(d)

def main(dir_):
    filter_files(dir_)

if __name__=='__main__':
    argc = len(sys.argv)
    if argc != 2: 
        print 'usage: python ex03findfiles.py directory'
        sys.exit(1)
    else:
        dir_ = sys.argv[1]
        main(dir_)

