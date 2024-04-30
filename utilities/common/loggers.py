import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

from utilities.common.datetime_utils import round_to_x_mins

def create_logger(logger_name):
    """Custom function that automatically creates and configures the logger object called '__main__'

    Args:
        logger_name (String): Name to be passed as logFileName

    Returns:
        Logger object: Returns a Logger object with the standard log stream and file formatting. Log files are automatically created in a directory "logs" every 15 minutes.
    """
    # Create logger object
    logger = logging.getLogger('__main__')
    
    # Create logging handlers
    c_handler = logging.StreamHandler()
    logPath = "../logs"
    # logFileDatetime = f"{datetime.now().strftime('%Y-%m-%d_%H%MH')}"
    logFileDatetime = f"{round_to_x_mins(datetime.now(), 15).strftime('%Y-%m-%d_%H%MH')}"
    logFileName = f"{logger_name}.log"
    f_handler = RotatingFileHandler(f"{logPath}/{logFileDatetime}_{logFileName}")

    # Set logging handler levels
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)

    # Create logging formatters and add to handlers
    c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    f_handler.setFormatter(f_format)

    # Add handlers to custom logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger