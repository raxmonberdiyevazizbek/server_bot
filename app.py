# from telegram.ext import Updater , Filters , CommandHandler
# import os
# from name import start


# # TOKEN=os.environ.get("6806178452:AAHwxFmry9CVNlCXP-1IhKHMR3MyGDFEBgM")

# def main():
#     # updater obj
#     updater = Updater(token="6806178452:AAHwxFmry9CVNlCXP-1IhKHMR3MyGDFEBgM")

#     # dispetcher obj
#     dp = updater.dispatcher

#     # handlers
#     dp.add_handler(CommandHandler(['start', 'boshlash'], start))
    

#     # polling started
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()


import requests
from pprint import pprint
TOKEN="6806178452:AAHwxFmry9CVNlCXP-1IhKHMR3MyGDFEBgM"

from time import sleep

base_url = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    update = requests.get(f"{base_url}/getUpdates")
    data = update.json()
    return data['result']

def send_message(chat_id, text):
    parameters = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    r = requests.get(f"{base_url}/sendMessage", params=parameters)
    return r.json()


last_message_id = -1

while True:
    msgs = get_updates()
    last_msg = msgs[-1]
    # print(last_msg)
    
    message_id = last_msg['message']['message_id']

    chat_id = last_msg['message']['chat']['id']
    text = last_msg['message']['text']

    print(last_message_id, message_id)

    if last_message_id != message_id:
        
        if text == '/start':
            
            send_message(chat_id, "Welcome to Echo Bot!")
        else:
            send_message(chat_id, text)

        last_message_id = message_id
    
    sleep(2)