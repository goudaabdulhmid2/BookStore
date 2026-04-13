from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.shortcuts import reverse


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    brief = models.TextField()
    image = models.ImageField(upload_to="books/images", blank=True)
    no_of_pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.title:
            self.title = self.title.strip()

        if not self.title:
            raise ValidationError({"title": "Title is required."})

        if not (self.brief or "").strip():
            raise ValidationError({"brief": "Brief is required."})

    def __str__(self):
        return self.title

    @property
    def show_url(self):
        return reverse("books.show", args=[self.id])

    @property
    def image_url(self):
        if self.image:
            return self.image.url

        return ""
