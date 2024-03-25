from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    choice_periodicity = [
        (1, 'раз в неделю'),
        (2, 'два раза в  неделю'),
        (3, 'три раза в неделю'),
        (4, 'четыре раза в неделю'),
        (5, 'пять раз в неделю'),
        (6, 'шесть раз в неделю'),
        (7, 'ежедневно')

    ]

    name = models.CharField(max_length=50, verbose_name='название привычки')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время,когда необходимо выполнять привычку', **NULLABLE)
    action = models.CharField(max_length=1000, verbose_name='действие', **NULLABLE)
    is_habit_good = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    habit_related = models.ForeignKey('Habit', verbose_name='связанная привычка', on_delete=models.SET_NULL, **NULLABLE)
    periodicity = models.IntegerField(verbose_name='переодичность', choices=choice_periodicity, default=7)
    reward = models.CharField(max_length=50, verbose_name='вознагрождение', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')
    time_to_complete = models.IntegerField(default=1, verbose_name='время на выполнение в секундах')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
