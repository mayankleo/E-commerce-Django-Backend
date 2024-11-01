from .models import Category, Product, ProductImage
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductImageSerializer,
    ProductListSerializer,
)
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    # http_method_names = ["get"]
    # renderer_classes = [JSONRenderer]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductSerializer
    
    def retrieve_by_slug(self, request, slug):
        try:
            product = self.queryset.get(product_slug=slug)
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."},status=status.HTTP_404_NOT_FOUND)
        

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

