"""
FOR FINAL AND FRAMEWORK FUNCTIONS ONLY. Use temp.py to test new functions.
"""

import datetime
import time


# TODO expand the get_start so the it does it all on its own
# TODO see temp.py for better method to get current time


def get_start():
    """
    :param item: String name of item to set: e.g. "Year" or "Day"
    :param default: Default value for item to take
    :return: Returns integer of input or default value
    """

    def get_data(item, default):
        """
        Used to get all the data later, but no where else. So... function in a function
        """
        try:
            output = int(input("\nEnter start {}: ".format(item)))
        except ValueError:
            print("Assuming current {}: {}".format(item, default))
            output = default
        return output

    # Get the current time
    current_time = datetime.datetime.fromtimestamp(time.time())

    # Use  the current time to set the year and such.
    # Unfortunately have to do this due to an issue with the seconds and having to rebuild datetime and compare later
    year_current = int(current_time.year)
    month_current = int(current_time.month)
    day_current = int(current_time.day)
    hour_current = int(current_time.hour)
    minute_current = int(current_time.minute)

    # Get the start time information
    year_start = get_data("Year", year_current)
    month_start = get_data("Month", month_current)
    day_start = get_data("Day", day_current)
    hour_start = get_data("Hour", hour_current)
    minute_start = get_data("Minute", minute_current)
    second_start = 0

    # Have to rebuild the current time. Otherwrise, the second would not match due to the method in which the
    # current time is got, the second don't match.... maddeningly.
    current_time = datetime.datetime(year_current, month_current, day_current, hour_current,
                                     minute_current, 0)

    # Build the datetime object for the current time
    start_time = datetime.datetime(year_start, month_start, day_start, hour_start,
                                   minute_start, 0)

    # if the two times do match, set start to time way back. Could also use a boolean and check that
    if current_time == start_time:
        print("\nGraphing All Data")
        start_time = datetime.datetime(2000, 1, 1, 1, 1, 1)

    return start_time
