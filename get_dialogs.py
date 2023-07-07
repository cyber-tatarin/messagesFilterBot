import asyncio
import sys

from telethon import TelegramClient, sync, events
import re
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

client = sync.TelegramClient('session_name', api_id, api_hash)
client.start()


def run():
    # print('we are in')
    # group = client.get_entity('Тест бота медиапати')
    # mktwt = client.get_entity('MarketTwits')
    # entity = client.get_entity(-1001745883901)
    # print(entity)
    
    dialogs = client.get_dialogs()
    dialogs = [(i, x.name, x.id) for i, x in enumerate(dialogs)]
    dialogs = tuple(dialogs)
    
    with open('chats.txt', 'w', encoding='utf-8') as file:
        for dialog in dialogs:
            print(dialog, '\n\n')
            # try:
            text = f'({dialog[0]}, {dialog[1]}, {dialog[2]})\n\n'
            # except UnicodeEncodeError:
            #     text = f"{dialog[0]}, {dialog[2]}"
            
            file.write(text)


if __name__ == '__main__':
    run()



