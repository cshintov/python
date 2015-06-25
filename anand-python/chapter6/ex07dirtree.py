'''exercise 6.7 prints the directory tree recursively'''
import sys,os

#gets the absoulute path of directory/item
def abspath(directory,item=""):
    relpath = os.path.join(directory,item)
    abpath = os.path.abspath(relpath)
    return abpath

#lists the directory tree of the given directory
def dirtree(directory,item = "",depth = 0):
    print os.path.basename(directory)+'/'
    path = abspath(directory,item)
    contents = os.listdir(path)
    last = contents[-1]
    pref = '|-- '
    endpref = '\-- '
    for item in contents:
        absitem = abspath(directory,item)
        if item == last: use = endpref
        else : use = pref
        if os.path.isdir(absitem):
            st = '|   '*depth + use
            sys.stdout.write(st)
            dirtree(absitem,depth=depth+1)
        else:
            lst = '|   '*depth + use + item
            print lst

if __name__ == '__main__':
    if len(sys.argv)!= 2:
        print 'usage: python ex07dirtree.py directory'
        sys.exit(1)
    directory = sys.argv[1]
    dirtree(directory)
