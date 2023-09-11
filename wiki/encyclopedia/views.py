from django.shortcuts import render
from markdown2 import Markdown

from . import util

def convert_md_to_html(title):
    """
    Converts a MD file to HTML

    :param title: The title of the MD file we want to convert.
    :type title: String
    """
    content = util.get_entry(title)
    markdowner = Markdown()
    
    # check if the file exists (content != None)
    if content == None:
        return None
    else:    
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)

    if html_content == None:
        pass
    else:
        return render(request, "encyclopedia/entry.html")
