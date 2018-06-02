import logging 
import os
import logging.handlers


file_path=os.path.join(r'C:\Users\пользователь\Desktop','information.log')
format=logging.Formatter("%(asctime)s %(levelname)-10s %(module)-10s %(funcName)-10s %(message)s")
server_logger = logging.getLogger('server')
server_handler = logging.handlers.TimedRotatingFileHandler(r'C:\Users\пользователь\Desktop\Python 2\information.log','d')
server_handler.setFormatter(format)
server_logger.addHandler(server_handler)
server_logger.setLevel(logging.INFO)