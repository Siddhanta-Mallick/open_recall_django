from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_word),
    path("view/", views.list_words)
]