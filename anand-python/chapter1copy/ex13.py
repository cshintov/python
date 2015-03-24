def istrcmp(str1,str2):
  str1=str1.upper()
  str2=str2.upper()
  if str1==str2:
    return "TRUE"
  else :
    return "FALSE"
def main():
  print istrcmp('Hai','haI')
  print istrcmp('heLLo','HEllo')
  print istrcmp('A','c')
  
if __name__=="__main__":
  main()
