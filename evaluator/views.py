from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .services import EvaluatorService
from django.http import JsonResponse
import json

# Create your views here.
@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    word = data.get("title")
    meaning = data.get("content")
    student_answer = data.get("answer")

    evaluation = EvaluatorService.check_answer({word:word, meaning:meaning}, student_answer)

    return JsonResponse(evaluation, safe=False)

@csrf_exempt
def check_sentence(request):
    data = json.loads(request.body)
    word = data.get("title")
    meaning = data.get("content")
    sentence = data.get("answer")

    evaluation = EvaluatorService.check_sentence({word:word, meaning:meaning}, sentence)
    
    return JsonResponse(evaluation)