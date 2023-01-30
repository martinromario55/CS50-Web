from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .util import *
from . import util
from fuzzywuzzy import fuzz
from django import forms
from django.contrib import messages
import os
import random


# Get matching results
# The query and list_entries are lowercased to remove case sensitivity
def get_match(query, choices, limit=1, threshold=50):
    results = [(choice, fuzz.ratio(choice.lower(), query.lower())) for choice in choices]
    results = sorted(results, key=lambda x: x[1], reverse=True)
    return [choice for choice, ratio in results if ratio >= threshold]


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request, title):
    # entries = markdown.markdown(get_entry(title))
    entries = get_entry(title)
    
    return render(request, "encyclopedia/entries.html", {"entries": entries, "title":title})


def search(request):
    query = request.GET.get('q', '')
    result = None
    # print(query) 
    if query:
        # print(query)
        result = get_entry(query)
        if result is None:
            # Get all available entries and see if there is any matching substring with the query
            matches = get_match(query, list_entries())
            # print(matches)
            return render(request, "encyclopedia/entries.html", {"entries":result, "matches":matches, "query":query})
    
        return render(request, "encyclopedia/entries.html", {"entries":result})


# Create Form for new page
class NewPageForm(forms.Form):
    title = forms.CharField(label="Page Title", min_length=1)
    page_details = forms.CharField(widget=forms.Textarea, min_length=10)

    title.widget.attrs.update({'class': 'form-control mt-3 mb-3 w-75'})
    page_details.widget.attrs.update({'class': 'form-control w-75'})

def create_new_page(request):
    # Check if method is POST
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewPageForm(request.POST)

        # Check if form data is from the cleaned version of the form data
        if form.is_valid():
            # isolate the data
            title = form.cleaned_data["title"]
            page_details = form.cleaned_data["page_details"]

            # Error if file already exists
            # directory = 'entries'
            # file_name = f'{title}.md'
            # file_path = os.path.join(os.getcwd(), directory, file_name)
            if os.path.exists(f'./entries/{title}.md'):
                messages.error(request, 'File with the same name already exists.')

                return render(request, "encyclopedia/create.html", {"form": form})

            # Create a markdown file
            with open(f'./entries/{title}.md', 'w') as file:
                file.write(page_details)

            return HttpResponseRedirect(reverse('wiki:wiki_entry', args=(title,)))

    form = NewPageForm()
    return render(request, "encyclopedia/create.html", {"form": form})


# Edit File
# Create Form for new page
class MarkdownForm(forms.Form):
    title = forms.CharField(label="Page Title", min_length=1)
    page_details = forms.CharField(widget=forms.Textarea, min_length=10)

    title.widget.attrs.update({'class': 'form-control mt-3 mb-3 w-75'})
    page_details.widget.attrs.update({'class': 'form-control w-75'})


def edit_markdown_view(request, file_path):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)

        # Validator
        if form.is_valid():
            title = form.cleaned_data['title']
            page_details = form.cleaned_data['page_details']

            # Update file
            with open(f'./entries/{title}.md', 'w') as file:
                file.write(page_details)

            return HttpResponseRedirect(reverse('wiki:wiki_entry', args=(title,)))

    
    with open(f'./entries/{file_path}.md', 'r') as file:
        title = file_path
        page_details = file.read()
        form = MarkdownForm(initial={'title': title, 'page_details': page_details})

        return render(request, 'encyclopedia/edit_markdown.html', {'form': form, "file_path":file_path})


# Return Random Page
def random_page(request): 
    random_entry = random.choice(list_entries())

    return redirect(f'/wiki/{random_entry}')