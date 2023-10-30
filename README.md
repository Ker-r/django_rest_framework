# django_rest_framework
Данный проект является API для учебного сайта animals, где можно создать свои посты по двум разным категориям. 
В данном проекте много закомментированного кода для того, чтобы можно было посмотреть стадии развития проекта и
понимать, какие бывают подходы к созданию API.  

### Технологический Стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)

## Установить venv 
``` python3.9 -m venv venv ```

## Активировать venv 
``` source venv/bin/activate ```

## Обновить менеджер пакетов pip 
``` python3 -m pip install --upgrade pip ```

## Установить все зависимости из requirements 
``` pip install -r requirements.txt ```

## Создать миграции
``` python manage.py makemigrations ```

## Применить миграции
``` python manage.py migrate ```

## Создать суперюзера
``` python manage.py createsuperuser ```

## Запустить проект 
``` python3 manage.py runserver ```


### Доступ к админке
Доступ к админке предоставляется по адресу `admin/`

### Адрес API
Адрес API - `api/v1/animal`. По данному адресу в браузере можно получить GET запрос на список всех записей, а также реализовать POST запрос для создания новой записи. По данному адресу все запросы можно реализовать через Postman. 

### Создание нового пользователя
Для регистрации перейдите по ссылке `api/v1/authusers/` в браузере. Здесь вы можете ввести свои данные и выполнить POST запрос для создания нового пользователя. 

### Для создания нового пользователя через Postman.
Вводим адрес `api/v1/auth/users/` и выбираем POST запрос
В графе Body выбираем form-data
Ключи: username, password, email

### Для авторизации по токену через Postman.
Вводим адрес `auth/token/login/` и выбираем POST запрос
В графе Body выбираем form-data
Ключи: username, password такие же как при создание пользователя.
Система возвращает токен с помощью которого в дальнейшем будет производиться аутентификация пользователя.

### Для авторизации для отправки GET запроса на адресу конкретной страницы через Postman.
Вводим адрес `api/v1/animal/1/` и выбираем GET запрос. 
В графе Headers отмечаем графу Authorization и прописываем в нее токен. Прописываем: Token и через пробел указываем токен. Как получить токен, описано в блоке выше. 

### Для выхода из системы через Postman.
Вводим адрес `auth/token/login/` и выбираем POST запрос
В графе Headers отмечаем графу Authorization и прописываем в нее токен. Прописываем: Token и через пробел указываем токен. Авторизоваться по этому токену уже не получиться. Нужно заново получить токен. 

### JWT-токен. Для предоставления доступа по access токену к определенной странице через POSTMAN.
### На данный момент JWT-токен закомментирован. Для работы с ним, необходимо закомментировать url "api/v1/drf-auth".
Через GET запрос по адресу `api/v1/token/` необходимо ввести свой логин и пароль. Далее вам будет предоставлено 2 токена: refresh и access. Необходимо копировать второй токен. 
Через приложение Postman, выполните запрос на определенную страницу, например, `api/v1/animal/1/`. В графе Headers отмечаем графу Authorization и прописываем в нее токен следующим образом: Bearer пробел и скопированный токен. Отправляем GET запрос. 
'Bearer' - это ключевое слово, указанное в settings "AUTH_HEADER_TYPES" в SIMPLE_JWT.

### Доступ к данным предоставлен только авторизованным пользователям по умолчанию. 

[Документация по JWT токенам](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)

[Документация по Django Rest Framework](https://www.django-rest-framework.org/)\



Автор: Ефремова Каролина