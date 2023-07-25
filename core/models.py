from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    site = models.URLField()

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Book(models.Model):
    tittle = models.CharField(max_length=255, unique=True)
    ISBN = models.CharField(max_length=50)
    quantify = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='books')
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, related_name='books')
    authors = models.ManyToManyField(Author, related_name='Books')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.tittle} ({self.publisher})'


class Purchase(models.Model):
    class StatusPurchase(models.IntegerChoices):
        CART = 1, 'Cart'
        ORDER = 2, 'Order'
        PAID = 3, 'Paid'
        DELIVERED = 4, 'Delivered'

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='Purchases')
    status = models.IntegerField(
        choices=StatusPurchase.choices, default=StatusPurchase.CART)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f'Purchse of {self.user}'

    @property
    def total(self):
        queryset = self.Items.all().aggregate(
            total=models.Sum(
                F('quantify')*F('book__price')
            )
        )
        return queryset['total']


class ItemsPurchase(models.Model):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, related_name='Items')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='+')
    quantify = models.IntegerField()

    class Meta:
        verbose_name = 'Purchase Items'
        verbose_name_plural = 'Purchase Items'

    def __str__(self):
        return f'Purchse ({self.purchase})'
