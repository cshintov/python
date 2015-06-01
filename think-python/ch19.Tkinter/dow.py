
from BeautifulSoup import BeautifulSoup
import urllib,re,os

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def get_text(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    print type(visible_texts)
    i=0
    for text in visible_texts:
        visible_texts[i] = visible_texts[i].encode('utf-8')
        i+=1
    visible_texts = ''.join(visible_texts)
    cmd = 'touch temp.txt'
    os.system(cmd)
    f = open('temp.txt','w')
    f.seek(0)
    try:
        f.write(str(visible_texts))
    except:
        pass
    f.close()
    #print visible_texts
    return visible_texts

if __name__== '__main__':
    url='www.google.com'
    get_text(url)
