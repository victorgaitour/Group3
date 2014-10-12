import google
from bs4 import BeautifulSoup
import sys
from namere import findname
from nameFinder import get_potential_names
from nameFinder import check_names
import urllib2

question = "Who is the president of the United States today?"

#returns a dictionary with the search results
def search(question):
    g =  google.search(question, num = 10, start = 0, stop = 10, pause=3.0)
    utils = [w for w in g]

    d = {}
    searchtype = question.split(" ")[0]
    if searchtype == "Who" or searchtype == "":
        name = True
    else:
        name = False
        
    for x in utils:
    #run beautiful soup to find names
        try:
            html_doc = google.get_page(x)
            soup = BeautifulSoup(html_doc)
            y = soup.get_text()

            if name:
                names = check_names(get_potential_names(y))
                #names = findname(y)
                for k in names.keys():
                    if k not in d.keys():
                        d[k] = names[k]
                    else:
                        d[k] = d[k] + names[k]
                    #find highest number of names
                   # dhigh=findhigh(d);
                    #return addition of that 
            else: #when regex
                #do when regex here



        except Exception, error:
            print error
            
    return d
           
def findhigh(d,numb = None):
    print "Finding highest results"
    if numb == None:
        n = 3
    else:
        n = numb
    maxd = {}
    maxn=[]
    
    for x in d:
        if len(maxd)<n:
            maxd[x] = d[x]
            maxn.append(d[x])
            maxn.sort()
        else:
            if d[x] > maxn[0]:
                for y in maxd:
                    if maxd[y] == maxn[0]:
                        del maxd[y]
                        break
                maxd[x] = d[x]
                maxn[0] =d[x]
                maxn.sort()
    print maxn
    return maxd
                


print findhigh(search(question))



'''
Soup functions/google functions
print soup.prettify()

print soup.get_text()

g.googlesearch("Question", num = 10, start =0, stop = 10)
utils [x for x in g]
print utils

Results: (who testing with:
question = "Who is the president of the United States today?"
)
//nameFinder runs alot faster than namere.py//
probably b/c namere.py looks for all kinds of different names like those including middle names and stuff
1)namere.py
{u'April': 279, u'Barack Obama': 261, u'January': 461}

2)nameFinder.py
{u'Barack Obama': 263, u'Ann Dunham': 52, u'Michelle Obama': 120}



'''
