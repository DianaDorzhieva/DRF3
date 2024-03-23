from rest_framework import serializers
from habit.models import Habit
from habit.validators import Check_habit, Check_time


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [Check_habit(field1='is_habit_good', field2='reward', field3='habit_related'),
                      Check_time(field='time_to_complete')]
