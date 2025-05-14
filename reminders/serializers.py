from rest_framework import serializers
from .models import Reminder
from django.utils import timezone

class ReminderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reminder
        fields = ['id', 'reminder_date', 'reminder_time', 'message', 'reminder_method', 'created_at']
        read_only_fields = ['id', 'created_at']