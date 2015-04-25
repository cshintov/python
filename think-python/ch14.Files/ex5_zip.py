'''
exercise 14.5 given a zipcode prints the name and population

'''
from urllib import urlopen as opn
##finds the name of the city from the html page
def name(url):
  count = 0
  for line in url:
    if line.startswith('<title>'):      
      break    
  if not 'zip' in line:
    return False
  for c in '<>/':
    line = line.replace(c,'')
  line = line.replace('title','')
  if line.startswith(','):
    return False
  line = line.replace('zip code','')
  print 'The name of the place :',line.strip()
  return True
#finds the total population from the html page
def population(url):
  for line in url:  
    if 'Total population' in line:
      break
  index = line.index('<span')
  line = line[index-15:index]
  for c in '</>dt':
    line = line.replace(c,'')
  print 'The population of the city:',line
        
#finds the city with the given zip and prints its population
def find(zipcode):
  add = 'http://www.uszip.com/zip/'+zipcode
  url = opn(add)
  if not name(url):
    print 'There is no such zipcode!'
    return
  population(url)
  url.close()
  
def repeat():
  while True:
    zipcode=raw_input('enter the zipcode:')
    if len(zipcode)!= 5: 
      print 'Enter a valid zipcode(must be of length 5)!'
      continue
    find(zipcode)
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
