# Generated by Django 2.2.5 on 2019-09-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(blank=True),
        ),
    ]
