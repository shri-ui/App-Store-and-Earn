from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import App, UserTask, Point
from .serializers import AppSerializer, UserTaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AppForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view, permission_classes

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
    permission_classes = [IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
   
    pass


def home(request):
    return render(request, 'home.html') 

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'signup.html')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('show_apps')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def upload_screenshot(request, app_id):
    app = get_object_or_404(App, id=app_id)  # Get the app instance by ID

    if request.method == 'POST':
        screenshot = request.FILES['screenshot']  # Get the uploaded file
        fs = FileSystemStorage() 
        filename = fs.save(screenshot.name, screenshot)
        uploaded_file_url = fs.url(filename)  # Get the URL of the uploaded file

        return redirect('upload_success', app_id=app_id)  # Redirect with app_id

    return render(request, 'upload_screenshot.html', {'app_id': app_id, 'app': app}) 


def upload_success(request, app_id):
    return render(request, 'upload_success.html', {'app_id': app_id})


def apps_page(request):
    apps = App.objects.all()
    return render(request, 'apps.html', {'apps': apps})  

# Custom permission check
def is_admin(user):
    return user.is_staff  # Check if the user is an admin

@login_required
@user_passes_test(is_admin)
def manage_apps(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_apps')  # Redirect to the same page after saving
    else:
        form = AppForm()
    apps = App.objects.all()
    return render(request, 'manage_apps.html', {'form': form, 'apps': apps})

@login_required
def show_apps(request):
    apps = App.objects.all()  # Get all available apps
    return render(request, 'show_apps.html', {'apps': apps})

@login_required
def points_earned(request, app_id):
    app = get_object_or_404(App, id=app_id)  # Get the app by ID
    points = Point.objects.filter(app=app)  # Get points related to the app

    return render(request, 'points_earned.html', {'app': app, 'points': points})

def redirect_to_signup(request):
    return redirect('signup')  # Redirect to the signup page

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return render(request, 'protected_view.html') 


