from django.shortcuts import render, redirect
from django.shortcuts import render

def home(request):
    return render(request, 'learning/home.html')

def login_page(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            return render(
                request,
                'learning/login.html',
                {'success': 'Login Successful'}
            )

        return render(
            request,
            'learning/login.html',
            {'error': 'Invalid Email or Password'}
        )

    return render(request, 'learning/login.html')

def register_page(request):

    if request.method == "POST":

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(
                request,
                'learning/register.html',
                {'error': 'Email already registered'}
            )

        User.objects.create(
            full_name=full_name,
            email=email,
            role=role,
            password=password
        )

        return redirect('/login/')

    return render(request, 'learning/register.html')

    
from .models import User