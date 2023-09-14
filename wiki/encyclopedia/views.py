from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    """
    Renders the html content of a .md file 

    :param request: The HTTP request made by the user
    :type request: HttpRequest
    :param title: The title of the .md file we want to render
    :type title: str
    """
    html_content = util.convert_md_to_html(title)

    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "title": "Error",
            "message": "The entry you were looking for does not exist. "
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "html_content": html_content
        })

def search(request):
    """
    Searches a specific entry in the list of entries and renders it if existent

    :param request: The HTTP request the user makes in the searchbar
    :type request: HttpRequest
    """
    if request.method == "POST":
        # get the 'q' parameter from the URL or set query = '' if q doesn't exist
        query = request.POST['q']
        html_content = util.convert_md_to_html(query)
        
        # check if the query/entry exists
        if query in util.list_entries():
            # check if the page has html content
            if html_content is not None:
                return render(request, "encyclopedia/entry.html", {
                    "title": query,
                    "html_content": html_content
                })
            else:
                return render(request, "encyclopedia/error.html", {
                    "title": "Error",
                    "message": "The entry you were looking for does not exist. "
                })
        else:
            return render(request, "encyclopedia/search.html", {
            "title": "Search Result",
            "entries_substr": util.find_substring_entry(query)
        })

