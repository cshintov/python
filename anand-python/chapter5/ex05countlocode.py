'''exercise 5.5 Count the total number of lines of code in python files in a given directory'''

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

def linesofcode(file_):
    loc = 0
    for line in open(file_):
       if line != '\n':
        loc += 1
    return loc

def count_pyth_code(dir_):
    contents = os.listdir(dir_)
    files = findfiles(dir_,contents)
    dirs = finddirs(dir_,contents)
    loc = 0
    for f in files:
        if f.endswith('.py'):
            loc += linesofcode(f)
    for d in dirs:
        loc += count_pyth_code(d)

    return loc

def main(dir_):
    loc = count_pyth_code(dir_)
    print 'There are {} lines of code in total in the directory: {}'.format(loc,dir_)

if __name__=='__main__':
    argc = len(sys.argv)
    if argc != 2: 
        print 'usage: python ex05countlocode.py directory'
        sys.exit(1)
    else:
        dir_ = sys.argv[1]
        main(dir_)

