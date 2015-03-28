import sys
import re
#validates the phone numbers
def validate(phonenum):
  phonenum=re.sub(r'[ /\\()\s.-]','',phonenum)
  valid=re.match(r'^\d{10}$|^\+?91\d{10}$',phonenum)
  if valid:
    return True
  else:
    return False



#This is the main function

def main():
  if len(sys.argv) >=2:
    phonenum=sys.argv[1] #phonenumber given through the command line argument
  else:
    print "usage: python module.py [numlist] "
    sys.exit(1)  
  if validate(phonenum):
    print "This phone number is a valid phone number!"
  else: 
    print "This phone number is *NOT* a valid phone number!"
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
