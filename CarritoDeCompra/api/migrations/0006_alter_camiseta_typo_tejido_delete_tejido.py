# Generated by Django 4.2.7 on 2023-12-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cart_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camiseta',
            name='typo_tejido',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Tejido',
        ),
    ]
