from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book


# Create your views here.


books = [
    {"id": 1, "title": "The Great Gatsby", "breif": "A novel about the American dream.", "noOfPages": 180, "price": 10.90,"image":"1.jpg"},
    {"id": 2, "title": "To Kill a Mockingbird", "breif": "A novel about racial injustice.", "noOfPages": 281, "price": 12.50,"image":"2.jpg"},
    {"id": 3, "title": "1984", "breif": "A novel about a dystopian future.", "noOfPages": 328, "price": 15.00,"image":"3.jpg"}, 
    {"id": 4, "title": "Pride and Prejudice", "breif": "A novel about love and social class.", "noOfPages": 279, "price": 9.99,"image":"4.jpg"},
]

def index(request):
    books = Book.objects.all()
    print(type(books))
    return render(request, "books/index.html", context={"books": books})

def show(request, id):
    book = get_object_or_404(Book,id=id)
    return render(request, "books/view.html", context={"book": book})


def create(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = Book()
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.image = form.cleaned_data["image"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]
            book.save()

            return redirect("books.index")
    
    return render(request, "books/create.html", context={"form": form, "is_update": False, "book": None})


def update(request, id):
    book = get_object_or_404(Book, id=id)

    form = BookForm(instance=book, initial={
        "title": book.title,
        "brief":book.brief,
        "no_of_pages":book.no_of_pages,
        "price":book.price,
    })

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]
            
            if form.cleaned_data["image"]:
                book.image = form.cleaned_data["image"]

            book.save()

            return redirect("books.show", id=book.id)
        
    return render(request, "books/create.html", context={"form": form, "is_update": True, "book": book})
   
            

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect("books.index")

    return redirect("books.show", id=book.id)
