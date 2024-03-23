from config import settings
import requests


class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TOKEN_TELEGRAM

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '1089245849',
                'text': text
            }

        )
