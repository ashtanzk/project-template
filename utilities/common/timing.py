import atexit
from datetime import datetime
from utilities.common.datetime_utils import strfdelta
import logging

logger = logging.getLogger("__main__")
start = datetime.now()

def startProgram():
    atexit.register(endlog)
    log("Start Program")

def secondsToStr(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return strfdelta(elapsed.total_seconds(), inputtype='s')

def log(s, elapsed=None):
    line = "="*40
    logger.info(line)
    logger.info(s)
    if elapsed:
        logger.info("Elapsed time: " + elapsed)
    logger.info(line)

def endlog():
    end = datetime.now()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

