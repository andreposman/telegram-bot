import os
import re
import telebot
import logging
import json
import yfinance as yf
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

bot = telebot.TeleBot(os.environ["API_KEY"])

@bot.message_handler(commands=['start'])
def reply(message):
  print(message)
  if message.from_user.username == 'andreposman':
    bot.reply_to(message, 'Oi Mestre, Avanti Palestra!')

  elif message.username == 'raafvargas':
    bot.reply_to(message, f'Eai {message.first_name}, Rei do PHP!')

  elif message.username == 'Matheus':
    bot.reply_to(message, 'Eai {message.first_name}, Rei do Spring!')

  else:
    bot.reply_to(message, 'Olá {message.first_name}, Vai Palmeiras!')
  

def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]

def handleInput(data, message, stock):
  if data.info['regularMarketPrice'] == None:
    return True

def handleETF(message, bot, data):
  if data.info['quoteType'] == 'ETF':
    if data.info['regularMarketPrice'] != None:
      replyMsg = f"Hey {message.from_user.first_name}, {data.info['symbol']} current price is: ${data.info['regularMarketPrice']}"

      bot.reply_to(message, replyMsg)

def handleEquity(message, bot, data):
    if data.info['quoteType'] == 'EQUITY':
      if data.info['regularMarketPrice'] != None:
        print(json.dumps(data.info))
        price = data.info['currentPrice']
        replyMsg = f"Hey {message.from_user.first_name}, {data.info['symbol']} current price is: ${price}. 💵"

        bot.reply_to(message, replyMsg)

"""
def foo():
    while True:
        try:
            foo2()
        except:
            pass
        else:
            break
"""

def runBot(bot):
  @bot.message_handler(commands=['stock'])
  def get_stocks(message):
    stocks = extract_arg(message.text)
    if len(stocks) <=0:
      bot.reply_to(message, f"Yo {message.from_user.first_name}, you have to send me stock ticker. 🙄")

    for stock in stocks:
      data = yf.Ticker(stock)
      print(data.info)

      if handleInput(data, message, stock):
        bot.reply_to(message, f"Yo {message.from_user.first_name}, I found no data available for: {stock}. 🤔")

      else:
        handleETF(message, bot, data)
        handleEquity(message, bot, data)


  bot.polling()

def main():
    while True:
        try:
            runBot(bot)
        except:
            pass
        else:
            break

if __name__ == "__main__":
  main()