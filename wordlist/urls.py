from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_word),
    path("view/", views.list_words),
    path("edit/", views.edit_word),
    path("get-by-pk/", views.get_word),
    path("get-question-list/", views.get_questions)
]