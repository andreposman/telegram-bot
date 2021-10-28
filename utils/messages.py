import utils.calculate
import logging

def format_asset(message, data):
  performance =  utils.calculate.one_day_performance(data)
  performance_output = add_performance_emoji(performance)
  specialMsg = ' '
  name_output = ''

  format_data_output(data, performance_output, name_output)
    
  r = f'''{message.from_user.first_name}{specialMsg}, here it is:\n*{name_output}*
  \n\n
  Type:                   *{data.info['quoteType']}*
  Symbol:               *{data.info['symbol']}*
  Current Price:             *{data.info['regularMarketPrice']}*
  Performance:               *{performance_output}*
  '''

  logging.info(r)
  
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

def format_data_output(data, strPerformance, name_output):
  if data.info['longName'] == None or data.info['longName'] == '' or not 'longName' in data.keys():
    name_output = data.info['shortName']
  
  elif data.info['longName'] != None or data.info['longName'] != '' or 'longName' in data.keys():
    name_output = data.info['longName']
  
  elif data.info['shortName'] == None or data.info['shortName'] == '':
    data.info['shortName'] = data.info['symbol']
  
  elif data.info['regularMarketPrice'] == None or data.info['regularMarketPrice'] == '':
    data.info['regularMarketPrice'] = 'Price error'
  
  elif performance_output == None or performance_output== '':
    performance_output = 'Performance error'
  
  elif data.info['quoteType'] != 'INDEX':
    '$' + data.info['regularMarketPrice']
  