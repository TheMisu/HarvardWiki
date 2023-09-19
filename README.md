# HarvardWiki
My solution to CS50w's Project 1


# Understanding:
- There are some potentially useful (when writing views) functions inside of encyclopedia/urls.py, namely:
    1. list_entries: returns a list of the names of all encyclopedia entries currently saved
    2. save_entry: saves a new encyclopedia entry, given its title and some MD content.
    3. get_entry: retrieves an encyclopedia entry by its title, returning its MD contents if the entry exists or None otherwise


# Task:
1. ~~**Entry Page**:~~ Visiting /wiki/TITLE where TITLE is the title of an encyclopedia entry should render a page that displays the contents of that entry
    - The view should get the content of the encyclopedia entry by calling the appropriate util function
    - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found
    - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry

2. ~~**Index Page**:~~ Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page

3. ~~**Search**:~~ Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
    - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page
    - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
    - Clicking on any of the entry names on the search results page should take the user to that entry’s page.

4. ~~**New Page**:~~ Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
    - Users should be able to enter a title for the page and, in a _textarea_, should be able to enter the Markdown content for the page
    - Users should be able to click a button to save their new page
    - When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
    - Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

5. ~~**Edit Page**:~~ On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a _textarea_.
    - The _textarea_ should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial _value_ of the _textarea_).
    - The user should be able to click a button to save the changes made to the entry.
    - Once the entry is saved, the user should be redirected back to that entry’s page.

6. **Random Page**: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

7. ~~**Markdown to HTML Conversion**:~~ On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the _python-markdown2_ package to perform this conversion, installable via _pip3 install markdown2_.


# Hint:
- By default, when substituting a value in a Django template, Django HTML-escapes the value to avoid outputting unintended HTML. If you want to allow for an HTML string to be outputted, you can do so with the safe filter (as by adding |safe after the variable name you’re substituting).