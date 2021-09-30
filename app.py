from Adafruit_IO import Client,Data
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def turnoffthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned off")
  send_value(0)

def turnonthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned on")
  send_value(1)

def send_value(value):
  feed = aio.feeds('Bedroom Light')
  aio.send_data(feed.key,value)
def input_message(update, context):
  text=update.message.text
  if text =="turnonthelight":
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned on")
  elif text =="turnoffthelight":
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bulb turned off")
  

  
def start(update, context):
  start_message='''
/turnoffthelight or 'turn off':To turn off the bulb ,sends value=0 in feed
/turnonthelight or 'turn on':To turn on the bulb ,sends value=1 in feed
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
TOKEN = os.getenv('TOKEN')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoffthelight',turnoffthelight))
dispatcher.add_handler(CommandHandler('turnonthelight',turnonthelight))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
