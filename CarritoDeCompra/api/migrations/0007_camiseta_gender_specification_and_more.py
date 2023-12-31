# Generated by Django 4.2.7 on 2023-12-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_camiseta_typo_tejido_delete_tejido'),
    ]

    operations = [
        migrations.AddField(
            model_name='camiseta',
            name='gender_specification',
            field=models.CharField(choices=[('MEN', 'Men'), ('WOMEN', 'Women'), ('UNISEX', 'Unisex')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='camiseta',
            name='size_specification',
            field=models.CharField(max_length=10),
        ),
    ]
