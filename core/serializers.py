from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField)
from .models import Category, Publisher, Author, Book, Purchase, ItemsPurchase


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(ModelSerializer):
    category = CharField(source='category.name')
    authors = SerializerMethodField()
    publisher = CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

    def get_authors(self, instance):
        name_authors = []
        authors = instance.authors.get_queryset()
        for author in authors:
            name_authors.append(author.name)
        return name_authors


class ItemsPurchaseSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItemsPurchase
        fields = ('book', 'quantify', 'total')
        depth = 1

    def get_total(self, instance):
        return instance.quantify * instance.book.price


class PurchaseSerializer(ModelSerializer):
    user = CharField(source='user.first_name')
    status = SerializerMethodField()
    Items = ItemsPurchaseSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ('id', 'status', 'user', 'Items', 'total')

    def get_status(self, instace):
        return instace.get_status_display()
