import logging

log_format = '%(filename)s %(funcName)s %(asctime)s %(message)s'
log_filename = "logging_test.log"
logging.basicConfig(filename=log_filename, format=log_format, datefmt='%Y-%m-%d %H:%M:%S:%S %p', filemode='w', level=logging.INFO)
if __name__ == '__main__':
     logger = logging.getLogger(__name__)
     logger.info("this is a")

