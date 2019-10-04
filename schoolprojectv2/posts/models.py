from django.db import models
from multiselectfield import MultiSelectField
from users.choices import INTERESTS_CHOICES
from votes.models import Vote
from comments.models import Comment
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from categories.models import Category

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    datestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        blank=True,
        null=True
    )
    activities = GenericRelation(Vote)

    def __str__(self):
        return f"{self.title} : {self.category.category_name}"

    def get_username(self):
        return self.user.email

    def get_likes(self):
        return self.activities.likes()

    def get_comments(self):
        return self.comments.filter_by_instance(instance=self)

    @property
    def category_type(self):
        return self.category.category_type

    @property
    def category_name(self):
        return self.category.category_name


    # ADD : get_like_history --> Get the history of users who liked that post
    # ADD : @property(downvotes) that count how many get_downvotes have been created for this post
