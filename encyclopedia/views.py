from django.shortcuts import render

from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Define view that you will call in urls.py later, that will show an appropriate page while going to wiki/TITLE
def wiki(request, title):

    if util.get_entry(title) == None:
        return render (request, "encyclopedia/error404.html")

    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
    })