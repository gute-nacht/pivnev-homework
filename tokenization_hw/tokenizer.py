"""
Модуль для токенизации текста: регулярные выражения, NLTK и spaCy
"""
#проверяем, установлены ли библиотеки
try:
    import re, nltk, spacy # пробуем импортировать
    print('\n\nНеобходимые библиотеки установлены\n\n')
#если какая-то из библиотек отсутсвует, пользователь получает инструкцию, как он может это исправить
except ImportError:
    print('\n\nКакая-то из библиотек отсутствует. Скопируйте команду (1), а затем команду (2) в терминал и перезапустите программу:\n\n(1) pip install -r requirements.txt\n\n(2) python3 -m spacy download en_core_web_sm\n\n')

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass
#токенизация текста через split()
    def tokenize_with_split(self, text):
        """
        Простая токенизация по пробелам 

        Args:
            text (str): Входной текст
        Returns:
            list: Список токенов
        """
        text_tok_split = text.split()
        return text_tok_split
#токенизация текста через регулярные выражения
    def tokenize_with_re(self, text):
        """
        Простая токенизация по знакам препинания с использованием регулярных выражений

        Args:
            text (str): Входной текст
        Returns:
            list: Список токенов
        """
        re_text_tok = re.findall(r'\w+', text)
        return re_text_tok
#пословная токенизация с NLTK
    def tokenize_with_nltk_w(self, text):
        """
        Токенизация по словам с использованием NLTK

        Args:
            text (str): Входной текст
        Returns:
            list: Список токенов или сообщение об ошибке
        """
        nltk.download('punkt')
        nltk.download('punkt_tab')

        from nltk.tokenize import word_tokenize
        nltk_text_tok_by_word = word_tokenize(text) 
        return nltk_text_tok_by_word
#токенизация с NLTK по предложениям
    def tokenize_with_nltk_s(selft, text):
        """
        Токенизация по предложениям с использованием NLTK

        Args:
            text (str): Входной текст
        Returns:
            list: Список токенов или сообщение об ошибке
        """
        nltk.download('punkt')
        nltk.download('punkt_tab')

        from nltk.tokenize import sent_tokenize
        nltk_text_tok_by_sentence = sent_tokenize(text)
        return nltk_text_tok_by_sentence
#токенизация со spaCy
    def tokenize_with_spacy(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст
        Returns:
            list: Список токенов или сообщение об ошибке
        """
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        spacy_text_tok = [t.text for t in doc]
        return spacy_text_tok
#токенизация всеми способами одновременно
    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации
        
        Args:
            text (str): Входной текст
        Returns:
            dict: Словарь с результатами всех методов
        """
        retok = self.tokenize_with_re(text)
        splittok = self.tokenize_with_split(text)
        nltkwtok = self.tokenize_with_nltk_w(text)
        nltkstok = self.tokenize_with_nltk_s(text)
        spacytok = self.tokenize_with_spacy(text)
    
        alltok = {
            'Токенизация по пробелам и знакам препинания с использованием Regex': retok,
            'Простая токенизация по пробелам с использованием split()': splittok,
            'Токенизация по словам с использованием NLTK': nltkwtok,
            'Токенизация по предложениям с использованием NLTK': nltkstok,
            'Токенизация с использованием spaCy': spacytok
        }
        return alltok


