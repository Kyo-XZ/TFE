# Generated by Django 5.0.6 on 2024-12-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_status_alter_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='regular_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='solde_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sub_total_ht',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sub_total_ttc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='taxe',
            field=models.FloatField(),
        ),
    ]
