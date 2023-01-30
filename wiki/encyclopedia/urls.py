from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.wiki_entry, name="wiki_entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create_new_page, name="create_new_page"),
    path("edit/<str:file_path>/", views.edit_markdown_view, name="edit_markdown_view"),
    path("random/", views.random_page, name="random_page"),
]
