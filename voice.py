from os import system
import time

try:
	from pyrogram import Client, filters
except ModuleNotFoundError:
	system('pip install pyrogram')

try:
	import gtts
except ModuleNotFoundError:
	system('pip install gtts')
	
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

app = Client("my_account", api_id=1582033, api_hash="d8a9ec6ca042b6391baa12d13ded42d2")


@app.on_message(filters.command("сек", prefixes="."))
def timer(_, msg):
	orig_text = msg.text.split(".сек ", maxsplit=1)[1]
	msgg = msg
	try:
		t = int(orig_text)
	except:
		t = 60
	
	i = t
	clok = '⌛️'
	if msg.chat.type == 'private' or msg.outgoing:
		msg.delete()
		reply = False
	else:
		reply = True
	
	if reply:
		msg = msg.reply('Запуск таймера')
	else:
		msg = app.send_message(msg.chat.id, 'Запуск таймера…')
	while i >= 0:
		try:
			msg.edit(clok + ' | Запущен таймер: ' + str(i) +'/' + str(t))
		except FloodWait as e:
			sleep(e.x)
			i -= e.x
		i -= 1
		if clok == '⌛️':
			clok = '⏳'
		else:
			clok = '⌛️'
		sleep(1)
			
	msgg.reply('⏲ | ' + str(t) + ' сек. вышло!')
	

@app.on_message(filters.command("т", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".т ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "✍️"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
 
            tbp = tbp + text[0]
            text = text[1:]
            msg.edit(tbp)
            #sleep(random.uniform(0, 1))
        except FloodWait as e:
            sleep(e.x)
 
# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")
 
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
	

@app.on_message(filters.command("с", prefixes="."))
def tts(_, msg):
	name = msg.from_user.username
	if msg.chat.type == 'private' or msg.outgoing:
		msg.delete()
		reply = False
	else:
		reply = True
	text_tos = msg.text.split(".с ", maxsplit=1)[1]
	if msg.reply_to_message != None:
		msg = msg.reply_to_message
		reply = True
	try:
		lng = text_tos.split("-l ", maxsplit=1)[1].split(' ', maxsplit = 1)[0]
		
		if lng == '' or lng == ' ':
			lng = 'ru'
	except Exception as e:
		print(e)
#		app.send_message(msg.from_user.username, '[Вот](https://ru.m.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2) коды языков, стыдно их не знать!\n' + str(e))
		lng = 'ru'
	
	audio_file = str(name).replace('None', 'Кто-то') + ' (' + str(time.time()) + ') - by NIKDISSV.mp3'
	if text_tos.find('-slow') != -1:
		slow = True
	else:
		slow = False
	text_tos = text_tos.replace(lng, '').replace('-slow', '').replace('-l', '')
	print('Текст: %s\nЯзык: %s\n Медлянный режим: %s' %(text_tos, lng, str(slow)))
	tts = gtts.gTTS(text = text_tos, lang = lng, slow = slow)
	tts.save(audio_file)
	if reply:
		msg.reply_audio(audio_file)
	else:
		app.send_audio(msg.chat.id, audio_file)
	system('rm *.mp3')

while 1:
	app.run()