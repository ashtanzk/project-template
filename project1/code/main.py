import logging
import argparse
import time
import sys
sys.path.append("../../")
from utilities.common import timing
from utilities.common.datetime_utils import get_date_list
from utilities.common.loggers import create_logger

def main():
    # Create custom logger
    logger = create_logger("TESTING-UTIL-LOGGERS")

    # Create argparse parser
    argparser = argparse.ArgumentParser()

    # Add argument
    args = argparser.add_argument('--debug', action="store_const", dest="logLevel", const=logging.DEBUG, default=logging.INFO, help="Sets the logging level to DEBUG. If not specified, defaults to INFO.")
    args = argparser.add_argument('--date', type=str, nargs="+", required=True, help="The START_DATE and END_DATE of data to be read formatted as 'YYYY-MM-DD'. END_DATE is optional if planning to read just one day of data.")
    args = argparser.add_argument('--mask', action="store_true", help="Sets mask to True for masking sensitive information within the data. If not specified, defaults to False.")
    args = argparser.parse_args()

    # Set logging level for custom logger
    logger.setLevel(args.logLevel)
    logger.info(f"Log level {logging.getLevelName(logger.getEffectiveLevel())} is set.")
    
    timing.startProgram()

    # Getting argument values
    start_end = args.date
    date_list = get_date_list(start_end)

    logger.info(f"{' to '.join(start_end)} selected.")
    logger.info(f"Reading data from {date_list}.")
    logger.info(f"Mask is set to {args.mask}")
    for i in range(20):
        logger.debug(i)
    return

if __name__ == "__main__":
    main()