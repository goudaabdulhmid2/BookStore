from django.urls import path
from books import views

urlpatterns = [
    path("", views.index, name="books.index"),
    path("index.html", views.index, name="books.index_html"),
    path("create/", views.create, name="books.create"),
    path("<int:id>/", views.show, name="books.show"),
    path("<int:id>/edit/", views.update, name="books.update"),
    path("<int:id>/delete/", views.delete, name="books.delete"),
]
