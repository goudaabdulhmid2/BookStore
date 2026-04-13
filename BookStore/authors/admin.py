from django.contrib import admin
from .models import Author

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "gender", "created_at", "updated_at")
	search_fields = ("name", "email")
	list_filter = ("gender", "created_at")
	filter_horizontal = ("books",)
