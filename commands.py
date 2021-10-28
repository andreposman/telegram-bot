import telebot
import securities
import yfinance as yf
import utils.validate
import utils.messages
import utils.calculate

def stop_bot(bot, env):
  @bot.message_handler(commands=['stop'])
  def command_stop_bot(message):
    print(message)
    if env == 'dev' and message.from_user.username == 'andreposman':
      bot.reply_to(message, "DEV ENVIRONMENT - Go Crazy", parse_mode='Markdown')
      return False
    elif env == 'prod' and message.from_user.username == 'andreposman':
      bot.reply_to(message, "`Be Careful - PROD ENVIRONMENT`", parse_mode='Markdown')
      return True
    else:
      bot.reply_to(message, "`DEU RUIM`", parse_mode='Markdown')

def fetch_bot(bot):
    @bot.message_handler(commands=['fetch'])
    def fetch_command(message):

      asset = extract_user_input(message.text)

      if validate_user_input(asset):
        bot.reply_to(message, f"Yo {message.from_user.first_name}, you have to send me stock ticker. 🙄")

      
      for a in asset:
        data = yf.Ticker(a)
        print(data.info)

        if is_asset_valid(data):
          print('in handlers block')
          securities.handle_assets(message, bot, data)

        else:
          bot.reply_to(message, f"Yo {message.from_user.first_name}, I found no data available for {a}. 🤔")


def helper(bot):
  @bot.message_handler(commands=['help'])
  def help_command(message):
    print(message)
    helpMsg = f"""
    Hi {message.from_user.first_name} 👋, this is how to use me, I have the following commands:

    /greet: I will say Hi to you.
    /fetch: This is where the magic happens, I will fetch USA Market data for the ticker that you send me.

    Examples: 
        /fetch AAPL - fetch data for Apple stock
        /fetch VT - fetch data for the ETF VT
        /fetch BTC-USD - fetch data for Bitcoin
        /fetch USDBRL=X - fetch data for the FOREX pair USD/BRL    
        /fetch CL=F - fetch data from the future market, in this case is Crude Oil
        
        You can also fetch mutiple assets in one line:
        /fetch aapl vt btc-usd usdbrl=x cl=f
    """
    bot.reply_to(message, helpMsg, parse_mode='Markdown')

def greet(bot):
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



def extract_user_input(arg):
  print(arg.split()[1:])
  return arg.split()[1:]

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
        
