# Generated by Django 5.1.5 on 2025-01-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usertask_points_earned'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='playstore_link',
            field=models.URLField(default='https://play.google.com/store/apps/details?id=com.example'),
        ),
    ]
