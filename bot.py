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
  bot.reply_to(message, 'Vai Palmeiras')


def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]

def handleEtf(message, bot, data):
  if data.info['quoteType'] == 'ETF':
    if data.info['regularMarketPrice'] != None:
      print(json.dumps(data.info))
      # price = data.info['regularMarketPrice']
      replyMsg = f"{data.info['symbol']} current price is: ${data.info['regularMarketPrice']}"

      bot.reply_to(message, replyMsg)

def handleEquity(message, bot, data):
    if data.info['quoteType'] == 'EQUITY':
      if data.info['regularMarketPrice'] != None:
        print(json.dumps(data.info))
        price = data.info['currentPrice']
        replyMsg = f"{data.info['symbol']} current price is: ${price}"

        bot.reply_to(message, replyMsg)

@bot.message_handler(commands=['stock'])
def get_stocks(message):
  stocks = extract_arg(message.text.upper())
  if len(stocks) <=0:
    bot.reply_to(message, f"You have to type a stock ticker")

  for stock in stocks:
    data = yf.Ticker(stock)

    # if data.info['regularMarketPrice'] != None and data.info['regularMarketPrice'] != None:
    #   bot.reply_to(message, f"No data available for: {stock}")
    #   break

    handleEtf(message, bot, data)
    handleEquity(message, bot, data)


bot.polling()