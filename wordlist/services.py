from .models import WordList
import random

class Scheduler :
    @staticmethod
    def randomScheduler(available_pks, count=10):
        total_questions = min(count, len(available_pks))

        if total_questions == 0:
            return []
        
        selected_questions = random.sample(available_pks, total_questions)
        return selected_questions

class WordService :

    @staticmethod
    def add_word(word, meaning) :
        return WordList.objects.create(word=word, meaning=meaning)

    @staticmethod
    def get_words(limit=100):
        return WordList.objects.all()[:limit]
    
    def get_word_by_pk(pk):
        try:
            entry =  WordList.objects.get(pk=pk)
            return entry
        except Entry.DoesNotExist :
            print("Entry does not exist!")
    
    @staticmethod
    def get_question_list(scheduler="random"):
        questions = []
        
        match scheduler :
            case "random":
                valid_pks = list(WordList.objects.values_list('pk', flat=True)) 
                randomized_pks = Scheduler.randomScheduler(valid_pks, 10)
                sorted_questions = list(WordList.objects.filter(pk__in=randomized_pks))

                question_map = {q.pk:q for q in sorted_questions}

                questions = [question_map[pk] for pk in randomized_pks if pk in question_map]

            case "spaced_repition" :
                pass
            case _:
                print(f"Warning: Unknown scheduler '{scheduler}'. Returning empty list.")
        return questions