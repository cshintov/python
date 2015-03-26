import sys
import ex32mutate as mu
# Returns True(Nearly equal) if word_a is an element of mutation-list of word_b 
# else False(Not Nearly equal)
def near_equal(word_a,word_b):
  if word_a in mu.mutate(word_b):
    return True
  else:
    return False
#This is the main function

def main():
  if len(sys.argv) ==3:
    args=sys.argv[1:] #command line arguments as list of strings
    word_a=args[0]
    word_b=args[1]    
  else:
    print "usage: python ex33near_equal.py word1 word2"
    sys.exit(1)  
  result=near_equal(word_a,word_b)
  if result:
    print "They are nearly equal!"
  else:
    print "They are not nearly equal!"
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
