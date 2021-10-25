import telebot

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


def help_bot(bot):
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

