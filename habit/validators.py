from rest_framework.serializers import ValidationError


class Check_habit:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_habit_good = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        habit_related = dict(value).get(self.field3)
        if habit_related and reward:
            raise ValidationError('Нельзя использовать связанную привычку и вознагрождение')
        if habit_related and not habit_related.is_habit_good:
            raise ValidationError('В связанные привычки можно добавлять привычки только с признаком приятной')
        if (is_habit_good and reward) or (is_habit_good and habit_related):
            raise ValidationError('У приятной привычки не может быть вознагрождения или связанной привычки')


class Check_time:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = dict(value).get(self.field)
        if time_to_complete and time_to_complete > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд')
