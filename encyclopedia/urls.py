from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("randomPage", views.randomPage, name="randomPage")
]

