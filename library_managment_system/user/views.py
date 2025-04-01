from django.shortcuts import render, redirect, get_object_or_404
from .forms import Member_Form, Member_login_Form, Book_Form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Book

def home_page(request):

    books = Book.objects.all()
    return render(request, "home_page.html", {'books': books})

def book_page(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'book_page.html', { 'book': book })

def register_page(request):

    if request.method == 'POST':

        form = Member_Form(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('home_page')

    return render(request, "register_page.html", { 'form': Member_Form })

def login_page(request):

    if request.POST:

        form = Member_login_Form(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect('home_page')
            

    form = Member_login_Form()
        

    return render(request, "login_page.html", {'form': form})

def logout_page(request):


    logout(request)

    return redirect("home_page")

def create_book_page(request):

    if request.method == 'POST':

        form = Book_Form(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('home_page')

    form = Book_Form()

    return render(request, 'create_book_page.html', { 'form': form })