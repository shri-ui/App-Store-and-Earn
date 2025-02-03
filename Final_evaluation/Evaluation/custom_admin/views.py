from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import App, UserTask
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

@login_required
def admin_dashboard(request):
    tasks = UserTask.objects.select_related('user', 'app').all()
    apps = App.objects.all()
    return render(request, 'custom_admin/dashboard.html', {'tasks': tasks, 'apps': apps})

@login_required
def edit_user(request, user_id):
    user_profile = get_object_or_404(UserTask, user_id=user_id)
    if request.method == 'POST':
        user_profile.points = request.POST.get('points', user_profile.points)
        user_profile.save()
        return redirect('custom_admin_dashboard')
    return render(request, 'custom_admin/edit_user.html', {'user_profile': user_profile})

@login_required
def delete_user(request, user_id):
    user_profile = get_object_or_404(UserTask, user_id=user_id)
    user_profile.delete()
    return redirect('custom_admin_dashboard')

@login_required
def add_app(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        points = request.POST.get('points')
        playstore_link = request.POST.get('playstore_link')
        App.objects.create(name=name, points=points, playstore_link=playstore_link)
        return redirect('custom_admin_dashboard')
    return render(request, 'custom_admin/add_app.html')

@login_required
def edit_app(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if request.method == 'POST':
        app.name = request.POST.get('name', app.name)
        app.points = request.POST.get('points', app.points)
        app.playstore_link = request.POST.get('playstore_link', app.playstore_link)
        app.save()
        return redirect('custom_admin_dashboard')
    return render(request, 'custom_admin/edit_app.html', {'app': app})

@login_required
def delete_app(request, app_id):
    app = get_object_or_404(App, id=app_id)
    app.delete()
    return redirect('custom_admin_dashboard')

@login_required
def assign_points(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        points = request.POST.get('points')
        user_task = get_object_or_404(UserTask, id=task_id)
        user_task.points_earned += int(points)
        user_task.save()
        return redirect('custom_admin_dashboard')
    tasks = UserTask.objects.select_related('user', 'app').all()
    return render(request, 'custom_admin/assign_points.html', {'tasks': tasks})

@login_required
def download_app(request, user_id, app_id):
    user = get_object_or_404(User, id=user_id)
    app = get_object_or_404(App, id=app_id)
    UserTask.objects.create(user=user, app=app)
    return redirect('custom_admin_dashboard')

@login_required
def custom_admin_logout(request):
    logout(request) 
    return redirect('custom_admin_login')  

def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('custom_admin_dashboard')
        else:
            return render(request, 'custom_admin/login.html', {'error': 'Invalid credentials'})
    return render(request, 'custom_admin/login.html')
