from django.contrib import admin
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "price", "no_of_pages", "authors_list", "created_at")
	search_fields = ("title",)

	def get_queryset(self, request):
		return super().get_queryset(request).prefetch_related("authors")

	def authors_list(self, obj):
		return ", ".join(author.name for author in obj.authors.all()) or "-"

	authors_list.short_description = "Authors"

