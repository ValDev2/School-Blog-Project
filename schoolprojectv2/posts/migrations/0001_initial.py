# Generated by Django 2.2.5 on 2019-09-21 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='vote_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('F', 'Favorite'), ('L', 'Like'), ('D', 'Down vote')], max_length=1)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mat', 'Maths'), ('phy', 'Physics'), ('his', 'History'), ('bio', 'Biologie'), ('eco', 'Economics'), ('pol', 'Politics'), ('mus', 'Music'), ('eng', 'English'), ('fra', 'French'), ('spa', 'Spanish'), ('law', 'Law'), ('cs', 'Computer Science'), ('com', 'Communication'), ('mar', 'Marketing'), ('spo', 'Sport')], max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]