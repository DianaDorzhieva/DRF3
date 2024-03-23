from rest_framework import status
from rest_framework.test import APITestCase
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana@mail.ru",
            FIO="Diana",
            password="123",
            pk=2
        )
        self.client.force_authenticate(user=self.user)

    def test_list_habit(self):
        """Тестирование вывода списка привычек"""
        responce = self.client.get('/habit/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        """Тестирование создания привычек"""
        data = {"name": "Test"}
        responce = self.client.post('/habit/create/', data=data)
        self.assertEquals(responce.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_update_habit(self):
        """Тестирование изменения привычек """
        habit = Habit.objects.create(name="Test3", time_to_complete=119, user=self.user)
        responce = self.client.patch(f'/habit/update/{habit.id}/', {'name': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """Тестирование удаления привычек """
        habit = Habit.objects.create(name="Test", user=self.user)
        responce = self.client.delete(f'/habit/delete/{habit.id}/')
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)
