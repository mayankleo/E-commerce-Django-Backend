from rest_framework import serializers
from .models import Product, Category, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    product_image_urls = ProductImageSerializer(source="productimage_set", many=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_fields = ["product_image_urls"]


class ProductListSerializer(serializers.ModelSerializer):
    product_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ["product_registered_at", "product_updated_at", "product_quantity"]

    def get_product_image(self, obj) -> str:
        first_image = obj.productimage_set.first()
        if first_image:
            return ProductImageSerializer(first_image, context=self.context).data.get(
                "product_image_url"
            )
        return ""
