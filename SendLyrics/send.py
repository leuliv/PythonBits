from telethon import TelegramClient

api_id = "1423014"
api_hash = "f8bcf807bdf6e38aab1231a382f5a4de"

phone = "+251944228847"
session_file = 'leulw'

text_file = open("lyrics.txt", "r")
print(len(text_file.readlines()))

with TelegramClient(session_file, api_id, api_hash,
                        sequential_updates=True) as client:
    for line in text_file.readlines():
        client.loop.run_until_complete(client.send_message('i_trustmyself', line))

text_file.close()
