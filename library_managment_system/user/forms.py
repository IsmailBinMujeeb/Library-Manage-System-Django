from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Book_Form(forms.ModelForm):

    class Meta:

        model = Book
        fields = ('book_name', 'cover_image', 'issued_date', 'auther', 'category')

class Member_Form(UserCreationForm):

    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Member_login_Form(AuthenticationForm):

    class Meta:

        model = User
        fields = ('username', 'password1', 'password2')