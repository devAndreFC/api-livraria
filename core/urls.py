from django.urls import path, include

from rest_framework import routers

from core.views.categories import CategoryViewSet
from core.views.publishers import PublisherViewSet
from core.views.authors import AuthorViewSet
from core.views.books import BookViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet)
router.register(r'editoras', PublisherViewSet)
router.register(r'autores', AuthorViewSet)
router.register(r'livros', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
