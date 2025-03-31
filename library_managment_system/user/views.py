from django.shortcuts import render, redirect
from .forms import Member_Form, Member_login_Form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

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