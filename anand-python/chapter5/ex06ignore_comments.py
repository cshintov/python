'''exercise 5.6 Count the total number of lines of code, ignoring empty lines and comments in python files in a given directory'''

import sys,os
def findfiles(dir_,dircontent):
    for item in dircontent:
        relpath = os.path.join(dir_,item)
        abspath = os.path.abspath(relpath)
        cond = os.path.isfile(abspath) and abspath.endswith('.py')
        if cond:
            yield abspath

def finddirs(dir_,dircontent):
    for item in dircontent:
        relpath = os.path.join(dir_,item)
        abspath = os.path.abspath(relpath)
        cond = os.path.isdir(abspath)
        if cond: 
            yield relpath

def readfiles(files):
    #generates all nonempty and non -#- comment lines
    return (line for f in files for line in open(f))

def iscode(line):
    if line.startswith('#') or line == '':
        return False
    return True

def linesofcode(files):
    lines = readfiles(files)
    loc = 0
    comment= False
    for line in lines:
        line = line.strip()
        #marks the beginning of the multiline comments
        if line.startswith('\'\'\''):
            comment= True
        if iscode(line) and not comment:
            loc += 1
        #marks the end of the multiline comments
        if line.endswith('\'\'\''):
            comment= False
    return loc

def count_pyth_code(dir_):
    contents = os.listdir(dir_)
    pyfiles = findfiles(dir_,contents)
    dirs = finddirs(dir_,contents)

    loc = linesofcode(pyfiles)
    for d in dirs:
        loc += count_pyth_code(d)

    return loc

def main(dir_):
    loc = count_pyth_code(dir_)
    print 'There are {} lines of code in total in the directory: {}'.format(loc,dir_)

if __name__=='__main__':
    argc = len(sys.argv)
    if argc != 2: 
        print 'usage: python ex06ignore_comments.py directory'
        sys.exit(1)
    else:
        dir_ = sys.argv[1]
        main(dir_)

