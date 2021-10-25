def market_data(message, data):
  performance = calculatePerformance(data)
  strPerformance = addPerformanceEmoji(performance)
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
