
# Виртуальная стажировка
## API_pereval

ФСТР — организация, занимающаяся развитием и популяризацией спортивного туризма в России 
и руководящая проведением всероссийских соревнований в этом виде спорта.
На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.

После преодоления очередного перевала, турист заполняет отчёт в формате PDF 
и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает эту информацию, 
верифицирует, а затем вносит её в базу, которая ведётся в Google-таблице.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, 
а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, 
внесёнными другими.

ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, 
которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

***
Пользователь (турист) передает следующие данные:

+ почта (email) 
+ телефон (phone)
+ фамилия (fam)
+ имя (name)
+ отчество (otc)
+ заголовки (beautyTitle, title, other_titles)
+ координаты (coord)
+ уровень сложности (level)
+ тип активности (activities_types)
+ изображения (images)

***
Метод: POST
~~~
/submitData/added
~~~
принимает JSON, например:
```
{
    "beautyTitle": "BTitle_1",
    "title": "Title_1",
    "other_titles": "OTitle_1",
    "connect": "C_1",
    "add_time": "2024-01-01 01:01:01",
    "user": {
        "email": "test_1@example.com",
        "phone": "11111111111",
        "fam": "Fam_1",
        "name": "Name_1",
        "otc": "Otc_1"
    },
    "coord": {
        "latitude": 11.01,
        "longitude": 11.01,
        "height": 1111
    },
    "level": {
        "winter": "1А",
        "summer": "1А",
        "autumn": "1А",
        "spring": "1А"
    },
    "activities_types": "01",
    "images": [
{
            "title_img": "Title_img_1",
            "data": "https://cdn.culture.ru/images/5517e3f2-4fdf-50c8-a025-23bec1a658b4"
        }
]
}
```

Результатом выполнения является Response с кодом __201__ (создание объекта _added_).  
Код __400__ — возвращается при отправке неверных данных.  
Код __500__ — возвращается при проблеме на стороне сервера.

***
После добавления новой информации,
сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле __status__, содержащее по умолчанию
значение:  
__new = 'N' — 'Новое'__.

Другие значения поля status:  
__pending = 'P' —  'В работе'__,  
__accepted = 'A' — 'Принято'__,  
__rejected = 'R' — 'Не принято'__.

***
Метод: GET
~~~
/submitData/added/<id>
~~~

Выводит всю информацию об одной записи по ее id (Response с кодом __200__).   
Код __404__ — возвращается при отсутствии объекта с заданным id.

***
Метод: PATCH 
~~~
/submitData/added/<id>
~~~
Выполняет функцию редактирования объекта _added_. 
При этом, редактируемый объект должен находиться в статусе __new (status = 'N')__. 
Кроме того, ___запрещено редактировать информацию о пользователе.___

Результатом выполнения является Response,  
где __state: 1__, означает, что изменения сохранены, __message: 'Changes saved'__;  
__state: 0__ может возвращаться как при статусе, 
отличном от __new,  
message: 'Changes rejected. Status: (текущий статус объекта)'__,  
так и при других ошибках, __message: serializer.errors__.

***
Метод: GET 
~~~
/submitData/user__email=<email>
~~~
Для получения всех объектов _added_, созданных пользователем с указанным адресом почты.

***
### _Опубликовано на pythonanywhere.com._  
Ссылки:  
https://apipereval.pythonanywhere.com/api/submitData/  
https://apipereval.pythonanywhere.com/swagger/

***

### _Тесты:_

Name                                                                              | Stmts | Miss | Cover
--- | --- | --- | --- |
manage.py                                                                    | 11 | 2 | 82%  | 
pereval_app\__init__.py                                                      | 0  | 0 | 100% |
pereval_app\admin.py                                                         | 7  | 0 | 100% |
pereval_app\apps.py                                                          | 4  | 0 | 100% |
pereval_app\migrations\0001_initial.py                                       | 6  | 0 | 100% |
pereval_app\migrations\0002_alter_images_add_alter_level_autumn_and_more.py  | 5  | 0 | 100% |
pereval_app\migrations\0004_alter_level_autumn_alter_level_spring_and_more.py| 4  | 0 | 100% |
pereval_app\migrations\__init__.py                                           | 0  | 0 | 100% |
pereval_app\models.py                                                        | 56 | 0 | 100% |
pereval_app\serializers.py                                                   | 43 | 13|  70% |
pereval_app\swagger.py                                                       | 5  | 0 | 100% |
pereval_app\tests.py                                                         | 46 | 0 | 100% |
pereval_app\views.py                                                         | 38 | 9 |  76% |
pereval_pj\__init__.py                                                       | 0  | 0 | 100% |
pereval_pj\asgi.py                                                           | 4  | 4 |   0% |
pereval_pj\settings.py                                                       | 26 | 0 | 100% |
pereval_pj\urls.py                                                           | 11 | 0 | 100% |
pereval_pj\wsgi.py                                                           | 4  | 4 |   0% |
TOTAL                                                                        | 275| 32|  88% |
