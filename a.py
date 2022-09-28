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
  
def main():  
  parser = argparse.ArgumentParser(usage="usage msg")
  parser.add_argument("-l", "--log", help = "Set Log level")
  args = parser.parse_args()
  
  # Handle Logging Level from Command Line
  level = logging.getLevelName(str.upper(args.log)) if (args.log is not None) else logging.INFO
  print(f"Logging set to {logging.getLevelName(level)}")
    
    #if args.log in [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]:
    #  level = args.log
    #else:
    #  raise ValueError(f'Invalid log level: {args.log}')   
    
  #fmt = '%(filename)s:%(lineno)d [%(levelname)s] %(asctime)s - %(message)s'
  fmt = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
  logging.basicConfig(level=level, format=fmt)
  logging.info('Started')
  start = time.perf_counter()
  #print(f'{logging.__dict__["ERROR"]}')
  sorted_complex()
  end = time.perf_counter()
  logging.info(f"Ended   {end-start}")
  
if __name__ == "__main__":
  main()
