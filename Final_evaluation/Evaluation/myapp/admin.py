from django.contrib import admin
from .models import App, UserTask

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
    search_fields = ('name',)
    
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'app', 'points_earned', 'completed')
    search_fields = ('user__username', 'app__name')
    list_filter = ('completed',)
    
    
admin.site.register(App, AppAdmin)
admin.site.register(UserTask, UserTaskAdmin)
