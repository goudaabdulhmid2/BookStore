from django.urls import path
from books.views import index, show

urlpatterns = [
    path("", index, name="books.index"),
    path("<int:id>/", show, name="books.show"),
]
