Дорогой пользователь,

Перед тобою – модуль токенизации текста для python. 

***Описание модуля***

Модуль представляет собой простой токенизатор, который может, прибегая к помощи 3 библиотек: Regex, NLTK и spaCy, – токенизировать текст по пробелам, знакам препинания и предложениям

***Инструкция по установке***

Чтобы пользоваться модулем, тебе необходимо создать виртуальную среду и установить библиотеки из файла requirements.txt. Для этого – последовательно скопируй команды в терминал:

(1) python -m venv tokenizer_env #создает виртуальное окружение
(2) source tokenizer_env/bin/activate  #активирует виртуальное окружение
(3) pip install -r requirements.txt #устанавливает библиотеки
(4) python3 -m spacy download en_core_web_sm #скачивает данные для spaCy

Теперь можешь пользоваться модулем.

***Тестирование модуля***

Чтобы протестировать модуль, скопируй в терминал команду (3). Ты запустишь демо-программу.

(3) python3 demo.py

Демо-программа включает в себя небольшой пользовательский интерфейс со списком команд – ты можешь токенизировать предложенный мною текст, вставить свой текст для токенизации или завершить программу.

***Инструкция по использованию***

Чтобы пользоваться функционалом модуля самостоятельно, импортируй его

    from tokenizer import TextTokenizer

И создай объект для токенизатора

    tokenizer = TextTokenizer

Модуль tokenizer.py может токенизировать текст несколькими способами:

1) С помощью функции split(). Возвращается список последовательностей символов, разделенных пробелом:

    tokenizer.tokenize_with_split(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: ['Hello,', 'world!', 'This', 'is', 'a', 'test', 'sentence.', 'How', 'are', 'you', 'today?']

2) С помощью библиотеки Regex. Возвращает список последовательностей символов, разделенных по пробелам и знакам препинания

    tokenizer.tokenize_with_re(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: ['Hello', 'world', 'This', 'is', 'a', 'test', 'sentence', 'How', 'are', 'you', 'today']

3) С помощью библиотеки NLTK:

    3.1) Возвращает список последовательностей символов, включает в себя знаки припинания как отдельный элемент списка

    tokenizer.tokenize_with_nltk_w(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?']

    3.2) Возвращает список предложений

    tokenizer.tokenize_with_nltk_s(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: ['Hello, world!', 'This is a test sentence.', 'How are you today?']

4) С помощью библиотеки spaCy: Возвращает список последовательностей символов, включает в себя знаки припинания как отдельный элемент списка

    tokenizer.tokenize_with_spacy(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?']

5) Всеми способами одновременно: Возвращает словарь в формате Метод_токенизации:Список 

    tokenizer.tokenize_all(Hello, world! This is a test sentence. How are you today?)

    #Пример выдачи: {'Токенизация по пробелам и знакам препинания с использованием Regex': ['Hello', 'world', 'This', 'is', 'a', 'test', 'sentence', 'How', 'are', 'you', 'today'], 'Простая токенизация по пробелам с использованием split()': ['Hello,', 'world!', 'This', 'is', 'a', 'test', 'sentence.', 'How', 'are', 'you', 'today?'], 'Токенизация по словам с использованием NLTK': ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?'], 'Токенизация по предложениям с использованием NLTK': ['Hello, world!', 'This is a test sentence.', 'How are you today?'], 'Токенизация с использованием spaCy': ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?']}