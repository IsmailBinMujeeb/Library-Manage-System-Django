# Generated by Django 5.1.7 on 2025-03-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('issued_date', models.DateField()),
                ('auther', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('ACT', 'Action'), ('ROM', 'Romance'), ('MYS', 'Mystries'), ('THR', 'Thrill'), ('HOR', 'Horror')], default='HOR', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('books_borrow', models.ManyToManyField(related_name='users', to='user.book')),
            ],
        ),
    ]
