import sys

#Opens the input file , converts the content to single string
def file_to_string(in_file):
  fhandle=open(in_file,'r')
  file_string=fhandle.read()
  fhandle.close()
  return file_string

def new_file_string(string,file_string):
  new_string=file_string+string+"\n"
  return new_string
  
def write_to_file(newcontent,oldfile):
  fhandle=open(oldfile,'w')
  fhandle.write(newcontent)
  fhandle.close
  return

def insert(string,in_file):
  f_string=file_to_string(in_file)
  new_string=new_file_string(string,f_string)
  write_to_file(new_string,in_file)
  #print new_string
  return 

#This is the main function

def main():
  print "**************************\n"
  args=sys.argv[1:]
  if len(args) >=2:
    ins_string_file=args[0] #the string to be inserted
    input_file=args[1] #the file to be inserted into
  else:
    print "usage: python insert.py --[string/file] string/file [file] "
    sys.exit(1)  
  print ins_string_file
  print input_file
  insert(ins_string,input_file)
  print "The line has been inserted successfully!  " 
  print "\n**************************"
if __name__=="__main__":
  main()
