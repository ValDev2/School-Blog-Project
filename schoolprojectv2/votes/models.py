from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User


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
        User,
        on_delete = models.CASCADE
    )
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    datestamp = models.DateTimeField(auto_now_add=True)
    #Model instance
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #Target's Id
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.user.email} liked the post : {self.content_object.title}"
