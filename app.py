from flask import Flask, render_template, request
import collections
import soup
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    searchstring=request.form.get("search")
    # print searchstring
    if searchstring>0:
        # sampleresults=collections.OrderedDict()
        # sampleresults["Toby McGuire"]=27
        # sampleresults["Andrew Garfeild"]=19
        # sampleresults["Peter Parker"]=6
        # sampleresults["Norman Osborne"]=3
        # sampleresults["Mary Jane"]=1
        results=soup.search(searchstring)[0]
        if results == None:
            newresults = "SORRY, the string you inputted was not a who or when query. GO BACK and Try again."
            nresults = None
        elif len(results) < 5:
            newresults = results[0][0]
            nresults = results
        else:
            newresults = [results[x] for x in range(5)][0][0]
            nresults = [results[x] for x in range(5)]
        # print results
        return render_template("search.html",results=newresults,
                               searchstring=searchstring,
                               nresults = nresults)
    else:
        return render_template("index.html")

@app.route("/search",methods=["GET","POST"])
def search():
    return index()
    
if __name__=="__main__":
    app.debug=True
    app.run()
