import google
from bs4 import BeautifulSoup
import sys
from namere import findname
from nameFinder import get_potential_names
from nameFinder import check_names
import urllib2
from dateFinder import find_dates
import operator


question = "Who is the president of the United States today?"
dquestion = "When was Martin Luther King Jr. born?"
#returns a dictionary with the search results
def search(question):
    g =  google.search(question, num = 10, start = 0, stop = 10, pause=3.0)
    utils = [w for w in g]
    
    d = {}
    name = False
    date = False
    searchtype = question.split(" ")[0]
    if searchtype.lower() == "who" or searchtype == "":
        name = True
    elif searchtype.lower() == "when":
        date = True

    else:
        name = False
        date = False
    count = 0
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
                    count = count + names[k]
                    if k not in d.keys():
                        d[k] = names[k]
                    else:
                        d[k] = d[k] + names[k]
                    #find highest number of names
                   # dhigh=findhigh(d);
                    #return addition of that 
            elif date:
                dates = find_dates( y )
                for k in dates.keys():
                    count = count + dates[k]
                    if k not in d.keys():
                        d[k] = dates[k]
                    else:
                        d[k] = d[k] + dates[k]
            else: 
                return


        except Exception, error:
            pass
    d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

    return [d,count]

           
#finds the highest counts in a dictionary
def findhigh(d,numb = None):
    if d == {}:
        return None
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
    return maxd


'''
x = search(question)
print x
print findhigh(x[0]) #first element is the dictionary
print x[1] #second element is the count
y = search(dquestion)
print findhigh(y[0])
print y[1]


print findhigh(search(dquestion)[0])

'''


'''
Name Results: (who testing with:
question = "Who is the president of the United States today?"
)
//nameFinder runs alot faster than namere.py//
probably b/c namere.py looks for all kinds of different names like those including middle names and stuff
1)namere.py
{u'April': 279, u'Barack Obama': 261, u'January': 461}

2)nameFinder.py
{u'Barack Obama': 263, u'Ann Dunham': 52, u'Michelle Obama': 120}
'''
