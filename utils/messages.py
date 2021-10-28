import utils.calculate
import logging

def others(message, data):
  performance =  utils.calculate.one_day_performance(data)
  strPerformance = add_performance_emoji(performance)
  specialMsg = ' '
  quoteType = data.info['quoteType']

  if data.info['shortName'] == None or data.info['shortName'] == '':
    data.info['shortName'] = data.info['symbol']
  elif data.info['regularMarketPrice'] == None or data.info['regularMarketPrice'] == '':
    data.info['regularMarketPrice'] = 'Price error'
  elif strPerformance == None or strPerformance== '':
    strPerformance = 'Performance error'
    
  r = f"""Hey {message.from_user.first_name}{specialMsg}, here is the data that I found for:\n\n*{data.info['shortName']}*
----------------------------------------------
Symbol:               *{data.info['symbol']}*
Current Price:             *${data.info['regularMarketPrice']}*
Performance:               *{strPerformance}*
"""
  print(r)
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

  return strPerformance