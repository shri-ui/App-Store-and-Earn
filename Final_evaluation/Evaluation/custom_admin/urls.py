from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    admin_dashboard,
    add_app,
    edit_app,
    delete_app,
    assign_points,
    download_app,
    custom_admin_login,
    custom_admin_logout,
)

urlpatterns = [
    path('admin/', admin_dashboard, name='custom_admin_dashboard'),
    path('login/', custom_admin_login, name='custom_admin_login'),
    path('logout/', custom_admin_logout, name='custom_admin_logout'),
    path('add-app/', add_app, name='add_app'),
    path('edit-app/<int:app_id>/', edit_app, name='edit_app'),
    path('delete-app/<int:app_id>/', delete_app, name='delete_app'),
    path('assign-points/', assign_points, name='assign_points'),
    path('download-app/<int:user_id>/<int:app_id>/', download_app, name='download_app'),
]
