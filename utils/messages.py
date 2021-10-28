import utils.calculate
import logging

def format_asset(message, data):
  specialMsg = ' '
  name_output = ''
  price_output = str(data.info['regularMarketPrice'])
  performance =  utils.calculate.one_day_performance(data)
  performance_output = add_performance_emoji(performance)

  if data.info['quoteType'] == 'EQUITY' or data.info['quoteType'] == 'ETF':
    name_output = data.info['longName']
  else:
    name_output = data.info['shortName']


  format_data_output(data, performance_output, name_output, price_output)
    
  r = f'''  {message.from_user.first_name}{specialMsg}, here it is:\n\n *{name_output}*
  ------------------------------------
  Type:                   *{data.info['quoteType']}*
  Symbol:                 *{data.info['symbol']}*
  Current Price:             *${price_output}*
  Performance:               *{performance_output}*
  '''

  logging.info(r)
  
  return r


def add_performance_emoji(performance):
  performance_string = ''
  emojiSuffix = ''

  if performance < 0:
    emojiSuffix = '🔻'
    if performance < -10:
      emojiSuffix = '⚰️'

  elif performance > 0:
    performance_string = ' +'
    emojiSuffix = '👍'
    if performance > 10: 
      emojiSuffix = '🚀💰'

  performance_string = performance_string + str(performance) + '% ' + emojiSuffix

  return performance_string

def format_data_output(data, performance_output, name_output, price_output):
  if data.info['shortName'] == None or data.info['shortName'] == '':
    data.info['shortName'] = data.info['symbol']
  
  elif data.info['regularMarketPrice'] == None or data.info['regularMarketPrice'] == '':
    data.info['regularMarketPrice'] = 'Price error'
  
  elif performance_output == None or performance_output== '':
    performance_output = 'Performance error'
  
  elif data.info['quoteType'] != 'INDEX':
    price_output = '$' + str(data.info['regularMarketPrice'])
  