import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from markdown2 import Markdown


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.

    :param title: The title of the entry we want to save
    :type title: str
    :param content: The md content of the new entry we want to create
    :type content: str?
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def create_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it returns None in order to help with programming the view.

    :param title: The title of the entry we want to save
    :type title: str
    :param content: The md content of the new entry we want to create
    :type content: str?
    """
    file_name = f"entries/{title}.md"
    if default_storage.exists(file_name):
        return None # we will use this in the view
    else:
        default_storage.save(file_name, ContentFile(content))
        return 1 # return anything to pass the if check in the view 


def get_entry(title: str):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.

    :param title: The title of the entry we want to get.
    :type title: str
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def convert_md_to_html(title: str):
    """
    Converts a MD file to HTML

    :param title: The title of the .md file we want to convert.
    :type title: str
    """
    content = get_entry(title)
    markdowner = Markdown()
    
    # check if the file exists (content != None)
    if content == None:
        return None
    else:    
        return markdowner.convert(content)

def find_substring_entry(query: str) -> list[str]:
    """
    Returns a list of all wiki entries that have the query as a substring.

    :param query: The entry the user tried to find on the wiki
    :type query: str
    """
    result = []
    for entry in list_entries():
        if query in entry:
            result.append(entry)
    
    return result