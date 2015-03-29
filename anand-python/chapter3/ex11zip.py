'''
Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
'''

import sys
import os
import zipfile as zf

#Zips the given file to the specifie zipfilename
def myzip(zipname,files):

  try:
    import zlib
    compression = zf.ZIP_DEFLATED
  except:
    compression = zf.ZIP_STORED

  modes = { 
            zf.ZIP_DEFLATED: 'deflated',
            zf.ZIP_STORED:   'stored',
          }
  print modes[compression]
  zobj=zf.ZipFile(zipname,mode='w')
  for _file in files:
    try:
      zobj.write(_file,compress_type=compression)
    except:
      print "The %s file doesn't exist" % (_file)
  print zobj.printdir()
  zobj.close()  
  return

#This is the main function

def main():
  if len(sys.argv) >=3:
    args=sys.argv[1:] #zipname and list of files to zip
  else:
    print "usage: python ex11myzip.py zipfilename filelist "
    sys.exit(1)  
  zipname=args[0]
  files=args[1:]
  result=myzip(zipname,files)
  print "The files have been zipped to : ", zipname
  os.system('xdg-open '+zipname)
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
