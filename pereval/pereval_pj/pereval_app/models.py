from django.db import models
from django.utils import timezone


class Level(models.Model):
    level_1 = '1А'
    level_2 = '1Б'
    level_3 = '2А'
    level_4 = '2Б'
    level_5 = '3А'
    level_6 = '3Б'

    LEVEL = {
        (level_1, '1А'),
        (level_2, '1Б'),
        (level_3, '2А'),
        (level_4, '2Б'),
        (level_5, '3А'),
        (level_6, '3Б'),
    }

    winter = models.CharField(max_length=2, choices=LEVEL, default=level_1)
    summer = models.CharField(max_length=2, choices=LEVEL, default=level_1)
    autumn = models.CharField(max_length=2, choices=LEVEL, default=level_1)
    spring = models.CharField(max_length=2, choices=LEVEL, default=level_1)


class Users(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Added(models.Model):
    new = 'N'
    pending = 'P'
    accepted = 'A'
    rejected = 'R'

    STATUS = [
        (new, 'Новое'),
        (pending, 'В работе'),
        (accepted, 'Принято'),
        (rejected, 'Не принято'),
    ]

    walk = '01'
    ski = '02'
    catamaran = '03'
    kayak = '04'
    raft = '05'
    rafting = '06'
    bicycle = '07'
    car = '08'
    bike = '09'
    sail = '10'
    ride = '11'

    ACT = [
        (walk, 'Пешком'),
        (ski, 'Лыжи'),
        (catamaran, 'Катамаран'),
        (kayak, 'Байдарка'),
        (raft, 'Плот'),
        (rafting, 'Cплав'),
        (bicycle, 'Велосипед'),
        (car, 'Автомобиль'),
        (bike, 'Мотоцикл'),
        (sail, 'Парус'),
        (ride, 'верхом')
    ]

    beautyTitle = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.CharField(max_length=100)
    add_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    activities_types = models.CharField(max_length=2, choices=ACT, default=walk)
    status = models.CharField(max_length=1, choices=STATUS, default=new)


class Images(models.Model):
    add = models.ForeignKey(Added, on_delete=models.CASCADE, related_name='images')
    title_img = models.CharField(max_length=100)
    data = models.URLField(blank=True)
