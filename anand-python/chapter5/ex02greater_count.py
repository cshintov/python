'''exercise 5.2 print all the lines having more than specified number of characters in a list of files'''

import sys,math
def readfiles(files):
    for f in files:
        for line in open(f):
            yield line.strip()

def greater(lines,ch_count):
    for line in lines:
        if len(line) > ch_count:
            yield line

def printlines(lines):
    for line in lines:
        print line

def main(filenames,ch_count):
    lines = readfiles(filenames)
    lines = greater(lines,ch_count)
    printlines(lines)

if __name__=='__main__':
    argc = len(sys.argv)
    ch_count = sys.argv[-1]
    if argc < 3 or not ch_count.isdigit():
        print 'usage: python ex02greater_count filenames count'
        sys.exit(1)
    else:
        ch_count = int(ch_count)
        filenames = []
        for n in range(1,argc-1):
            filenames.append(sys.argv[n])

    main(filenames,ch_count)

