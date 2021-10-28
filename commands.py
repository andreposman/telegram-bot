import logging
import telebot
import securities
import yfinance as yf
import utils.messages
import utils.calculate

def stop_bot(bot, env):
  @bot.message_handler(commands=['stop'])
  def command_stop_bot(message):

    logging.info(f'{message.from_user.username}, sent the /stop command to the bot.')
    logging.info(f'User Data: \n{message}')

    if env == 'dev' and message.from_user.username == 'andreposman':
      bot.reply_to(message, 'DEV ENVIRONMENT - Go Crazy', parse_mode='Markdown')
      return False
    elif env == 'prod' and message.from_user.username == 'andreposman':
      bot.reply_to(message, 'Be Careful - PROD ENVIRONMENT', parse_mode='Markdown')
      return True
    else:
      logging.error('an error ocurred on the command_stop_bot function.')
      bot.reply_to(message, 'an error ocurred on the command_stop_bot function.', parse_mode='Markdown')

def fetch_bot(bot):
    @bot.message_handler(commands=['fetch'])
    def fetch_command(message):

      logging.info(f'{message.from_user.username}, sent the /fetch command to the bot.')
      logging.info(f'User Data: \n{message}')

      asset = extract_user_input(message.text)

      if validate_user_input(asset):
        logging.info(f'{message.from_user.username}. User sent an empty command: {asset}')
        bot.reply_to(message, f"Yo {message.from_user.first_name}, you have to send me a ticker. 🙄")


      for a in asset:
        data = yf.Ticker(a)
        logging.info(f'Data found was: \n{data.info}')

        if is_asset_valid(data):
          securities.handle_assets(message, bot, data)

        else:
          logging.info(f'{message.from_user.username}. No data available found for: {a}')
          bot.reply_to(message, f"Yo {message.from_user.first_name}, I found no data available for {a}. 🤔")

def helper_bot(bot):
  @bot.message_handler(commands=['help'])
  def help_command(message):

    logging.info(f'{message.from_user.username}, sent the /help command to the bot.')
    logging.info(f'User Data: \n{message}')

    helpMsg = f'''
    Hi {message.from_user.first_name} 👋, this is how to use me, I have the following commands:

    /greet: I will say Hi to you.
    /fetch: This is where the magic happens, I fetch data for the ticker that you send me.
    -----
    Examples: 
        /fetch ^BVSP - fetch data from Indexes, in this case Bovespa
        /fetch B3SA3.SA - fetch data from B3 in the Brazilian market
        /fetch AAPL - fetch data for Apple stock
        /fetch VT - fetch data for the ETF VT
        /fetch BTC-USD - fetch data for Bitcoin
        /fetch USDBRL=X - fetch data for the FOREX pair USD/BRL    
        /fetch CL=F - fetch data from the future market, in this case is Crude Oil
        
        You can also fetch mutiple assets in one line:
        /fetch aapl vt btc-usd usdbrl=x cl=f b3sa3.sa ^bvsp

        If you don't know the ticker of the asset that you want you can search it on https://finance.yahoo.com thats where I fetch it from.
    '''

    bot.reply_to(message, helpMsg, parse_mode='Markdown')

def greet_bot(bot):
  @bot.message_handler(commands=['greet'])
  def greet_command(message):

    logging.info(f'{message.from_user.username}, sent the /greet command to the bot.')
    logging.info(f'User Data: \n{message}')

    if message.from_user.username == 'andreposman':
      bot.reply_to(message, 'Olá Mestre, Vai Palmeiras!')

    elif message.from_user.username == 'raafvargas':
      bot.reply_to(message, f'👋 {message.from_user.first_name}, Spec em PHP!')

    elif message.from_user.first_name == 'Matheus Luis':
      bot.reply_to(message, f'👋 {message.from_user.first_name}, Rei do Spring!')

    else:
      bot.reply_to(message, f'Olá {message.from_user.first_name} 👋')


def validate_user_input(asset):
        if len(asset) <=0:
          return True
        else:
          return False
          

def is_asset_valid(data):
        if data.info['regularMarketPrice'] != None:
          return True
        else:
          return False
        

def extract_user_input(arg):
  print(arg.split()[1:])
  return arg.split()[1:]