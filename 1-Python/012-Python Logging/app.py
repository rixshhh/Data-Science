from logger import logging

logger=logging.getLogger('Arithmetic-App')

def add(a,b):
    result=a+b
    logger.debug(f' Adding {a} + {b} = {result}')
    return result

def sub(a,b):
    result=a-b
    logger.debug(f' Substracting {a} - {b} = {result}')
    return result

def mul(a,b):
    result=a*b
    logger.debug(f' Adding {a} * {b} = {result}')
    return result

def div(a,b):
    try:
        result=a/b
        logger.debug(f' Adding {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by ZeroError')
        return None


add(50,20)
sub(10,5)
mul(15,5)
div(65,4)
