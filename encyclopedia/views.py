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

        #if search query is not in database
        if util.get_entry(search_query) == None:

            #get all the entries in db in form of a list
            all_entries = util.list_entries()

            #initiate list that you will append entries that have query as a substring
            substring_entries = []

            #check which entry has a query substring
            for entry in all_entries:
                if search_query in entry:
                    substring_entries.append(entry)

            return render(request, "encyclopedia/search.html", {
                "title":search_query,
                "substring_entries":substring_entries
            })



        return render(request, "encyclopedia/entry.html", {
            "entry":util.get_entry(search_query),
            "title":search_query
        })


#Creating new page

def newPage(request):

    #if "Create New Page" is clicked
    if request.method == "GET":
        return render(request, "encyclopedia/newPage.html")

    #if form with new entry is submitted
    if request.method == "POST":

        #if entry already existis
        if util.get_entry(request.POST.get("newTitle")) != None:
            return render (request, "encyclopedia/error404.html")