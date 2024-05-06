from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/category/")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/product/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name