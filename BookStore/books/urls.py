from django.urls import path
from books.views import index, show, create, update, delete

urlpatterns = [
    path("", index, name="books.index"),
    path("index.html", index, name="books.index_html"),
    path("create/", create, name="books.create"),
    path("<int:id>/", show, name="books.show"),
    path("<int:id>/edit/", update, name="books.update"),
    path("<int:id>/delete/", delete, name="books.delete"),

]
