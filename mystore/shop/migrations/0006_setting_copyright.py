# Generated by Django 5.0.6 on 2024-10-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='copyright',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]