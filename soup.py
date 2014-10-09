import google
from bs4 import BeautifulSoup
import sys
from namere import findname

question = "Who is the president of the United States today?"

g =  google.search(question, num = 10, start = 0, stop = 10, pause=3.0)
utils = [w for w in g]
print utils
d = {}
try:
    for x in utils:
    #run beautiful soup to find names
        html_doc = google.get_page(x)
        soup = BeautifulSoup(html_doc)
        y = soup.get_text()
        names = findname(y)
        for k in names.keys():
            if k not in d.keys():
                d[k] = names[k]
            else:
                d[k] = d[k] + names[k]
    #find highest number of names
    #return addition of that 
   
except urllib2.HTTPError, error:
    print error.read()

print d



'''
Soup functions/google functions
print soup.prettify()

print soup.get_text()

g.googlesearch("Question", num = 10, start =0, stop = 10)
utils [x for x in g]
print utils


'''
