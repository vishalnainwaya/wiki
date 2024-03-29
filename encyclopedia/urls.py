from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search , name="search"),
    path("create", views.create , name="create"),
    path("randompage", views.randompage , name="randompage"),
    path("edit/<str:entry>",views.edit , name="edit"),
    path("del/<str:entry>",views.deleteentry,name="deleteentry"),
    path("wiki/<str:entry>", views.entry, name="entry")
]
