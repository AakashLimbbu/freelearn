from django.shortcuts import render, redirect
from django.shortcuts import render

def dashboard(request):

    if not request.session.get('user_id'):
        return redirect('/login/')

    name = request.session.get('user_name')
    role = request.session.get('role')

    context = {
        'name': name,
        'role': role
    }

    return render(
        request,
        'learning/dashboard.html',
        context
    )

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

            request.session['user_id'] = user.id
            request.session['user_name'] = user.full_name
            request.session['role'] = user.role

            return redirect('/dashboard/')

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

def logout_page(request):

    request.session.flush()

    return redirect('/')

def upload_resource(request):

    if not request.session.get('user_id'):
        return redirect('/login/')
    if request.session.get('role') != 'Teacher':
        return redirect('/dashboard/')

    if request.method == "POST":

        title = request.POST.get('title')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        file_link = request.POST.get('file_link')

        Resource.objects.create(
            title=title,
            subject=subject,
            description=description,
            file_link=file_link,
            uploaded_by=request.session.get('user_name')
        )

        return redirect('/dashboard/')

    return render(
        request,
        'learning/upload_resource.html'
    )
def my_resources(request):

    if not request.session.get('user_id'):
        return redirect('/login/')

    resources = Resource.objects.filter(
        uploaded_by=request.session.get('user_name')
    )

    return render(
        request,
        'learning/my_resources.html',
        {
            'resources': resources
        }
    )
def resources(request):

    search = request.GET.get('search')

    resources = Resource.objects.filter(
        status='approved'
    )

    if search:

        resources = resources.filter(
            title__icontains=search
        )

    return render(
        request,
        'learning/resources.html',
        {'resources': resources}
    )
def admin_resources(request):

    resources = Resource.objects.all()

    return render(
        request,
        'learning/admin_resources.html',
        {
            'resources': resources
        }
    )
def approve_resource(request, resource_id):

    resource = Resource.objects.get(id=resource_id)

    resource.status = 'approved'

    resource.save()

    return redirect('/admin-resources/')
def reject_resource(request, resource_id):

    resource = Resource.objects.get(id=resource_id)

    resource.status = 'rejected'

    resource.save()

    return redirect('/admin-resources/')
from .models import User, Resource