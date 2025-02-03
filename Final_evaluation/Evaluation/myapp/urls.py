from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, UserTaskViewSet, CustomTokenObtainPairView, home, signup, login_view, show_apps, upload_screenshot, points_earned, apps_page, upload_success, manage_apps, redirect_to_signup, protected_view
from django.contrib.auth import views as auth_views 

router = DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'tasks', UserTaskViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('show_apps/', show_apps, name='show_apps'),
    path('upload_screenshot/<int:app_id>/', upload_screenshot, name='upload_screenshot'),
    path('points_earned/<int:app_id>/', points_earned, name='points_earned'),
    path('apps/', apps_page, name='apps'),
    path('upload/success/<int:app_id>/', upload_success, name='upload_success'),
    path('manage_apps/', manage_apps, name='manage_apps'),
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('protected-view/', protected_view, name='protected_view'),
]