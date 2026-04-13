from django.urls import path
from . import views

urlpatterns = [
    path("", views.AuthorListView.as_view(), name="authors.index"),
    path("create/", views.AuthorCreateView.as_view(), name="authors.create"),
    path("<int:id>/", views.AuthorDetailView.as_view(), name="authors.show"),
    path("<int:id>/edit/", views.AuthorUpdateView.as_view(), name="authors.update"),
    path("<int:id>/delete/", views.AuthorDeleteView.as_view(), name="authors.delete"),
]