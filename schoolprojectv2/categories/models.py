from django.db import models
from django.conf import settings

class Category(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    category_type = models.CharField(
        max_length=100
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
            super(Category, self).save()
            return user
        else:
            return ValidationError('You must be an Admin User !')
