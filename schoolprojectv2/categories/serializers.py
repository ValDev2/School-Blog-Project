from rest_framework import serializers
from .models import CategoryType, CategoryField


class CategoryTypeSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source="category_type", read_only=True, max_length=200)
    category_fields = serializers.SerializerMethodField()

    def get_category_fields(self, obj):
        return CategoryFieldSerializer(obj.get_subcategories(), many=True).data

    class Meta:
        model = CategoryType
        fields = ['category', 'category_fields']

class CategoryFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryField
        fields = ['category_name']
