from django.shortcuts import render
from django.http import JsonResponse

from .services import WordService

def add_word(request):
    word = request.GET.get("word")
    meaning = request.GET.get("meaning")
    
    obj = WordService.add_word(word, meaning)

    return JsonResponse({
        "word":obj.word,
        "meaning":obj.meaning
    })

def list_words(request):
    words = WordService.get_words()

    data = [{"word":w.word, "meaining":w.meaning} for w in words]

    return JsonResponse(data, safe=False)
