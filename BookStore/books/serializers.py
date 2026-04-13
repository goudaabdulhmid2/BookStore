from rest_framework import serializers
from authors.models import Author
from books.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all(),
        source="authors",
        write_only=True,
        required=False,
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "brief",
            "image",
            "no_of_pages",
            "price",
            "authors",
            "authors_ids",
            "created_at",
            "updated_at",
        ]
