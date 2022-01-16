
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator ,MaxValueValidator
# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=360)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name


class Rating(models.Model):

    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        verbose_name = ("Rating")
        verbose_name_plural = ("Ratings")
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)

