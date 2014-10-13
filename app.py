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
        results=soup.findhigh(soup.search(searchstring)[0])
        # print results
        return render_template("search.html",results=results,
                               searchstring=searchstring)
    else:
        return render_template("index.html")

@app.route("/search",methods=["GET","POST"])
def search():
    return index()
    
if __name__=="__main__":
    app.debug=True
    app.run()
