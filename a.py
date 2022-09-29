import argparse
import logging
import time

def comprehend_not():
  squares = []
  for i in range(10):
    squares.append(i*i)
  logging.debug(squares)
  
def comprehend_yes():
  squares = [i*i for i in range(10)]
  logging.debug(squares)

def enumerate_this():
  l = ["a","b","c"]
  for i, x in enumerate(l):
    logging.debug(f"{i}:{x}")
    
def sorted_complex():
  data = [{"name": "Max", "age": 6},
          {"name": "Lisa", "age": 20},
          {"name": "Ben", "age": 9}]
  sorted_data = sorted(data, key=lambda x: x["age"])
  logging.debug(sorted_data)
  
def handleCmdLineRequestedLogLevel(args):
  '''
  Handles the cmd line requested log level
  If none was requested, default to logging.INFO
  This function follows a pattern in the logging source code to address setting via name vs numeric
  '''
  requestedLogLevel = str.upper(args.log) if args.log is not None else logging.INFO
  result = logging._levelToName.get(requestedLogLevel)
  if result is not None:
      print(f"Logging set to {result}")
      return result
  else:
    result = logging._nameToLevel.get(requestedLogLevel)
    if result is not None:
      print(f"Logging set to {logging.getLevelName(result)}")
      return result
    else:
      raise ValueError(f'Invalid log level: {args.log}')   
    
def setupLogging():
  parser = argparse.ArgumentParser(usage="usage msg")
  parser.add_argument("-l", "--log", help = "Set Log level, must be one of the Python logging levels")
  args = parser.parse_args()
  level = handleCmdLineRequestedLogLevel(args)
  #fmt = '%(filename)s:%(lineno)d [%(levelname)s] %(asctime)s - %(message)s'
  fmt = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
  logging.basicConfig(level=level, format=fmt)
  logging.info('Started')
    
def main():
  setupLogging()
  start = time.perf_counter()
  sorted_complex()
  end = time.perf_counter()
  logging.info(f"Ended   {end-start}")
  
if __name__ == "__main__":
  main()
