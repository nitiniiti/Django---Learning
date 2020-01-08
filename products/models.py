from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(default="Its cool")
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        # Another way
        return reverse("products:product-detail-id", kwargs={"id": self.id})
