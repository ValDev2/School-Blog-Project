from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from users.choices import COLLEGES, INTERESTS_CHOICES
from users.school_datas import formations


GRADES = (
    ('L1', 'Licence1'),
    ('L2', 'Licence2'),
    ('L3', 'Licence3'),
    ('M1', 'Master 1'),
    ('M2', 'Master 2')
)

class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    grade = models.CharField(
        choices = GRADES,
        blank=True,
        max_length = 50,
        default='L1'
    )
    major = models.CharField(
        choices = INTERESTS_CHOICES,
        max_length = 50,
        blank=True,
        null=True
    )
    degree = models.CharField(
        choices = formations,
        max_length = 100,
        blank=True,
        null=True
    )
    datestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    def __str__(self):
        return f" Student {self.user.email}"

class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    researches = models.TextField(max_length=1000, default="Aucune information sur les travaux de recherches", blank=True, null=True)
    completed_degree = MultiSelectField(
        choices = formations,
        max_choices = 20,
        max_length = 271,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Teacher : {self.user.email}"
