import logging
from logging.handlers import RotatingFileHandler

LOGFILE = "../bot.log"

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Avoid adding handlers multiple times

    logger.setLevel(logging.INFO)

    # Save logs to a file (bot.log)
    handler = RotatingFileHandler(LOGFILE, maxBytes=5_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also show logs in the console
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
