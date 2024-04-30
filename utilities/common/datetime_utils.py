from datetime import datetime, timedelta
from string import Formatter
import logging

def get_date_list(start_end):
    """This function converts an input list of [start_date, end_date] and returns a list containing all individual dates between the given range.

    Args:
        dates (List): List of [start_date, end_date] as String in the format: "%Y-%m-%d"
    Returns:
        List: List of [date1, date2, ..., dateX] as String in the format: "%Y-%m-%d"
    """
    logger = logging.getLogger("__main__"+"."+__name__)
    logger.debug(f"Getting date list from: {start_end}")
    start_end = [datetime.strptime(date, "%Y-%m-%d") for date in start_end]
    date_list = [(start_end[0] + timedelta(days=x)).strftime("%Y-%m-%d") for x in range((start_end[-1]-start_end[0]).days + 1)]
    return date_list

def round_to_x_mins(dt, x):
    """Function to round up the given datetime object to the previous x minutes.

    Args:
        dt (datetime.datetime object): Given datetime object to be rounded to.
        x (Integer): _description_

    Returns:
        datetime.datetime object: Datetime object rounded to previous x minutes.
    """
    logger = logging.getLogger("__main__"+"."+__name__)
    if (x < 0) or (x > 60):
        logger.critical(f"Given minute to round to is not valid.")
        return
    if isinstance(dt, datetime):
        round_minute = dt.minute - (dt.minute % x)
        return (datetime(dt.year, dt.month, dt.day,
                                dt.hour, round_minute, 0, 0))
    else:
        logger.critical("Input time is not a valid datetime object.")
        return

def strfdelta(tdelta, fmt='{D:02}d {H:02}h {M:02}m {S:02}s', inputtype='timedelta'):
    """Convert a datetime.timedelta object or a regular number to a custom-formatted string, just like the stftime() method does for datetime.datetime objects.

    The fmt argument allows custom formatting to be specified.  Fields can include seconds, minutes, hours, days, and weeks.  Each field is optional.

    Some examples:
        '{D:02}d {H:02}h {M:02}m {S:02}s' --> '05d 08h 04m 02s' (default)
        '{W}w {D}d {H}:{M:02}:{S:02}'     --> '4w 5d 8:04:02'
        '{D:2}d {H:2}:{M:02}:{S:02}'      --> ' 5d  8:04:02'
        '{H}h {S}s'                       --> '72h 800s'

    The inputtype argument allows tdelta to be a regular number instead of the  default, which is a datetime.timedelta object.  Valid inputtype strings: 
        's', 'seconds', 
        'm', 'minutes', 
        'h', 'hours', 
        'd', 'days', 
        'w', 'weeks'
    """

    # Convert tdelta to integer seconds.
    if inputtype == 'timedelta':
        remainder = int(tdelta.total_seconds())
    elif inputtype in ['s', 'seconds']:
        remainder = int(tdelta)
    elif inputtype in ['m', 'minutes']:
        remainder = int(tdelta)*60
    elif inputtype in ['h', 'hours']:
        remainder = int(tdelta)*3600
    elif inputtype in ['d', 'days']:
        remainder = int(tdelta)*86400
    elif inputtype in ['w', 'weeks']:
        remainder = int(tdelta)*604800

    f = Formatter()
    desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
    possible_fields = ('W', 'D', 'H', 'M', 'S')
    constants = {'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
    values = {}
    for field in possible_fields:
        if field in desired_fields and field in constants:
            values[field], remainder = divmod(remainder, constants[field])
    return f.format(fmt, **values)