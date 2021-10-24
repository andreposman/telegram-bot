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

@bot.message_handler(commands=['greet'])
def greet_command(message):
  print(message)
  if message.from_user.username == 'andreposman':
    bot.reply_to(message, 'Oi Mestre, Vai Palmeiras!')

  elif message.from_user.username == 'raafvargas':
    bot.reply_to(message, f'Eai {message.from_user.first_name}, Spec em PHP!')

  elif message.from_user.first_name == 'Matheus Luis':
    bot.reply_to(message, f'Eai {message.from_user.first_name}, Rei do Spring!')

  else:
    bot.reply_to(message, f'Olá {message.from_user.first_name} 👋')

@bot.message_handler(commands=['help'])
def help_command(message):
  helpMsg = """
  Hi {message.from_user.first_name} 👋, this is how to use me, I have the following commands:
  `/greet`: I will say Hi to you
  `/fetch`: This is where the magic happens, I will fetch US Market data for the ticker/symbol that you send me. 
    For example:
    
      `/fetch` AAPL - will make me fetch data for Apple stock
      `/fetch` VT - will make me fetch data for the ETF
      `/fetch` BTC-USD - will make me fetch data for Bitcoin
      `/fetch` USDBRL=X - will make me fetch data for the currency pair USD/BRL    

  """
  bot.reply_to(message, helpMsg, parse_mode='Markdown')



def calculatePerformance(data):
  closePrice = data.info['regularMarketPreviousClose']
  currentPrice = data.info['regularMarketPrice']
  performance = round((((currentPrice - closePrice)/currentPrice)*100), 2)

  return performance

def addPerformanceEmoji(performance):
  strPerformance = ''
  emojiSuffix = ''

  if performance < 0:
    emojiSuffix = '🔻'
    if performance < -10:
      emojiSuffix = '⚰️'

  elif performance > 0:
    strPerformance = ' +'
    emojiSuffix = '👍'
    if performance > 10: 
      emojiSuffix = '🚀💰'

  strPerformance = strPerformance + str(performance) + '% ' + emojiSuffix
  print(strPerformance)

  return strPerformance

def formatMessage(message, data):
  performance = calculatePerformance(data)
  strPerformance = addPerformanceEmoji(performance)
  specialMsg = ''

  if message.from_user.username == 'raafvargas':
    specialMsg = ' seu trouxa'

  if data.info['quoteType'] == 'EQUITY':
    r = f"""Hey {message.from_user.first_name} {specialMsg}, here is the data that I found for the company:\n\n*{data.info['longName']}*
----------------------------------------------
Sector:                 *{data.info['sector']}*
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:             *{strPerformance}*
"""


  elif data.info['quoteType'] == 'ETF':
      r = f"""Hey {message.from_user.first_name} {specialMsg}, here is the data that I found for the ETF:\n\n*{data.info['longName']}*
----------------------------------------------
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:               *{strPerformance}*
"""


  elif data.info['quoteType'] == 'CRYPTOCURRENCY':
      r = f"""Hey {message.from_user.first_name} {specialMsg}, here is the data that I found for the Crypto:\n\n*{data.info['shortName']}*
----------------------------------------------
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:               *{strPerformance}*
"""
  
  elif data.info['quoteType'] == 'CURRENCY':
      r = f"""Hey {message.from_user.first_name} {specialMsg}, here is the data that I found for the FOREX:\n\n*{data.info['shortName']}*
----------------------------------------------
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:               *{strPerformance}*
"""

  return r


def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]

def handleInput(data):
  if data.info['regularMarketPrice'] == None:
    return True

def handleETF(message, bot, data):
  if data.info['quoteType'] == 'ETF':
    print("-----------------------------------------")
    print("ETF")
    print("-----------------------------------------")

    if data.info['regularMarketPrice'] != None:
      replyMsg = formatMessage(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleEquity(message, bot, data):
  if data.info['quoteType'] == 'EQUITY':
    print("-----------------------------------------")
    print("STOCK")
    print("-----------------------------------------")

    if data.info['regularMarketPrice'] != None:
      replyMsg = formatMessage(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleCrypto(message, bot, data):
  if data.info['quoteType'] == 'CRYPTOCURRENCY':
    print("-----------------------------------------")
    print("CRYPTO")
    print("-----------------------------------------")

    if not handleInput(data):
      replyMsg = formatMessage(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

def handleCurrency(message, bot, data):
  if data.info['quoteType'] == 'CURRENCY':
    print("-----------------------------------------")
    print("CURRENCY")
    print("-----------------------------------------")

    if not handleInput(data):
      replyMsg = formatMessage(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')


def runBot(bot):
  @bot.message_handler(commands=['fetch'])
  def fetch_command(message):
    securities = extract_arg(message.text)
    
    if len(securities) <=0:
      bot.reply_to(message, f"Yo {message.from_user.first_name}, you have to send me stock ticker. 🙄")


    for s in securities:
      data = yf.Ticker(s)
      print(data.info)

      if handleInput(data):
        bot.reply_to(message, f"Yo {message.from_user.first_name}, I found no data available for {s}. 🤔")

      else:
        print('in handlers block')
        handleETF(message, bot, data)
        handleEquity(message, bot, data)
        handleCrypto(message, bot, data)
        handleCurrency(message, bot, data)



  bot.infinity_polling()

def stop_bot():
  env = os.environ["ENV"]
  if env == 'dev':
    print("DEV ENVIRONMENT - go crazy")
    return True
  elif env == 'prod':
    print("PROD ENVIRONMENT - be careful")
    return False


def main():
    while True:
        try:
            runBot(bot)
        except Exception(e):
            print(e)
        else:
            if stop_bot():
              break
            

if __name__ == "__main__":
  main()