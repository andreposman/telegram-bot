def one_day_performance(data):
  closePrice = data.info['regularMarketPreviousClose']
  currentPrice = data.info['regularMarketPrice']
  performance = round((((currentPrice - closePrice)/currentPrice)*100), 2)

  return performance
