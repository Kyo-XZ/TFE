# Generated by Django 5.0.6 on 2024-10-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]