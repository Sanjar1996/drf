from django.db import models


# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=255, default='Kitob nomi', )
    subtitle = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.title
