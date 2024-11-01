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
    product_category = CategorySerializer()
    product_images = ProductImageSerializer(source="productimage_set", many=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_fields = ["product_images"]


class ProductListSerializer(serializers.ModelSerializer):
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ["product_registered", "product_updated", "product_quantity"]

    def get_product_image(self, obj) -> str:
        first_image = obj.productimage_set.first()
        if first_image:
            return ProductImageSerializer(first_image, context=self.context).data.get(
                "image_url"
            )
        return ""
