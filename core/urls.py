from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views


router = routers.DefaultRouter()
router.register(r'categorias', views.CategoryViewSet)
router.register(r'editoras', views.PublisherViewSet)
router.register(r'autores', views.AuthorViewSet)
router.register(r'livros', views.BookViewSet)
router.register(r'compras', views.PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
