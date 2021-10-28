import utils.calculate
import utils.messages


def handle_assets(message, bot, data):
    print("-----------------------------------------")
    print(data.info['quoteType'])
    print("-----------------------------------------")

    try:
      replyMsg = utils.messages.others(message, data)
      bot.reply_to(message, replyMsg, parse_mode='Markdown')

    except Exception as e:
      logging.critical("Error: ", e)
      replyMsg = '*Error fetching data*'
      bot.reply_to(message, replyMsg, parse_mode='Markdown')
