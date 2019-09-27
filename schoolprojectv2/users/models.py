from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from multiselectfield import MultiSelectField
from .school_datas import college_list
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Student, Teacher
from comments.models import Comment
from .choices import COLLEGES, INTERESTS_CHOICES, RANKING_CHOICES


class UserManager(BaseUserManager):
    #custom create_user method
    def create_user(self, email, password=None, is_student=True):
        if not email:
            raise ValueError('Users must have an email address')
        if is_student == None:
            raise ValueError('You must provide a status')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.is_student = is_student
        user.save(using=self._db)
        print(user)
        return user

    #Custom create_super_user method
    def create_superuser(self, email, password=None, is_student=False):
        user = self.create_user(
            email = email,
            password = password,
        )
        user.is_student = is_student
        user.admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    school = MultiSelectField(
        max_length = 400,
        choices = COLLEGES,
        max_choices=3,
        blank=True
    )
    interests = MultiSelectField(
        max_length = 7,
        choices = INTERESTS_CHOICES,
        blank=True,
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=False,
        null=False
    )
    followers = models.ManyToManyField(
        "User",
        related_name = "followers_list",
        blank=True,
    )
    following = models.ManyToManyField(
        "User",
        related_name = "following_list",
        blank=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    birth_date = models.DateField(null=True, blank=True)
    reputation = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    rank = models.CharField(choices=RANKING_CHOICES, max_length=5, default="basic")
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    bio = models.TextField(
        max_length=300,
        default="default Bio",
        blank=True
    )
    is_student = models.BooleanField(blank=True, null=True)
    objects = UserManager()
    #Setting email to be the main source of authentication
    USERNAME_FIELD = 'email'

    #Super User Only
    REQUIRED_FIELDS = ['password']

    #def get_absolute_url(self):
        #use reverse + nom de l'url de view

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def set_user_league(self):
        if 15 <= self.reputation < 40:
            self.rank = "gold"
        elif 40 <= self.reputation < 80:
            self.rank = "platinium"
        else:
            self.rank = "diamond"

    @property
    def is_admin(self):
        print(f" is {self.email} admin ? ")
        return self.admin

    @property
    def status(self):
        if self.is_student == None:
            "visitor"
        elif self.is_student == True:
            return "Student"
        else:
            return "Teacher"

    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, obj=None):
        return True

    def get_sent_friendrequest(self):
        fqs = FriendRequest.objects.filter(from_user=self.id)
        return fqs

    def get_friendrequest(self):
        fqs = FriendRequest.objects.filter(to_user=self.id)
        return fqs

    def get_user_comments(self):
        qs = Comment.objects.filter(user=self)
        return qs


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student is not None:
            if instance.is_student:
                student = Student.objects.create(user=instance)
                #Keeping track of user_profile changes
                instance.profile_history.append({
                    "type" : "Student",
                    "datestamp" : student.datestamp
                })
                print("creation of instance STUDENT")
            elif instance.is_student:
                teacher = Teacher.objects.create(user=instance)
                #Keeping track of user_profile changes
                instance.profile_history.append({
                    "type" : "Teacher",
                    "datestamp" : teacher.datestamp
                })
                print("Creation of instance Teacher ! ")

#change user profile on update
@receiver(post_save, sender = User)
def update_profile(sender, instance, created, **kwargs):
    #Check if the user has already been created
    if created == False:
        if instance.is_student is not None:
            #Check the new value of the is_student attribute
            if instance.is_student:
                #Check if the user was previously a Teacher, if yes, delete the actual Teacher instance
                prev_teacher = eacher.objects.filter(user=instance).first()
                if prev_teacher is not None:
                    prev_teacher.delete()
                    print("deleting the previous profile : Teahcer")
                    student = Student.objects.create(user = instance)
                    student.save()
            #Do the exact same thing if is_student is False, but delete the existing Student instance
            elif instance.is_student == False:
                prev_student = Student.objects.filter(user=instance).first()
                if prev_student is not None:
                    prev_student.delete()
                    print("deleting the previous profile : Student")
                    teacher = Teacher.objects.create(user = instance)
                    teacher.save()
    else:
        print("Created")

#FriendRequest Model
class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "from_user"
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "to_user"
    )
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request sent frm {self.from_user} to {self.to_user}"



#Enable each user to add experiences
class Experience(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    date = models.DateField()
    content = models.TextField(max_length=300, blank=True, null=True)
    school = MultiSelectField(
        max_length = 400,
        choices = COLLEGES,
        max_choices=3,
        blank=True
    )
    #Replace Company name with auto fill
    company = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        if self.company:
            return f"{self.user}a eu une expérience chez {self.company}"
        else:
            return f"{self.user}a eu une expérience chez {self.school}"
