import os
from typing import List
import slack
from slack.errors import SlackApiError


class SlackBot:
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.client = slack.WebClient(token=self.bot_token)
        self.kacper_id = "U01ML8QFYT1"
        self.id_list = []

    def get_users_list(self, list_of_students: list) -> List:
        response = (self.client.users_list(token=self.bot_token))
        users_list = response.get('members')
        for user in users_list:
            user_name = user.get('real_name')
            if user_name in list_of_students:
                user_id = user.get("id")
                self.id_list.append(user_id)
        return self.id_list

    def send_message(self):
        for user in self.id_list:
            try:
                self.client.chat_postMessage(channel=user,
                                             text=f"Cześć! Ostatni call już za Tobą. Daj znać <@{self.kacper_id}>, jeżeli planujesz nie przedłużać abonamentu ",
                                             token=self.bot_token)

                self.client.chat_postMessage(channel=self.kacper_id,
                                             text=f"Hej Kacper! Wysłałem wiadomość przypominającą do <@{user}>. Pozdro! ",
                                             token=self.bot_token)

            except SlackApiError as e:
                assert e.response['error']
