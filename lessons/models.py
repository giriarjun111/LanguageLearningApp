from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Language(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('language_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Quiz(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    questions = models.JSONField()  # Store questions and options as JSON

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'pk':self.pk})


    def __str__(self):
        return f"Quiz for {self.language.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    subscription_type = models.CharField(max_length=20, choices=[('Free', 'Free'), ('Individual', 'Individual'), ('Business', 'Business'), ('Professional', 'Professional')])
    progress = models.JSONField(default=dict)  # Store user progress as JSON & Default value set to an empty dictionary

    # def get_absolute_url(self):
    #     return reverse('userprofile_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username
