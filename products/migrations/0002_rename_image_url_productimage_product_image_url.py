# Generated by Django 5.1.2 on 2024-11-01 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image_url',
            new_name='product_image_url',
        ),
    ]
