from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    brief = models.TextField()
    image = models.ImageField(upload_to='books/images', blank=True)
    no_of_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2 ,validators= [MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
