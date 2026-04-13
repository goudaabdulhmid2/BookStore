from django import forms
from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    brief = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    no_of_pages = forms.IntegerField(min_value=1)
    price = forms.DecimalField(max_digits=6, decimal_places=2, min_value=0)

    def __init__ (self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        query = Book.objects.filter(title__iexact=title)

        if self.instance:
            query = query.exclude(id=self.instance.id)
        
        if query.exists():
            raise forms.ValidationError("Book title already exists.")
        
        return title

