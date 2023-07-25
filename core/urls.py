from django.urls import path, include

from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoryViewSet)
router.register(r'editoras', views.PublisherViewSet)
router.register(r'autores', views.AuthorViewSet)
router.register(r'livros', views.BookViewSet)
router.register(r'compras', views.PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
