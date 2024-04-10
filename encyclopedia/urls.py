from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:nombre>", views.entry, name="entry"),
    path("search/",views.buscar, name="buscar"),
    path("new/",views.new, name="new"),
    path("edit/",views.edit, name="edit"),
    path("save/",views.save, name="save"),
    path("random_page/",views.random_page, name="random_page")
]
