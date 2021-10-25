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

@bot.message_handler(commands=['greet'])
def greet_command(message):
  print(message)
  if message.from_user.username == 'andreposman':
    bot.reply_to(message, 'Olá Mestre, Vai Palmeiras!')

  elif message.from_user.username == 'raafvargas':
    bot.reply_to(message, f'👋 {message.from_user.first_name}, Spec em PHP!')

  elif message.from_user.first_name == 'Matheus Luis':
    bot.reply_to(message, f'👋 {message.from_user.first_name}, Rei do Spring!')

  else:
    bot.reply_to(message, f'Olá {message.from_user.first_name} 👋')

@bot.message_handler(commands=['help'])
def help_command(message):
  print(message)
  helpMsg = f"""
  Hi {message.from_user.first_name} 👋, this is how to use me, I have the following commands:

  /greet: I will say Hi to you
  /fetch: This is where the magic happens, 
    I will fetch USA Market data for the ticker that you send me:

      /fetch AAPL - fetch data for Apple stock
      /fetch VT - fetch data for the ETF VT
      /fetch BTC-USD - fetch data for Bitcoin
      /fetch USDBRL=X - fetch data for the FOREX pair USD/BRL    

  """
  bot.reply_to(message, helpMsg, parse_mode='Markdown')


def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]

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
  @bot.message_handler(commands=['fetch'])
  def fetch_command(message):
    asset = extract_arg(message.text)
    
    if len(sec) <=0:
      bot.reply_to(message, f"Yo {message.from_user.first_name}, you have to send me stock ticker. 🙄")

    for a in asset:
      data = yf.Ticker(a)
      print(data.info)

      if utils.validate.data_has_price(data):
        bot.reply_to(message, f"Yo {message.from_user.first_name}, I found no data available for {s}. 🤔")

      else:
        print('in handlers block')
        handleETF(message, bot, data)
        handleEquity(message, bot, data)
        handleCrypto(message, bot, data)
        handleCurrency(message, bot, data)
        securities.handle_others(message, bot, data)



  bot.infinity_polling()

def main():
    while True:
        try:
            run_bot(bot)
        except Exception(e):
            print(e)
        else:
            commands.stop_bot(message, bot, os.environ["ENV"])
            break
            

if __name__ == "__main__":
  main()