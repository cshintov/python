import sys
import mylib as my
#comments are removed in this function

'''lines_wo_comment=[]
  for line in lines:
    if marker in line:
      index=0
      for i in range(len(line)):
        if line[i]==marker:
          index=i
          break
      if index==0:
        break
      
      line=line[:index]
    lines_wo_comment.append(line)  
'''

def str_com(line,marker):
  line=line.strip() #removes the leading and trailing whitespaces
  for i in range(len(line)):
    if line[i] == marker:
      if i!=0:
        line=line[:i]
        break
      return None
  line=line+'\n'  
  return line

def strip_comment(lines,marker='#'):
  print lines
  print marker
  lines_wo_comment=[]
  for line in lines:
    if str_com(line,marker):
      lines_wo_comment.append(str_com(line,marker))
    else:
      print "Its a Comment LIne!"
  return lines_wo_comment

def parse_gen(_file,marker,delim=','):                  #All default arg should be at the end
  fh=open(_file,'r')
  file_lines=strip_comment(fh.readlines(),marker)
  print file_lines
  #new_string=my.strip(file_string,delim)
  list_pars=[]
  for line in file_lines:
    list_pars.append(line.strip().split(delim))
  fh.close()
  return list_pars

#This is the main function

def main():
  if len(sys.argv) ==4:
    args=sys.argv[1:] #command line arguments as list of strings
    _file=args[0]
    delim=args[1]
    marker=args[2]
  else:
    print "usage: python ex31parse_gen.py [file] [delimiter] \[comment_marker]"
    print "Try using escape character \ before comment_marker!"
    sys.exit(1)  
  result=parse_gen(_file,marker,delim)
  print "The result : \n"
  print result
  my.print_2d(result)
  
if __name__=="__main__":
  print "*************here*************\n"
  main()
  print "\n**************************"
