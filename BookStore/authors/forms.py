from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "bio", "gender", "books"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
            "books": forms.SelectMultiple(),
        }
