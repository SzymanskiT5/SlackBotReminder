from typing import List

import slack
from slack.errors import SlackApiError

BOT_TOKEN = "xoxb-1591793740982-2503927576400-Kk7j2xrQAKKwLpADfXQKvXyf"
SLACK_TOKEN = "xoxp-1591793740982-2479925633731-2480302224514-7fb52577608bd9ed4e381562deb41478"


class SlackBot:
    def __init__(self):
        self.bot_token = BOT_TOKEN
        self.slack_token = SLACK_TOKEN
        self.client = slack.WebClient(token = self.slack_token)


    def get_users_list(self, list_of_students:list) -> List:

        response = (self.client.users_list(token=BOT_TOKEN))
        users_list = response.get('members')
        list_of_id = []
        for user in users_list:
            user_name = user.get('real_name')
            if user_name in list_of_students:
                user_id = user.get("id")
                list_of_id.append(user_id)
        return list_of_id

    def send_message(self, users_list:list):
        for user in users_list:
            try:
                self.client.chat_postMessage(channel=user,
                                    text="Cześć! Ostatni call już za Tobą. Daj znać @Kacper Garbaciński - Devs Mentoring, jeżeli planujesz nie przedłużać abonamentu ",
                                    token=self.bot_token)
            except SlackApiError as e:
                assert e.response['error']

