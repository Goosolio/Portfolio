# Портфолио

Greetings to everyone who looked at my portfolio! 
Unfortunately, this portfolio is designed for a certain circle of employers, so all information is currently only in Russian. Comments in English may appear in the future.

Приветствую всех, кто заглянул в моё портфолио.

Некоторое время назад заинтересовался темой аналитики данных и теперь я в гонке.
Здесь будут собраны различные работы, которые включают анализ, различную визуализацию (от графиков до Дэшборда) и секцию про SQL.
Всё реализовано с помощью языка программирования Python и различных библиотек.

Внутри каждого блокнота есть комментарии к действиям.
Сложность проектов увеличивается по нарастающей.

На данный момент мой стэк состоит из:
- Python
- Pandas
- Numpy
- Matplotlib
- SeaBorn
- Plotly
- Dash
- SQLite3
- Datetime

Имею опыт написания несложных Телеграм ботов с помощью библиотеки Telebot (например, регистратор на какое-либо мероприятие с сохранением данных при регистрации в отдельный файл), написания оконных приложений с помощью библиотеки Tkinter.

Сложность растёт от проекта к проекту.


## Проект 1

Работа с данными, используя только библиотеку Pandas.
Все манипуляции с данными и визуализация взяты оттуда.

Данные парсятся из файла в формате CSV (есть в директории проекта). 

В этом проекте рассматривается Биткоин с сентября 2014 по начало января 2024. Работа происходит с числовыми и временными данными.
Присутсвует генерация данных и визуализация.

Все комментарии к действиям есть в блокноте.


## Проект 2

Работа с данными, используя Pandas + Random и Plotly.

Данные парсятся из файла в формате CSV (есть в директории проекта). 

В этом проекте посмотрим на индустрию видео игр в разрезе 4х регионов.
Осуществляется чистка данных, генерация данных, объединение данных, анализ и визуализация. Работа происходит с различными типами данных.

Все комментарии к действиям есть в блокноте.



## Проект 3

Работа с данными, используя Pandas + Seaborn и частично Matplotlib.

Данные парсятся из файла в формате CSV (есть в директории проекта). 
В этот раз Датасет слишком большой, предлагаю скачать его по ссылке - [ссылка на файл](https://drive.google.com/file/d/1SKdjvP79gZw04JGghFxAHTkdpzk4s2t4/view)

Датасет более чем на 350 000 записей, в котором находятся различные данные про автомобили, продающиеся на вторичном рынке Германии. Проще говоря, объявления о продаже.
В проекте реализуется детальная чистка, так как в файле масса аномалий, корректировка данных, генерация дополнительных данных, группировки данных и масса визуализаций.
За визуализацию в этот раз, по большей части, отвечает библиотека Seaborn с небольшой помощью Matplotlib. Показатели интерпритируются в различных разрезах.

Все комментарии к действиям есть в блокноте.


## Проект 4

Работа с данными, используя Pandas + Matplotlib и частично Plotly.

Первичные данные берутся на сайте Федерального Резерва Сент Луиса через их API, доступ к которому можно получить бесплатно у них на сайте.
Все подробности и ссылки указаны в файле, но ссылки я продублирую.
Происходит сбор, чистка, преобразование, объединение и визуализация данных.
Основное направление исследования, это оценка влияния работающего и активно ищущего работу населения на уровень безработицы по каждому штату США с визуализацией.

[FRED](https://fred.stlouisfed.org/)

[Python API for Federal Reserve Economic Data](https://pypi.org/project/fredapi/)

Все комментарии к действиям есть в блокноте.


## Проект 5

В следующих 3х проектах так или иначе будет задействован SQL (MySQL).
В этом проекте будут использоваться SQLite3 + Random + Names + Datetime для генерации различных данных и TKinter для создания оконного приложения.

В этот раз все данные будут генерироваться на ходу. Задействуем все типы данных (строки, целые и дробные числа, даты).
Создадим базу на 2 таблицы для примера, далее сделаем к ней запросы через приложение и получим ответы с визуализацией данных.
Файл с базой данных отсутствует в папке с проектом, он создастся автоматически при первом запуске файла.
Первая таблица про торговый ассортимент магазина/приложения, вторая таблица про покупателей/пользователей магазина/приложения.
Примеры отработки приложения и запросов к одной из таблиц будут отражены в виде скриншотов в папке с проектом.

Все комментарии к действиям есть в блокноте.


## Проект 6


В этом проекте будут использоваться SQLite3 + Random + Names + Datetime + Pandas + Matplotlib + Seaborn + Dash + Plotly

### Часть 1

База данных (MySQL), которая создается в проекте, будет состоять из пяти таблиц, в которых будут связи: продукция, доп инфо по продукции, складские данные, пользователи и таблица продаж.
В ассортименте приложения/магазина по продаже мебели 100 товаров (более 10 брендов и 5 категорий товаров со случайной стоимостью), зарегистрированы 80 пользователей (фио, возраст, почта), продажи ведутся с начала 2020 по конец 2023 (100000 покупок).
Созданная база будет использоваться для аналитики, построения таблиц и графиков в различных разрезах.

Сама база есть в директории проекта, но вы можете создать её по новой, просто запустив блокнот.
Данная база будет использоваться для следующего проекта.

Все комментарии к действиям есть в блокноте.


### Часть 2

Пример дэшборда.

Реализовано вэб приложение, которое взаимодействует с ранее созданной базой данных. На всякий случай, дублирую файл базы данных в папке проекта.
Происходит подключение к базе (MySQL), сбор данных, формирование дата фрейма и построение дэшборда на его основании.

В проекте реализованы следующие виджеты:
- чеклист
- рэнджслайдер
- 3 вида графиков

На данный момент не могу разместить данное приложение в интернете.

Все комментарии к действиям есть в блокноте.


## Проект 7

В этом проекте будут использоваться  Pandas + Numpy + Datetime + Dash + Plotly

### Часть 1

Данные парсятся из файла в формате CSV (есть в директории проекта).
Анализируются показатели Яндекс Музыки.
В этой части происходит чистка, преобразование и генерация доп данных.
Дополнительно подготавливаются заготовки для постороения дэшборда.

Для примера будет взята Москва.
По итогам действий будет сохранён новый файл в формате CSV, который будет использован во второй части проекта (output.csv).

Все комментарии к действиям есть в блокноте.


### Часть 2

Пример дэшборда.

Реализовано вэб приложение, которое взаимодействует с ранее созданным файлом в формате CSV. На всякий случай, дублирую файл в папке проекта.

Дэшборд работает в разрезе 5 крупнейших город РФ и одной недели.
1ый график будет зависеть от 1го параметра, отражает показатели в выбраном городе за неделю.
2ой и 3ий от 2х параметров, отражают показатели в выбраном городе за сутки.

В проекте реализованы следующие виджеты:
- выпадающие списки, от которых зависят графики
- графики

На данный момент не могу разместить данное приложение в интернете.

Все комментарии к действиям есть в блокноте.

