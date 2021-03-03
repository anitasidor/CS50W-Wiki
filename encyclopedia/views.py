from django.shortcuts import render

from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Define view that you will call in urls.py later, that will show an appropriate page while going to wiki/TITLE
def wiki(request, title):
    # if request.method == "GET":

    if util.get_entry(title) == None:
        return render (request, "encyclopedia/error404.html")

    #if the user typed in the query in url
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
        })


def search(request):
    #if the user searched for a site
    if request.method == "GET":
        #access what user searched for
        search_query = request.GET.get("q")
        return render(request, "encyclopedia/entry.html", {
            "entry":util.get_entry(search_query),
            "title":search_query
        })
