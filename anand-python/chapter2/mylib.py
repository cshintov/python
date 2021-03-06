import sys

#prints a list
def print_list(list):
  for element in list:
    print element,
  return
#prints a two dimensional array
def print_2d(array_2d):
  for i in range(len(array_2d)):
    print_list(array_2d[i])
    print 

def split(string,width):
  string=string.strip()
  if len(string) <= width:
    #print "if"
    newstring=string+'\n'
  else:
    #print "else"
    first=string[:width]
    rest=string[width:]
    newstring=first+'\n'+split(rest,width)
  return newstring

def find_word_bef(string):
  #print "In find word before"
  #print list(string)
  index=0
  #print range(-1,-len(string)-1,-1)
  for i in range(-1,-len(string),-1):
    if string[i]==' ':
      index=i
      break
  #print index
  return index

def find_word_after(string):     #find the next space and hence the word    
  #print "In find word after"
  #print list(string)
  index=len(string)
  for i in range(len(string)):
    if string[i]==' ':
      index=i
      break
  #print index
  return index

def nice_split(string,width):
  string=string.strip()
  #print len(string),":",width
  if len(string) <= width:
    #print "tail"
    if string:
      newstring=string+'\n'
    else:
      newstring=string#+'\n'
  else:
    #print "else"
    #if ' ' not in string[:width]:
    #  print "NO space in ",string[:width]
    #  newstring=string[:width]
    if string[width] == ' ':
      #print "Go on , its a word"
      first=string[:width]
      rest=string[width:]
    else :
      #print "NO! Go for the last word"
      #print string[:width]
      word=find_word_bef(string[:width])
      #print string
      #print word
      if word==0:                               #string greater than width but one long-word itself
        #print "in word=0"
        word=find_word_after(string)     #find the next space and hence the word  
        first=string[:word]
        rest=string[word:]
      else:
        first=string[:width][:word]
        rest=string[word+width:]
      #print "first:",list(first)
      #print "rest:",list(rest)      
    newstring=first+'\n'+nice_split(rest,width)
  return newstring

def strip(string,letter):
  result=""
  for char in string:
    if char != letter:
      result+=char
  return result
#returns the string center aligned to the size of width  
def center(string,width):
  string=string.strip()
  padlength=width-len(string)
  back=padlength/2
  front=padlength-back
  al_string=' '*front+string+' '*back+'\n'
  return al_string
#This is the main function

def main():
  if len(sys.argv) == 4:
    args=sys.argv[1:] #command line arguments as list of strings
    string=args[1]
    option=args[0]
    if option == "--split":
      width=int(args[2])
      result=split(string,width)
      print "\nThe result : ",'\n', result
      print list(result)
    if option == "--nicesplit":
      width=int(args[2])
      result=nice_split(string,width)
      print "\nThe result : ",'\n', result
      print list(result)
    if option == "--strip":
      letter=args[2]
      result=strip(string,letter)
      print "\nThe result : ",'\n', result       
    if option == "--center":
      width=int(args[2])
      result=center(string,width)
      print "\nThe result : ",'\n', result
      print list(result)
  else:
    print "usage: python mylib.py --[split/strip/niceslip] [string] [width/letter] "
    sys.exit(1)  
  return
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
  
  

