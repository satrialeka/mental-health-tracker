import uuid 
from django.db import models
from django.contrib.auth.models import User


class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5