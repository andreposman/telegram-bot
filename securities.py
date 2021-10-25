import utils.calculate
import utils.messages

def handle_others(message, bot, data):
  if data.info['quoteType'] != 'CURRENCY' and data.info['quoteType'] != 'ETF' and data.info['quoteType'] != 'EQUITY' and data.info['quoteType'] != 'CRYPTOCURRENCY':
    quoteType = data.info['quoteType']
    print("-----------------------------------------")
    print(quoteType)
    print("-----------------------------------------")

    if not utils.validate.data_has_price(data):
      replyMsg = utils.messages.others(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
    else:
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
