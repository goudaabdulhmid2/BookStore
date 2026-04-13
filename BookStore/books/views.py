from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.order_by("-created_at")
    return render(request, "books/index.html", context={"books": books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "books/view.html", context={"book": book})


def create(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = Book()
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]

            if form.cleaned_data["image"]:
                book.image = form.cleaned_data["image"]

            book.full_clean()
            book.save()
            messages.success(request, "Book created successfully.")
            return redirect(reverse("books.show", args=[book.id]))

    return render(request, "books/form.html", context={"form": form, "page_title": "Create Book"})


def update(request, id):
    book = get_object_or_404(Book, id=id)
    initial = {
        "title": book.title,
        "brief": book.brief,
        "no_of_pages": book.no_of_pages,
        "price": book.price,
    }
    form = BookForm(instance=book, initial=initial)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book.title = form.cleaned_data["title"]
            book.brief = form.cleaned_data["brief"]
            book.no_of_pages = form.cleaned_data["no_of_pages"]
            book.price = form.cleaned_data["price"]

            if form.cleaned_data["image"]:
                book.image = form.cleaned_data["image"]

            book.full_clean()
            book.save()
            messages.success(request, "Book updated successfully.")
            return redirect(reverse("books.show", args=[book.id]))

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
