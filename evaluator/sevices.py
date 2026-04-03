from django.conf import settings
import json
import enum
import google.generativeai as genai
import typing_extensions as typing

API_KEY = settings.GEMINI_API_KEY
genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a vocabulary tutor that quizzes students on word meanings.
A student is given a word and asked to type its meaning.
Your job is to check if the student's answer matches with the actual word meaning or not.
Evaluate the answer and provide an observation.
"""

class EvaluationStatus(enum.Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"

class EvaluationResult(typing.TypedDict):
    evaluation: EvaluationStatus
    observation: str

class EvaluatorService:

    @staticmethod
    def check_answer(word, student_answer) :
        word['student-answer'] = student_answer
        word_string = json.dumps(word)

        model = genai.GenerativeModel(
            model_name='gemini-3-flash-preview',
            system_instruction=SYSTEM_PROMPT
        )

        response = model.generate_content(
            word_string,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=EvaluationResult, 
            ),
        )

        return json.loads(response.text)