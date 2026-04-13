from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.prefetch_related("authors").all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def book_detail(request, pk):
    book = get_object_or_404(Book.objects.prefetch_related("authors"), pk=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ["PUT", "PATCH"]:
        serializer = BookSerializer(book, data=request.data, partial=request.method == "PATCH")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    book.delete()
    return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
