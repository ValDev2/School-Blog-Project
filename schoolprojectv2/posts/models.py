from django.db import models
from multiselectfield import MultiSelectField
from users.choices import INTERESTS_CHOICES
from votes.models import Vote
from users.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    datestamp = models.DateTimeField(auto_now_add=True)
    tags = MultiSelectField(
        choices = INTERESTS_CHOICES,
        max_choices = 5,
        max_length = 50,
        blank=True,
        null=True
    )
    #return a QS of like instances
    activities = GenericRelation(Vote)

    def __str__(self):
        return self.title

    def get_username(self):
        return self.user.email

    # ADD : get_like_history --> Get the history of users who liked that post
    # ADD : @property(downvotes) that count how many get_downvotes have been created for this post
