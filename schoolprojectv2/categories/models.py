from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


#category type manager
class CategoryTypeManager(models.Manager):
    #Retourne les sous catégories d'un Type de catégorie
    def filter_by_type(self):
        qs = CategoryField.objects.filter(category_type=self.model.category_type)
        return qs

#Type de catégorie : Sciences, Littérature ...
class CategoryType(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        blank=True,
        null=True
    )
    category_type = models.CharField(max_length = 100, unique = True)
    objects = CategoryTypeManager()
    slug = models.SlugField(max_length=40, default="", blank=True, null=True)

    def __str__(self):
        return self.category_type

    def save(self, *args, **kwargs):
        user = self.created_by
        if user.is_admin:
            self.create_slug()
            super(CategoryType, self).save(*args, **kwargs)
        else: 
            return ValidationError('You must be an Admin User !')

    def create_slug(self):
        self.slug = slugify(self.category_type)
        return self.slug

    #Retourne les sous-cat d'un Type de catégorie
    def get_subcategories(self):
        qs = CategoryField.objects.filter(category_type=self)
        return qs


#Sous catégories : mathématiques, histoire ...
class CategoryField(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    category_type = models.ForeignKey(
        CategoryType,
        on_delete = models.CASCADE
    )
    category_name = models.CharField(
        unique=True,
        max_length=100,
    )

    slug = models.SlugField(max_length=40, default="", blank=True, null=True)

    def __str__(self):
        return self.category_name

    def create_slug(self):
        self.slug = slugify(self.category_name)
        return self.slug

    #Les administrateurs sont les seuls à pouvoir modifier les catégories.
    def save(self, *args, **kwargs):
        user = self.created_by
        if user.is_admin:
            self.create_slug()
            super(CategoryField, self).save()
        return ValidationError('You must be an Admin User !')
