# Generated by Django 2.2.5 on 2019-10-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20191005_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryfield',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='categorytype',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=40, null=True),
        ),
    ]
