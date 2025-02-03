from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    playstore_link = models.URLField(default='https://play.google.com/store/apps/details?id=com.example')

    def __str__(self):
        return self.name

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    points_earned = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name} - {'Completed' if self.completed else 'Not Completed'}"

class Point(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='point_entries')
    value = models.IntegerField()
    date_earned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} points for {self.app.name} on {self.date_earned}"

class Screenshot(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/')  # Directory to save uploaded screenshots
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class UserDownload(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    date_downloaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} downloaded {self.app.name}"
