import google
from bs4 import BeautifulSoup
import sys
from namere import findname

htmltester = "Lisa Zhang likes her food hot, but hates food cooked by Bob."

'''
args = sys.argv

try:
    question = str(args[1])
    num = str(args[2])
    print "yay this works"
except:
    question = "Who is the president of the United States today?"
'''

question = "Who played Spiderman?"

g =  google.search(question, num = 10, start = 0, stop = 10)
utils = [w for w in g]
print utils

d = {}
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

print d


'''
print soup.prettify()
print

print soup.get_text()


g.googlesearch("Question", num = 10, start =0, stop = 10)
utils [x for x in g]
print utils


'''
