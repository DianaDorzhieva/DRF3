from django.core.management import BaseCommand

from habit.models import Habit
from users.services import MyBot


class Command(BaseCommand):

    def handle(self, *args, **options):
        habits = Habit.objects.all()
        my_bot = MyBot()
        my_bot.send_message('Привет! Не забудь про привычку')
