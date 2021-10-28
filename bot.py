import os
import telebot
import logging
import yfinance as yf
import securities
import commands
import utils.messages
import utils.calculate
from dotenv import load_dotenv
from pathlib import Path

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='%d-%m-%Y %H:%M:%S')  

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

bot = telebot.TeleBot(os.environ["API_KEY"])


def run_bot(bot):
  commands.greet_bot(bot)
  commands.helper_bot(bot)
  commands.fetch_bot(bot)  
  commands.stop_bot(bot, os.environ["ENV"])


  bot.infinity_polling()
  

def main():
    while True:
        try:
            run_bot(bot)
        except Exception as e:
            logging.critical("Error: ", e)
            if message.from_user.username == 'andreposman':
              bot.reply_to(message, f'Error: {e}')
        else:
            logging.critical("for some reason mysterious reason you are reading this")
            break
            

if __name__ == "__main__":
  main()
