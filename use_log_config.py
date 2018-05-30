import logging
import log_config



log = logging.getLogger('messanger')

def main():
    log.info('Information')
    log.warning('Warning')
    log.critical('Critical')

if __name__=='__main__':
    main()


