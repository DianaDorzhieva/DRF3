from datetime import datetime
from celery import shared_task
from habit.models import Habit
from habit.services import create_message, create_bot_telegramm


@shared_task
def send_message_about_habit():
    now_time = datetime.now().time()
    habits = Habit.objects.all()
    for habit in habits:
        if now_time == habit.time:
            text = create_message(habit)
            chat_id = habit.user.chat_id
            create_bot_telegramm(chat_id, text)
