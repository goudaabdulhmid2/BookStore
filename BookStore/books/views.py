from django.http import Http404
from django.shortcuts import render

# Create your views here.

books = [
    {"id": 1, "title": "The Great Gatsby", "breif": "A novel about the American dream.", "noOfPages": 180, "price": 10.90,"image":"1.jpg"},
    {"id": 2, "title": "To Kill a Mockingbird", "breif": "A novel about racial injustice.", "noOfPages": 281, "price": 12.50,"image":"2.jpg"},
    {"id": 3, "title": "1984", "breif": "A novel about a dystopian future.", "noOfPages": 328, "price": 15.00,"image":"3.jpg"}, 
    {"id": 4, "title": "Pride and Prejudice", "breif": "A novel about love and social class.", "noOfPages": 279, "price": 9.99,"image":"4.jpg"},
]

def index(request):
    return render(request, "books/index.html", context={"books": books})

def show(request, id):
    book = next((book for book in books if book["id"] == id), None)

    if not book:
        raise Http404("Book not found")
    
    return render(request, "books/view.html", context={"book": book})


