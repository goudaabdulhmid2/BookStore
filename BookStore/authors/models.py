from django.db import models

# Create your models here.


class Author(models.Model):
	GENDER_CHOICES = [
		("male", "Male"),
		("female", "Female"),
	]

	name = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	bio = models.TextField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	books = models.ManyToManyField("books.Book", related_name="authors", blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
