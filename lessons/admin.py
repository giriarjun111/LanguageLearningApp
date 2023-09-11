from django.contrib import admin
from .models import Language, Lesson, Quiz, UserProfile

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1  # Number of empty forms to display

class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 1

# Register Language model along with Lesson and Quiz
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [LessonInline, QuizInline]

# Register other models as before
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'language']
    search_fields = ['title', 'language__name']
    list_filter = ['language']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'language']
    list_filter = ['language']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription_type']
    search_fields = ['user__username']
    list_filter = ['subscription_type']
