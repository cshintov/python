import sys
import ex34wrd_frequency as frq

#Returns the list of characters in the _file
def get_words(_file):
  fh=open(_file,'r')
  char_list=''.join(fh.read().split())
  fh.close()
  return char_list
#Returns the number of lines in the _file
def get_num_lines(_file):
  fh=open(_file,'r')
  num_lines=len(fh.readlines())
  fh.close()
  return num_lines

#Calculates the determiner of C file , Python file or Text file
#Uses counts of ;,{,} divided by line number for c file
#Uses c_count+ count of =,[ divided by line number for python or text file   
def find_det(freq_dict,lin_num):
  c_det=freq_dict.get(';',0)+freq_dict.get('{',0)+freq_dict.get('}',0)
  
  det=c_det/float(lin_num)
  #print 'c determiner:',det
  if det >= 0.9: return 'C'
  
  det=c_det+freq_dict.get('=',0)+freq_dict.get('[',0)
  py_txt_det= det/float(lin_num)
  #print 'python or text determiner:',py_txt_det
  if py_txt_det >= 0.2: return 'Python'
  else: return 'Text'
  
  return 'Text'  

#Determines type of the given file C,Python or Text
def  which_file(freq_dict,_file):
  lin_num=get_num_lines(_file)
  #det is number of ;,{,} combined
  det=find_det(freq_dict,lin_num)
  if det=='C': print "The file is a C program File!"
  elif det=='Text': print "The file is a Text File!"
  else : print "The file is a Python program File!"
  return

#This is the main function

def main():
  if len(sys.argv) ==2:
    _file=sys.argv[1] #command line arguments as list of strings
  else:
    print "usage: python ex35char_frequency.py file "
    sys.exit(1)  
  freq_dict=frq.word_frequency(get_words,_file)
  #print freq_dict
  #frq.print_sort(freq_dict)
  which_file(freq_dict,_file)
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
