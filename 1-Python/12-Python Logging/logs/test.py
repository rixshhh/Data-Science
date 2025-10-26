from logger import logging

def add(a,b):
    logging.debug('The Addition Operation is taking place.')
    return a+b

logging.debug("The Addition functions is called.")
add(5,5)