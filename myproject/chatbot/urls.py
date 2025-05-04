from django.urls import path
from .views import handle_intent

urlpatterns = [
    path('intents/<str:intent>/', handle_intent),
]
