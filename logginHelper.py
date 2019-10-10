import logging
import logging.handlers

log = logging.getLogger('snowdeer_log')
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s] (%(filename)s:%(lineno)d)  %(message)s')

# fileHandler = logging.FileHandler('./log.txt')
log_max_size = 10 * 1024 * 1024
log_file_count = 20
fileHandler = logging.handlers.RotatingFileHandler(filename='./log.txt', maxBytes=log_max_size,
                                                   backupCount=log_file_count)
streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

log.addHandler(fileHandler)
log.addHandler(streamHandler)

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')