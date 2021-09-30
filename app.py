from Adafruit_IO import Client
import os

x = os.getenv('ADAFRUIT_IO_USERNAME')
y = os.getenv('ADAFRUIT_IO_KEY')
z = os.getenv('TOKEN')

aio = Client(x, y)
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned on')

def demo2(bot,update):
  aio.send('light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned off') 

def demo3(bot,update):
  aio.send('fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')

def demo4(bot,update):
  aio.send('fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on light":
    demo1(bot,update)
  elif a =="turn off light":
    demo2(bot,update)
  elif a =="turn on fan":
    demo3(bot,update)
  elif a =="turn off fan":
    demo4(bot,update)
    

u = Updater(z,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
