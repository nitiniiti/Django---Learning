from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(default='Awesome')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
               # return f"/product/{self.id}"
        # Another way
        return reverse("articles:article-detail-id", kwargs={"id": self.id})
