from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Stone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(unique=True)
    product_code = models.CharField(max_length=64, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    stones = models.ManyToManyField(
        Stone,
        related_name="products",
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    size = models.ForeignKey(
        Size,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    
    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    upload = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )
