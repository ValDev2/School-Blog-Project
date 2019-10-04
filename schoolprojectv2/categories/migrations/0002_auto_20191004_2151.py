# Generated by Django 2.2.5 on 2019-10-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='NAME', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
