from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):

    categories = [('ACT', 'Action'), ('ROM', 'Romance'), ('MYS', 'Mystries'), ('THR', 'Thrill'), ('HOR', 'Horror')]

    book_name = models.CharField(max_length=100)
    issued_date = models.DateField()
    auther = models.CharField(max_length=50)
    category = models.CharField(max_length=3, choices=categories, default='HOR')

# class Member(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
