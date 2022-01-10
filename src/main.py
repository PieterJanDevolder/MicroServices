from Lib.Log import logger
from Lib.Master import Master
import time


print("hi world")
Version = '1.0.0'



if __name__ == '__main__':
     logger.info('Application V%s is starting up' % (Version))

     tt = Master('MasterAbc')

     while True:
          logger.info("Endless Loop")
          time.sleep(5)
    # Create two threads as follows