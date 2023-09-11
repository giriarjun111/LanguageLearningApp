import stripe
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Language, Lesson, Quiz, UserProfile
from django.urls import reverse_lazy
from django.http import JsonResponse

class IndexView(TemplateView):
    template_name = 'index.html'

class LanguageListView(ListView):
    model = Language
    template_name = 'language/language_list.html'

class LanguageDetailView(DetailView):
    model = Language
    template_name = 'language/language_detail.html'

    def get_object(self):
        name = self.kwargs.get("name")
        return get_object_or_404(Language, name=name)


class LessonListView(ListView):
    model = Lesson
    template_name = 'lesson/lesson_list.html'

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson/lesson_detail.html'


class QuizListView(ListView):
    model = Quiz    
    template_name = 'quiz/quiz_list.html'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile/userprofile_detail.html'

    def get_object(self):
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)
        return get_object_or_404(UserProfile, user=user)


def create_payment_intent(request):
    try:
        # Set up the payment
        intent = stripe.PaymentIntent.create(
            amount=1000,  # amount in cents
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'},
        )
        return JsonResponse({
            'client_secret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)})
