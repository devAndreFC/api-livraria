from django.contrib import admin
from django.urls import path

from .views import CategoriesView


urlpatterns = [
    path('categorias/', CategoriesView.as_view(), name='categorias'),
    path('categorias/<int:id>/', CategoriesView.as_view(), name='categoria'),
]
