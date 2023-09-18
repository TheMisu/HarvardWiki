from django.shortcuts import render
from django.urls import reverse
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
            if util.find_substring_entry(query) != []:
                return render(request, "encyclopedia/search.html", {
                "title": "Search Result",
                "entries_substr": util.find_substring_entry(query)
                })
            else:
                err_msg = ("There are no entries related to your search. " +  
                           "Please return to the <a href=" + reverse("index") + 
                           ">home</a> page") 
                return render(request, "encyclopedia/search.html", {
                "title": "Search Result",
                "err_msg": err_msg
                })                

def create(request):
    """
    Redirects the user to the create new page if the request methos is GET.
    Otherwise tries to save the user's new entry if it does not exist already.
    If an entry with the same title exists, it redirects the user to the error page.

    :param request: The HTTP request the user makes 
    :type request: HttpRequest
    """

    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        # get the values submitted in the form
        title = request.POST.get('title')
        content = request.POST.get('mdown')

        # create the new entry if it doesn't already existc
        # if entry exists => check is None
        # else => check = 1
        check = util.create_entry(title, content)

        # converting the entry to html so that we can display it
        html_content = util.convert_md_to_html(title)

        # if the entry already exists the redirect to the error page
        if check is None:
            err_msg = ("The entry you tried to create already exists. " +  
            "Please return to the <a href=" + reverse("index") + 
            ">home</a> page or try <a href=" + reverse("create") + ">creating " +
            "another entry</a> ") 
            return render(request, "encyclopedia/error.html", {
            "title": "Error",
            "message": err_msg
        })

        # redirect to the new entry's page
        else: 
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "html_content": html_content
            })

def edit(request, title):
    """
    Takes the user to a page where they can edit the wiki entry by writing in a
    textarea.
    Saves the edited entry and redirects the user to the new page.

    :param request: The HTTP request made by the user.
    :type request: HTTP request 
    """
    if  request.method == "GET":
        md_content = util.get_entry(title)
        
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": md_content
        })
    else:
        pass