# Generated by Django 2.2.5 on 2019-09-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190920_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
