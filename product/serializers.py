from rest_framework import serializers
from .models import Product

class ProductSrializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        #fields =('name','brand','category','price')