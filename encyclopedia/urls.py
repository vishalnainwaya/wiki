from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:link>",views.link, name="link"),
    path("randpg",views.randpg, name="randpg"),
    path("search",views.search, name="search"),
    path("create",views.create, name="create"),
    path("edit/<str:link>",views.edit, name="edit")
]
