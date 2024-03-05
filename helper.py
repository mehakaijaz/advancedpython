import logging
"""import logging.config
logging.config.fileConfig('logging.conf')

logger=logging.getLogger(__name__)
#logger.propagate=False
#logger.info('hello from helper module')

#create handler 
stream_h=logging.StreamHandler()
file_h=logging.FileHandler('file.log')

#level amd format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s - %(levelname)s -%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("warned")
logger.error('errored')"""
import traceback
try:
    a=[1,2,3]
    val=a[4]
#except IndexError as e:
    #logging.error(e , exc_info=True)
except:
    logging.error('the error is %s', traceback.format_exc())
    
#rotating file handler
from logging.handlers import RotatingFileHandler
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2kb and keep backup logs app.log.1 , app.log.2
handler=RotatingFileHandler('app.log',maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(1000):
 logger.info('hello world')
 
#timedrotating file handler
from logging.handlers import TimedRotatingFileHandler
import time
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2kb and keep backup logs app.log.1 , app.log.2
handler=TimedRotatingFileHandler('timed_test.log',when='m',interval=1, backupCount=2)
logger.addHandler(handler)

for _ in range(1000):
 logger.info('hello world!!!')
 time.sleep(5)