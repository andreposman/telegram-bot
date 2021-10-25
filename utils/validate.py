
def data_has_price(data):
  if data.info['regularMarketPrice'] == None:
    return False


def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]