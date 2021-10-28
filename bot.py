import os
import re
import telebot
import logging
import json
import yfinance as yf
import securities
import commands
import utils.messages
import utils.calculate
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
init_loggin(logging.DEBUG)

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
            break
            

if __name__ == "__main__":
  main()


def init_logging(level):
  logging.basicConfig(format='%(asctime)s %(message)s', level=level, datefmt='%d-%m-%Y %H:%M:%S')  