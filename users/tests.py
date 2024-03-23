from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="Diana2@mail.ru",
            FIO="Diana",
            password="123",
            pk=3
        )
        self.client.force_authenticate(user=self.user)

    def test_list_user(self):
        """Тестирование вывода списка пользователей"""
        responce = self.client.get('/users/user/')
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """Тестирование изменения пользователя """
        user_ex = User.objects.create(email="Test3@mail.ru", password="12345")
        responce = self.client.patch(f'/users/user/update/{user_ex.id}/', {'FIO': 'change'})
        self.assertEquals(responce.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        """Тестирование удаления пользователя """
        user_ex = User.objects.create(email="Test@mail.ru", password="12345")
        responce = self.client.delete(f'/users/user/delete/{user_ex.id}/')
        self.assertEquals(responce.status_code, status.HTTP_204_NO_CONTENT)
