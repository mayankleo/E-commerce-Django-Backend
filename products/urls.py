from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.ProductViewSet, basename='products')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'productImage', views.ProductImageViewSet, basename='productImage')

urlpatterns = [
    path('', include(router.urls)),
    path("slug/<slug:slug>/", views.ProductViewSet.as_view({'get': 'retrieve_by_slug'}), name='product-detail-by-slug'),
]
