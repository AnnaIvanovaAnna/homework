import logging 
import os

logging.basicConfig(
    filename =os.path.join(r'C:\Users\пользователь\Desktop','information.log'),
    format = "%(asctime)s %(levelname)-10s %(module)-10s %(funcName)-10s %(message)s",
    level = logging.INFO
)



