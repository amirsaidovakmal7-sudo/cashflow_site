from django.db import models
from location_field.models.plain import PlainLocationField

class Event(models.Model):
    event_name = models.CharField(max_length=128, verbose_name="Название мероприятия")
    event_date = models.TextField("Дата меоприятия")
    event_place_name = models.CharField(max_length=64, verbose_name='Название места', default='')
    event_location = models.URLField('Вставьте ссылку')
    event_age_min = models.CharField(max_length=8, verbose_name='Минимальный возраст участника')
    event_age_max = models.CharField(max_length=8, verbose_name='Минимальный возраст участника')
    event_amount = models.CharField(max_length=8, verbose_name='Свободно мест', default='0/9')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.event_name




class Team(models.Model):
    worker_image = models.ImageField(upload_to='media', verbose_name='Фото сотрудника')
    worker_name = models.CharField(max_length=64, verbose_name='Имя сотрудника')
    worker_description = models.TextField('Описание сотрудника')
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    def __str__(self):
        return self.worker_name

class BrandLogo(models.Model):
    brand_name = models.CharField(max_length=128,  default='BrandName', verbose_name='Имя бренда')
    brand_image = models.ImageField(upload_to='media', verbose_name='Лого бренда')
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand_name



class GamesCategory(models.Model):
    category_name = models.CharField(max_length=32, verbose_name='Название категории')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Games(models.Model):
    game_name = models.CharField(max_length=32, verbose_name='Название тренинга')
    game_sub_name = models.TextField('Подзаголовок для тренинга')
    game_desc = models.TextField('Описание тренинга')
    game_skills = models.TextField('Получаемые навыки')
    game_category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    game_photo1 = models.ImageField(upload_to='media', default='', verbose_name='Фото тренинга')
    game_photo2 = models.ImageField(upload_to='media', default='', verbose_name='Фото тренинга')
    game_photo3 = models.ImageField(upload_to='media', default='', verbose_name='Фото тренинга')
    game_photo4 = models.ImageField(upload_to='media', default='', verbose_name='Фото тренинга')
    game_photo5 = models.ImageField(upload_to='media', default='', verbose_name='Фото тренинга')
    class Meta:
        verbose_name = 'Тренинг'
        verbose_name_plural = 'Тренинги'

    def __str__(self):
        return self.game_name





