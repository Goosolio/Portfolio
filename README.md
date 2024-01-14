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

Имею опыт написания несложных Телеграм ботов с помощью библиотеки Telebot (например, регистратор на какое-либо мероприятие с сохранением данных при регистрации в отдельный файл), написания оконных приложений с помощью библиотеки Tkinter.

Сложность растёт от проекта к проекту.


## Проект 1

Работа с данными, используя только библиотеку Pandas.
Все манипуляции с данными и визуализация взяты оттуда.

Первичные данные берутся из файла в формате CSV (есть в директории проекта). 

В этом проекте рассматривается Биткоин с сентября 2014 по начало января 2023. Работа происходит с числовыми и временными данными.
Присутсвует генерация новой колонки на основании имеющихся данных.

Все комментарии к действиям есть в блокноте.


## Проект 2

Работа с данными, используя Pandas, Random и Plotly.

Первичные данные берутся из файла в формате CSV (есть в директории проекта).

В этом проекте посмотрим на индустрию видео игр в разрезе 4х регионов.
Осуществляется чистка данных, генерация данных, объединение данных и визуализация. Работа происходит с различными типами данных.

Все комментарии к действиям есть в блокноте.

На Гитхабе есть некоторые трудности с отражением интерактивных графиков Plotly в блокноте. Отобразил их отдельно внутри проекта для удобства.


## Проект 3

Работа с данными, используя Pandas, Seaborn и частично Matplotlib.

Первичные данные берутся из файла в формате CSV.
В этот раз Датасет слишком большой, предлагаю скачать его по ссылке - [ссылка на файл](https://drive.google.com/file/d/1SKdjvP79gZw04JGghFxAHTkdpzk4s2t4/view)

Датасет более чем на 350 000 записей, в котором находятся различные данные про автомобили, продающиеся на вторичном рынке Германии. Проще говоря, объявления о продаже.
В проекте реализуется детальная чистка, так как в файле масса аномалий, корректировка данных, генерация дополнительных данных, группировки данных и масса визуализаций.
За визуализацию в этот раз, по большей части, отвечает библиотека Seaborn с небольшой помощью Matplotlib. Показатели интерпритируются в различных разрезах.

Все комментарии к действиям есть в блокноте.


## Проект 4

Работа с данными, используя Pandas, Matplotlib и частично Plotly.

Первичные данные берутся на сайте Федерального Резерва Сент Луиса через их API, который можно получить бесплатно у них на сайте.
Все подробности и ссылки указаны в файле, но ссылки я продублирую.
Происходит сбор, чистка, преобразование, объединение и визуализация данных.
Основное направление исследования, это оценка влияния работающего и активно ищущего работу населения на уровень безработицы по каждому штату США с визуализацией.

[FRED](https://fred.stlouisfed.org/)

[Python API for Federal Reserve Economic Data](https://pypi.org/project/fredapi/)

Все комментарии к действиям есть в блокноте.

На Гитхабе есть некоторые трудности с отражением интерактивных графиков Plotly в блокноте. Отобразил график внутри проекта для удобства.


## Проект 5

В следующих 3х проектах так или иначе будет задействован SQL.
В этом проекте будут использоваться SQLite3, Random + Names + Datetime для генерации различных данных и TKinter для создания оконного приложения.

В этот раз все данные будут генерироваться на ходу. Задействуем все типы данных (строки, целые и дробные числа, даты).
Создадим базу на 2 таблицы для примера, далее сделаем к ней запросы через приложение и получим ответы с визуализацией данных.
Файл с базой данных отсутствует в папке с проектом, он создастся автоматически при первом запуске файла.
Первая таблица про торговый ассортимент магазина/приложения, вторая таблица про покупателей/пользователей магазина/приложения.
Примеры отработки приложения и запросов к одной из таблиц будут отражены в виде скриншотов в папке с проектом.

Все комментарии к действиям есть в блокноте.
