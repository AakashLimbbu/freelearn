from django.shortcuts import render

def home(request):
    return render(request, 'learning/home.html')

def login_page(request):
    return render(request, 'learning/login.html')

def register_page(request):

    if request.method == "POST":

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')

        User.objects.create(
            full_name=full_name,
            email=email,
            role=role,
            password=password
        )

    return render(request, 'learning/register.html')
from .models import User