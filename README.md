# CS50-Web
CS50’s Web Programming with Python and JavaScript

---
# Project 0 - Search

**Regular Search Page**

-   Centered
    
-   Rounded corners
    
-   The search button should also be centered and beneath the search bar.
    
-   “I’m Feeling Lucky” button, when clicked should take users directly to the first google search result for the query, bypassing the normal results page.
    

**Google Image Search Page**

-   User should be able to type in a query, click a search button, and be taken to the Google Image search results for that page.
    

**Google Advanced Search Page**

-   Find pages with… “all these words:”
    
-   Find pages with… “this exact word or phrase:”
    
-   Find pages with… “any of these words:”
    
-   Find pages with… “none of these words:”
    
-   The four options should be stacked vertically, and all of the text fields should be left aligned.
    
-   “Advanced Search” button should be blue with white text.
    
-   When “Advanced Search” button is clicked, the user should be taken to the search results page for their given query.

My presentation video on YouTube: [CS50 Web Programming | Project 0](https://youtu.be/0ALaoH5H_QY)
---
---


# PROJECT 1 - WIKI
### Technologies used
- [Django](https://docs.djangoproject.com/en/4.1/)
- [Markdown](https://pypi.org/project/Markdown/)
- [Fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [Random](https://docs.python.org/3/library/random.html)
---

## SPECIFICATIONS

1.  Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
    

- The view should get the content of the encyclopedia entry by calling the appropriate util function.
    
- If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    
- If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
    

2.  Index Page: I updated index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
    
3.  Search: Allows the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
- If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
- If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
- Clicking on any of the entry names on the search results page should take the user to that entry’s page.  

4.  New Page: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
- Users can enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
- Users are able to click a button to save their new page.
- When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
- Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.

5.  Edit Page: On each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
- The textarea is pre-populated with the existing Markdown content of the page.
- The user is able to click a button to save the changes made to the entry.
- Once the entry is saved, the user is redirected back to that entry’s page.

6.  Random Page: Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.
    
7.  Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user.

Here's my presentation video YouTube: [Project 1 - Wiki](https://youtu.be/_8RH29TpJPA)