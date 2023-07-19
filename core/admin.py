from django.contrib import admin
from .models import Category, Publisher, Author, Book, Purchase, ItemsPurchase


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Publisher)
# admin.site.register(Purchase)
# admin.site.register(ItemsPurchase)


class ItemsInline(admin.TabularInline):
    model = ItemsPurchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = (ItemsInline, )
