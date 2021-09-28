from Adafruit_IO import Client
import os

x= os.getenv('Username')
y= os.getenv('Key')

aio = Client(x, y)
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('Light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned on')

def demo2(bot,update):
  aio.send('Light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned off') 

def demo3(bot,update):
  aio.send('Fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')

def demo4(bot,update):
  aio.send('Fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')

def main(bot,update):
  a= bot.message.text
  if a =="Turn on light":
    demo1(bot,update)
  elif a =="Turn off light":
    demo2(bot,update)
  elif a =="Turn on fan":
    demo3(bot,update)
  elif a =="Turn off fan":
    demo4(bot,update)

bot_token = '2010152547:AAHxbqmoPad-araEtG6TP6YbF99-11gXzFk'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
