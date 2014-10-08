import google
from bs4 import BeautifulSoup
import sys

args = sys.argv

try:
    question = str(args[1])
    num = str(args[2])
    print "yay this works"
except:
    question = "Who is the president of the United States?"


g =  google.search(question, num = 10, start = 0, stop = 10)
utils = [x for x in g]
for x in utils:
    #run beautiful soup to find names
    #find highest number of names
    #return addition of that 
    pass
html_doc = "<html> <h1>Tester</h1> </html>"
soup = BeautifulSoup(html_doc)
print soup.prettify()
print

print soup.get_text()

'''

g.googlesearch("Question", num = 10, start =0, stop = 10)
utils [x for x in g]
print utils


'''
