'''Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.
$ python mydoc.py os
'''
import os
import sys
import inspect

#comment ur function here
'''def mydoc(module):
  mod=__import__(module)
  help=mod.__doc__
  #print help
  item_list=dir(mod)
  #print item_list
  print "-------------------"
  print "help:", help
  print "itemlist(dir(module)):", item_list
  for item in item_list:
    item=__import__(module+'.'+item)
    if inspect.isfunction(item):
      help+=item.__doc__
    else: 
      print "Not a function! :",type(module+'.'+item)
  return help
'''
def mydoc(module):
  help="Help on module %s :\nDESCRIPTION\n" % module
  mod=__import__(module)
  help+=mod.__doc__
  help+="\nFUNCTIONS\n" 
  items=inspect.getmembers(mod)
  for item in items:
    if inspect.isbuiltin(item[1]) :  
      help+='\n'+item[0]+" : "+item[1].__doc__+'\n'
    elif inspect.isfunction(item[1]):
      try:
        help=help+'\n'+item[1].__doc__+'\n'
      except:
        print item[0]+" Doesn't have a help string!"
  return help

def help_file(module):
  help=mydoc(module)
  cmd='>'+module+'.help'
  os.system(cmd)
  fh=open(module+'.help','w')
  fh.write(help)
  print 'The help file has been created as :"'+cmd[1:]+'"'
  return cmd[1:]

#This is the main function
def main():
  if len(sys.argv) ==2:
    module=sys.argv[1] #The module to get help of
  else:
    print "usage: python ex12mydoc.py module "
    sys.exit(1)  
  help=help_file(module)
  cmd='xdg-open '+help
  os.system(cmd)
  return
      
if __name__=="__main__":
  print "**************************\n"
  main()
  print "\n**************************"
