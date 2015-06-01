'''exercise 5.7 Splits a file into multiple files with n lines each'''

import sys,os
#generator to read the lines of the file
def readfile(file_):
    return (line for line in open(file_))

#creates the subfile and writes the string to it
def writeto(subfile,string):
    f = open(subfile,'w')
    print 'writing to {}'.format(subfile)
    f.write(string)
    f.close()

#splits the file into multiple subfiles having num lines in each
def split(file_,num):
    lines = readfile(file_)
    i = 1
    name,ext = os.path.splitext(file_)
    print 'name:ext',name,ext
    while True:
        n = 0
        string = ''
        for line in lines:
            subfile = name+str(i)+ext
            string = ''.join((string,line))
            n += 1
            if n == num:
                writeto(subfile,string)
                break
        else:
            #writes the last chunk
            writeto(subfile,string)
            break
        i += 1

if __name__=='__main__':
    argc = len(sys.argv)
    if argc != 3: 
        print 'usage: python ex07split.py file number_of_lines'
        sys.exit(1)
    else:
        file_ = sys.argv[1]
        num = int(sys.argv[2])
        split(file_,num)

