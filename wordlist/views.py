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

    data = [{"pk":w.pk, "word":w.word, "meaning":w.meaning} for w in words]

    return JsonResponse(data, safe=False)

def get_word(request):

    pk_fetch = request.GET['pk']
    word = WordService.get_word_by_pk(pk_fetch)

    return  JsonResponse({'pk':word.pk , 'word':word.word, 'meaning':word.meaning}, safe=False) 

@csrf_exempt
def edit_word(request):

    data = json.loads(request.body)
    
    pk_edit = data.get("pk")
    word = data.get("title")
    meaning = data.get("content")

    word_to_edit = WordService.get_word_by_pk(pk_edit)
    word_to_edit.word = word
    word_to_edit.meaning = meaning

    word_to_edit.save()

    return JsonResponse({'status':'updated word'})