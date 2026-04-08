from django.shortcuts import render

# Create your views here.
auhtors = [
    {"id": 1, "name": "F. Scott Fitzgerald", "bio": "An American novelist known for his portrayal of the Jazz Age.", "image": "1.jpg"},
    {"id": 2, "name": "Harper Lee", "bio": "    An American novelist best known for her novel 'To Kill a Mockingbird'.", "image": "2.jpg"},
    {"id": 3, "name": "George Orwell", "bio": "An English novelist and essayist known for his dystopian works.", "image": "3.jpg"},
    {"id": 4, "name": "Jane Austen", "bio": "An English novelist known for her romantic fiction set among the British landed gentry.", "image": "4.jpg"},
]

def index(request):
    return render(request, "authors/index.html", context={"authors": auhtors})