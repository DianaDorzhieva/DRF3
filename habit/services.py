import json
from datetime import datetime, timedelta
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from config import settings
import requests


def create_interval(habit):
    # Создаем интервал для повтора

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )
    return schedule


def task_message(habit):
    # Создаем задачу для повторения

    PeriodicTask.objects.create(
        interval=create_interval(habit),
        name='Habit',
        task='habit.tasks.send_message_about_habit',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )


def create_message(habit):
    return f'Я буду {habit.action} в {habit.time} в {habit.place}'


def create_bot_telegramm(chat_id, text):
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TOKEN_TELEGRAM

    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }

    )
