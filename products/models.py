from django.db import models
from django.db.models import Avg, Count
from profiles.models import UserProfile
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Occasion(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey('Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    sku_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def averageRating(self):
        rating = Reviews.objects.filter(product=self, status=True).aggregate(average=Avg('star_rating'))
        avg = 0
        if rating['average'] is not None:
            avg = float(rating['average'])
        return avg

    def reviewCount(self):
        rating = Reviews.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if rating['count'] is not None:
            count = int(rating['count'])
        return count


class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=600, blank=True)
    star_rating = models.DecimalField(max_digits=6, decimal_places=1, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class savedListItems(models.Model):
    """
    A saved item list model to keep users saved items
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Product, blank=True)
