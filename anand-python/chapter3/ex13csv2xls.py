'''
Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
'''


import sys
#Needs to install third-party package tablib which handles excel and csv files
import tablib as tb 
#Creats an xls file with the content of the csv file
def csvtoxls(csv,xls):
  try:
    with open(csv,'rb') as csvh:
      data=tb.Dataset()
      data.csv=csvh.read()
    with open(xls,'wb') as xlsh:
      xlsh.write(data.xls)    
  except:
      return False
  return True

#This is the main function

def main():
  if len(sys.argv) ==3:
    csv=sys.argv[1] #csv input
    xls=sys.argv[2] #xls name to be created
  else:
    print "usage: python ex13csv2xls.py csvfile xlsfile "
    sys.exit(1)  
  if csvtoxls(csv,xls):
    print "The xls file '{0}' has been successfully created from the csv file '{1}'! ".format(xls,csv)
  else:
    print "The csv file '{0}' Does not Exist!!!!".format(csv)
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"

