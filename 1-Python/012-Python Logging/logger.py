## configuring logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)