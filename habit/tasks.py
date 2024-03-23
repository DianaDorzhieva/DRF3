from celery import shared_task
from django.core.mail import send_mail
from config import settings
from habit.models import Habit
from users.models import User


@shared_task
def send_message_about_habit():
    habit = Habit.objects.all()

