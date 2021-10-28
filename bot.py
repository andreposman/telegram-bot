import os
import re
import telebot
import logging
import json
import yfinance as yf
import securities
import commands
import utils.validate
import utils.messages
import utils.calculate
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)
bot = telebot.TeleBot(os.environ["API_KEY"])


def handleETF(message, bot, data):
  if data.info['quoteType'] == 'ETF':
    print("-----------------------------------------")
    print("ETF")
    print("-----------------------------------------")

    if not utils.validate.data_has_price(data):
      replyMsg = utils.messages.market_data(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleEquity(message, bot, data):
  if data.info['quoteType'] == 'EQUITY':
    print("-----------------------------------------")
    print("STOCK")
    print("-----------------------------------------")

    if not utils.validate.data_has_price(data):
      replyMsg = utils.messages.market_data(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleCrypto(message, bot, data):
  if data.info['quoteType'] == 'CRYPTOCURRENCY':
    print("-----------------------------------------")
    print("CRYPTO")
    print("-----------------------------------------")

    if not utils.validate.data_has_price(data):
      replyMsg = utils.messages.market_data(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleCurrency(message, bot, data):
  if data.info['quoteType'] == 'CURRENCY':
    print("-----------------------------------------")
    print("CURRENCY")
    print("-----------------------------------------")

    if not utils.validate.data_has_price(data):
      replyMsg = utils.messages.market_data(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')


def run_bot(bot):
  commands.helper(bot)
  commands.greet(bot)
  commands.fetch_bot(bot)  

  bot.infinity_polling()
  

def main():
    while True:
        try:
            run_bot(bot)
        except Exception as e:
            print(e)
            if message.from_user.username == 'andreposman':
              bot.reply_to(message, f'Error: {e}')
        else:
            commands.stop_bot(bot, os.environ["ENV"])
            break
            

if __name__ == "__main__":
  main()