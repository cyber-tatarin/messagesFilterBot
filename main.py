from telethon import TelegramClient, sync, events, connection
import re
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
proxy_url = "http://proxy.server:"

proxy_address = 'http://proxy.server'
proxy_port = 3128
proxy_type = connection.ConnectionHttp

dialogs = (1, 2)
resend_chat_id = None


def execute_bot():
    client = sync.TelegramClient('session_name', api_id, api_hash, proxy=(proxy_address, proxy_port, proxy_type))
    client.start()

    resend_to_chat_id = client.get_entity(-916825551)
    group = client.get_entity('Тест бота медиапати')
    print(resend_to_chat_id)
    
    # @client.on(events.NewMessage(chats=(group, mktwt)))
    @client.on(events.NewMessage(chats=(group, )))
    async def normal_handler(event):
        print(event.message)
        if re.findall(r'#крипто', event.message.text):
            await client.forward_messages(entity=resend_to_chat_id, messages=[event.message], silent=False)
            await client.send_message('dimatatatarin', 'Message forwarded successfully!', silent=False)
        else:
            print('no crypto')
        print('done')
        
    client.run_until_disconnected()


if __name__ == '__main__':
    execute_bot()



