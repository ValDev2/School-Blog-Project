from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class CommentManager(models.Manager):
    #return all comments ()
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(model=instance)
        object_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=object_id).filter(parent=None)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    content = models.TextField(max_length=1000, default="")
    datestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self",
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = CommentManager()

    def __str__(self):
        return f"{self.user.email} commented on {self.content_type} : '{self.content[:30]}'"

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def get_children(self):
        qs = Comment.objects.filter(parent=self)
        return qs
