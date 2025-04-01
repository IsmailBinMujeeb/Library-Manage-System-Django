from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):

    categories = [('ACT', 'Action'), ('ROM', 'Romance'), ('MYS', 'Mystries'), ('THR', 'Thrill'), ('HOR', 'Horror')]

    book_name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    issued_date = models.DateField()
    auther = models.CharField(max_length=50)
    category = models.CharField(max_length=3, choices=categories, default='HOR')

    def __str__(self):
        return self.book_name

# class Member(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
