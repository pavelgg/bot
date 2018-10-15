import aiml
import time
import signal
import sys
import telegram
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text    
   
    bot.sendMessage(update.message.chat_id, text='Hola, soy Pepe!tu padre')



def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def chatter(bot, update):

    chat_id = update.message.chat_id
    message = update.message.text
    k = aiml.Kernel()
    k.learn("std-startup.xml")
    k.respond("helou")
    k.setBotPredicate("name", "Pepe")
    k.setBotPredicate("anyo_nacimiento", "2017")
    k.setBotPredicate("edad", str(date.today().year-2017) )
    k.setBotPredicate("botmaster", 'nosotros' )
    k.setBotPredicate("nombre_bot", 'tu papi' )
    k.setBotPredicate("birthday", '12/2/2017' )
    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    response = k.respond(message)
    bot.sendMessage(update.message.chat_id, text=response)    

def main():

    updater = Updater("AAF8D1GOEZRBbbNm0k1dGqAKtflM3uRX_QM")
  
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler (CommandHandler ( "help" , help ))
   
    dp.add_handler (MessageHandler (Filters.text, chatter))

    
    updater.start_polling()

 
    updater.idle()


if __name__ == '__main__':
    main()
