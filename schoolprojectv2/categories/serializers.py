from rest_framework import serializers
from .models import CategoryType, CategoryField
from posts.serializers import PostSerializer
from posts.models import Post

class CategoryTypeSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source="category_type", read_only=True, max_length=200)
    category_fields = serializers.SerializerMethodField()
    total_post_number = serializers.SerializerMethodField()

    def get_category_fields(self, obj):
        return CategoryFieldSerializer(obj.get_subcategories(), many=True).data

    def get_total_post_number(self, obj):
        qs = Post.objects.all()
        fqs = [ post for post in qs if post.category_type == obj]
        return qs.count()

    class Meta:
        model = CategoryType
        fields = ['total_post_number', 'category', 'category_fields']

class CategoryFieldSerializer(serializers.ModelSerializer):

    related_posts = serializers.SerializerMethodField()
    related_posts_number = serializers.SerializerMethodField()

    #Retourne tous les posts liés
    def get_related_posts(self, obj):
        qs = Post.objects.all().filter(category=obj)
        return PostSerializer(qs, many=True).data

    #Retourne le nombre de posts liés
    def get_related_posts_number(self, obj):
        qs = Post.objects.all().filter(category=obj)
        return qs.count()


    class Meta:
        model = CategoryField
        fields = ['category_name', 'related_posts_number', 'related_posts']
