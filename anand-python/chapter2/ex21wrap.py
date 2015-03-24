import sys

#splits the line at width
def wrap(_file,width):
  lines=open(_file,'rU').readlines()
  result=[]
  for line in lines:
    line=line.strip()
    print line
    num=len(line)/width
    #print num
    mod=len(line)%width
    #print mod
    if len(line)<width:
      result.append(line+'\n')
    else :
      last_index=0
      print range(width,num*width+1,width)
      for split in range(width,num*width+1,width):#range(width,(len(line)/width+1),width):
        result.append(line[split-width:split].strip()+'\n')
      if mod>0:
       last_index=split
       result.append(line[last_index:].strip()+'\n')
       
  print result
  print "++++++++++++"
  for line in result:
    print line,
  print "++++++++++++"
  return

#This is the main function

def main():
  if len(sys.argv) >=3:
    args=sys.argv[1:] #command line arguments as list of strings
    _file=args[0]
    width=int(args[1])
  else:
    print "usage: python ex21wrap.py [file] [width] "
    sys.exit(1)  
  wrap(_file,width)
  
  return
  
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"

