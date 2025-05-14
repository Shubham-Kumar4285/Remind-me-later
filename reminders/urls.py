# reminders/urls.py
from django.urls import path
from .views import create_reminder, list_reminders 

urlpatterns = [
    path('create/', create_reminder, name='create-reminder'),
    path('list/', list_reminders, name='list-reminders'),
]