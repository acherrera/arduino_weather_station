def get_start(item, default):
    """
    :param item: String name of item to set: e.g. "Year" or "Day"
    :param default: Default value for item to take
    :return: Returns integer of input or default value

    Typical implementation for variables shown below. Pass current values as the default.

    import datetime
    import time

    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S').split('-')

    year_current = current_time[0]
    month_current = current_time[1]
    day_current = current_time[2]
    hour_current = current_time[3]
    minute_current = 0 # no one is going to be this specific
    second_current = 0 # Not going to be this specific probably

    """
    try:
        output = int(input("\nEnter start {}: ".format(item)))
    except ValueError:
        print("Assuming current {}: {}".format(item, default))
        output = default
    return output
