from django import forms

from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    brief = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    no_of_pages = forms.IntegerField(min_value=1)
    price = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0.01)

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        query = Book.objects.filter(title__iexact=title)

        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise forms.ValidationError("A book with this title already exists.")

        return title

    def clean_brief(self):
        brief = self.cleaned_data["brief"].strip()

        if not brief:
            raise forms.ValidationError("Brief is required.")

        return brief

    def save(self):
        book = self.instance or Book()
        book.title = self.cleaned_data["title"]
        book.brief = self.cleaned_data["brief"]
        book.no_of_pages = self.cleaned_data["no_of_pages"]
        book.price = self.cleaned_data["price"]

        if self.cleaned_data.get("image"):
            book.image = self.cleaned_data["image"]

        book.full_clean()
        book.save()
        return book
