import google
from bs4 import BeautifulSoup
import sys
from namere import findname
from nameFinder import get_potential_names
from nameFinder import check_names
import urllib2

question = "Who is the president of the United States today?"

def search(searchtype):
    g =  google.search(question, num = 10, start = 0, stop = 10, pause=3.0)
    utils = [w for w in g]

    d = {}
    if searchtype == "Who" or searchtype == "":
        name = True
    else:
        name = False
        
    count = 0;
    for x in utils:
    #run beautiful soup to find names
        try:
            html_doc = google.get_page(x)
            soup = BeautifulSoup(html_doc)
            y = soup.get_text()
            if name:
                #names = check_names(get_potential_names(y))
                names = findname(y)
                for k in names.keys():
                    if k not in d.keys():
                        d[k] = names[k]
                    else:
                        d[k] = d[k] + names[k]
                    #find highest number of names
                    #return addition of that 
                count +=1
        except Exception, error:
            print error
            
    return d
           

print search("")



'''
Soup functions/google functions
print soup.prettify()

print soup.get_text()

g.googlesearch("Question", num = 10, start =0, stop = 10)
utils [x for x in g]
print utils


'''
