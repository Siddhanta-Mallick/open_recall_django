from django.urls import path
from . import views 

urlpatterns = [
    path('check-answer/', views.check_answer),
    path('check-sentence/', views.check_sentence)
]