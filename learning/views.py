from django.shortcuts import render

def home(request):
    return render(request, 'learning/home.html')

def login_page(request):
    return render(request, 'learning/login.html')

def register_page(request):
    return render(request, 'learning/register.html')