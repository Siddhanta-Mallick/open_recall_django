from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import WordService

import json

@csrf_exempt
def add_word(request):
    data = json.loads(request.body)
    word = data.get("title")
    meaning = data.get("content")
    
    obj = WordService.add_word(word, meaning)

    return JsonResponse({
        "word":obj.word,
        "meaning":obj.meaning
    })

def list_words(request):
    words = WordService.get_words()

    data = [{"word":w.word, "meaning":w.meaning} for w in words]

    return JsonResponse(data, safe=False)
