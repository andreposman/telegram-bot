import utils.calculate

def market_data(message, data):
  performance =  utils.calculate.one_day_performance(data)
  strPerformance = add_performance_emoji(performance)
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
      r = f"""Hey {message.from_user.first_name} from module {specialMsg}, here is the data that I found for the FOREX:\n\n*{data.info['shortName']}*
----------------------------------------------
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:               *{strPerformance}*
"""

  return r





def add_performance_emoji(performance):
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