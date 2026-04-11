from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.order_by("-created_at")
    return render(request, "books/index.html", context={"books": books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "books/view.html", context={"book": book})


def create(request):
    form = BookForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        book = form.save()
        messages.success(request, "Book created successfully.")
        return redirect("books.show", id=book.id)

    return render(request, "books/form.html", context={"form": form, "page_title": "Create Book"})


def update(request, id):
    book = get_object_or_404(Book, id=id)
    initial = {
        "title": book.title,
        "brief": book.brief,
        "no_of_pages": book.no_of_pages,
        "price": book.price,
    }
    form = BookForm(
        request.POST or None,
        request.FILES or None,
        instance=book,
        initial=initial,
    )

    if request.method == "POST" and form.is_valid():
        book = form.save()
        messages.success(request, "Book updated successfully.")
        return redirect("books.show", id=book.id)

    return render(
        request,
        "books/form.html",
        context={"form": form, "book": book, "page_title": "Update Book"},
    )


def delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect("books.index")

    return render(request, "books/delete.html", context={"book": book})
