from django.urls import path

from contactus.views import index

urlpatterns = [
    path('', index, name='contactus.index'),
]
