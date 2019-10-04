from rest_framework import serializers
from .models import Category

class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name']
