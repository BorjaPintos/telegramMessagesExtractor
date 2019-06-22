# -*- coding: utf-8 -*-
from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageMediaWebPage, WebPageEmpty

# You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = <TU API_ID>
api_hash = <TU API HASH>

client = TelegramClient('extractorApp', api_id, api_hash)
client.connect()

if not client.is_user_authorized():  # authorization (if there is no .session file created before)
  phone_number=input('Introduce número de teléfono con el prefijo de país (+34666666666):')
  client.send_code_request(phone_number)
  client.sign_in(phone_number, input('Entroduce el código que llega al telegram: '))

for message in client.iter_messages(input('Pon el nombre del chat o canal:'), search=input('¿Qué quieres buscar?'), reverse=True):
  obj = {}
  obj["id"] = message.id
  obj["date"] = str(message.date)
  obj["message"] = message.message
  if (type(message.media) is MessageMediaWebPage):
    obj["type"] = "web"
    obj["web"] = {}
    try:
        if not type(message.media.webpage) is WebPageEmpty:
            obj["web"]["description"] = message.media.webpage.description
    except:
        print (message);
  print(obj);
