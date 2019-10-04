from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class VoteManager(models.Manager):
    def likes(self):
        return self.get_queryset().filter(activity_type="L")
    def downvotes(self):
        return self.get_queryset().filter(activity_type="D")
    def favorites(self):
        return self.get_queryset().filter(activity_type="F")

# Create your models here.
class Vote(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = [
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (DOWN_VOTE, 'Down vote')
    ]

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    datestamp = models.DateTimeField(auto_now_add=True)
    #Model instance
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #Target's Id
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    objects = VoteManager()

    def __str__(self):
        return f"{self.user.email} used the action {self.activity_type} on post : {self.content_object.title}"

    def from_user(self):
        return str(self.user.email)
