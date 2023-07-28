from django.contrib import admin
from .models import Category, Publisher, Author, Book, Purchase, ItemsPurchase


admin.site.register(Author)

admin.site.register(Category)
admin.site.register(Publisher)
# admin.site.register(Purchase)
# admin.site.register(ItemsPurchase)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'quantify', 'category', 'publisher')
    list_filter = ('category', 'publisher')


class ItemsInline(admin.TabularInline):
    model = ItemsPurchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = (ItemsInline, )
