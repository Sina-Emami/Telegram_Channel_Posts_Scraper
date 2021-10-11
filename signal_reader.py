from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputChannel, InputPeerChannel
from telethon.tl.functions.channels import JoinChannelRequest


def field_separator(field_str, separator):
    return field_str.split(separator)


class TelegramChannel:
    def __init__(self, api_id, api_hash, phone):
        self.api_hash = api_hash
        self.api_id = api_id
        self.phone = phone

        self.channel_id = 'channel id'
        self.access_hash = 'channel access hash'
        self.channel_username = 'channel name'

    def connect_telegram(self):
        """
        Try to connect to the telegram account
        :return:
        """
        print('try to connect telegram...')
        try:
            self.tele_client = TelegramClient(self.phone,
                                              self.api_id,
                                              self.api_hash)

            # connecting to server of telegram
            self.tele_client.start()
            if not self.tele_client.is_user_authorized():
                self.tele_client.send_code_request(phone)
                self.tele_client.sign_in(phone, input('Enter the code: '))
            print('connect:D')
        except:
            print("something went wrong")

    def join_channel(self):
        """
        Joined the channel
        :return:
        """
        channel_entity = InputPeerChannel(channel_id=self.channel_id,
                                          access_hash=self.access_hash)
        self.channel_info = self.tele_client.get_input_entity(channel_entity)

        self.tele_client(JoinChannelRequest(self.channel_info))

    def get_massages(self):
        all_message_list = []
        messages = self.tele_client.get_messages(self.channel_info,
                                                 limit=1, search='Total_No')
        for message in messages:

            message_string = message.message
            # print(message_string)

    def get_all_dialogs(self):
        """
        If you do not have the channel info like id and hash
        you can join the channel by your account and get the info by getting
        all the dialogs you have and search the channel name among  them
        :return:
        """
        t = self.tele_client.get_dialogs()
        for d in t:
            print(d.entity)


if __name__ == '__main__':
    # your telegram account information
    api_id = 'your account api-id'
    api_hash = "your account api-hash"
    phone = "your number"
    signal_reader = TelegramChannel(api_id, api_hash, phone)
    signal_reader.connect_telegram()
    signal_reader.join_channel()
    signal_reader.get_massages()
