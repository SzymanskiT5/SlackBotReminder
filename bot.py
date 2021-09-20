import slack
from slack.errors import SlackApiError
import os
BOT_TOKEN =
SLACK_TOKEN =


class SlackBot:
    def __init__(self):
        self.bot_token = BOT_TOKEN
        self.slack_token = SLACK_TOKEN
        self.client = slack.WebClient(token = self.slack_token)


    def get_users_list(self):
        response = (self.client.users_list(token=BOT_TOKEN))
        users_list = response.get('members')
        print(users_list)
        for user in users_list:
            user_name = user.get('name')
            user_id = user.get("id")
            print(user_name)
            print(user_id)


    def send_message(self, channel):
        try:
            self.client.chat_postMessage(channel="U02E3T7JMMH",
                                    text="Cześć! Ostatni call już za Tobą. Daj znać @Kacper Garbaciński - Devs Mentoring, jeżeli planujesz nie przedłużać abonamentu ",
                                    token=self.bot_token)
        except SlackApiError as e:
            assert e.response['error']

