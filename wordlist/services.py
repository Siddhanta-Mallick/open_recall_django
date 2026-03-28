from .models import WordList

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