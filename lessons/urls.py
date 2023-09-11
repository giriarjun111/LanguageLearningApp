from django.urls import path
from .views import (
    UserProfileDetailView, IndexView,
    LanguageListView, LanguageDetailView,
    LessonListView, LessonDetailView, 
    QuizListView, QuizDetailView, 
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('language/', LanguageListView.as_view(), name='language_list'),
    path('language/<str:name>/', LanguageDetailView.as_view(), name='language_detail'),
    
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    
    path('quiz/', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),

    path('profile/<str:username>/', UserProfileDetailView.as_view(), name='profile'),    
]
