import telebot

@bot.message_handler(commands=['stop'])
def stop_bot(message, bot, env):
  print(message)
  if env == 'dev' and message.from_user.username == 'andreposman':
    bot.reply_to(message, "DEV ENVIRONMENT - Go Crazy", parse_mode='Markdown')
    return False
  elif env == 'prod' and message.from_user.username == 'andreposman':
    bot.reply_to(message, "`Be Careful - PROD ENVIRONMENT`", parse_mode='Markdown')
    return True
  else:
    bot.reply_to(message, "`DEU RUIM`", parse_mode='Markdown')


