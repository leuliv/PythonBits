from telethon import TelegramClient

#Get app_id and api_hash in the telegram api site
api_id = "app_id"
api_hash = "api_hash"

phone = "phone_number" #Your Phone Number here
session_file = 'session_name' #choose a unique session name

text_file = open("lyrics.txt", "r")
lines = text_file.readlines()
print(len(lines))
text_file.close()

with TelegramClient(session_file, api_id, api_hash,
                        sequential_updates=True) as client:
    for line in lines:
        client.loop.run_until_complete(client.send_message('reciever_uname', line)) #replace 'reciever_id' with recievers username 
