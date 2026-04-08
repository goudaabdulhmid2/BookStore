from django.urls import path
from aboutus.views import index

urlpatterns = [
    path('', index, name='aboutus.index'),
]