# Generated by Django 5.1.7 on 2025-03-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='chais/'),
        ),
    ]
