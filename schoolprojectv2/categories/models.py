from django.db import models
from django.conf import settings

class CategoryTypeManager(models.Manager):
    def filter_by_type(self):
        qs = CategoryField.objects.filter(category_type=self.model.category_type)
        return qs

class CategoryType(models.Model):
    category_type = models.CharField(max_length = 100, unique = True)
    objects = CategoryTypeManager()

    def __str__(self):
        return self.category_type

    def get_subcategories(self):
        qs = CategoryField.objects.filter(category_type=self)
        print(qs)
        return qs

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
        default="NAME"
    )

    def __str__(self):
        return self.category_name

    def save(self):
        user = self.created_by
        if user.is_admin:
            super(CategoryField, self).save()
            return user
        else:
            return ValidationError('You must be an Admin User !')
