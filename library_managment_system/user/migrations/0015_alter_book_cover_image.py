# Generated by Django 5.1.7 on 2025-03-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='covers/', verbose_name='Cover Image'),
        ),
    ]
