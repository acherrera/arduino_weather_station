"""
FOR FINAL AND FRAMEWORK FUNCTIONS ONLY. Use temp.py to test new functions.
This file contains helpers for the main file. Make main file cleaner and allows these parts to be
used elsewhere without issue.
"""

import datetime
import numpy as np


# TODO expand the get_start so the it does it all on its own
# TODO see test.py for better method to get current time

def data_start(fileName, lines_scanned):
    """
    Get the starting time of the data without loading all the data
    :param fileName: path to file
    :param lines_scanned: number of lines to scan. If errors occuring, check for large comments and headers
    :return: returns a compacted date_time string
    """
    with open(fileName) as f:
        # Gets top 20 lines to look for first non-comment line
        top = [next(f) for x in range(lines_scanned)]

    for line in top:
        # Take out first line that is not a comment or new line
        if line.startswith('#') or line == '\n':
            pass
        else:
            sample_line = line
            break

    # The first element of the CSV variable is the time. Returns a string
    return sample_line.split(',')[0]


def get_start(data_start_time):
    """
    This will ask the user for the time they want the graph the start. If nothing is entered - will assume
    start of data as start of graph. Use to get rid of transient temperature change - for example, when the
    sensor is place outside after being inside for a long period of time.

    :param data_start_time: data start as found by data_start() function
    :return: returns the time that the graph should start according to user input as datetime object
    """

    # This is ugly because the datetime is passed as string.
    year_data_start = int(data_start_time[0:4])
    month_data_start = int(data_start_time[4:6])
    day_data_start = int(data_start_time[6:8])
    hour_data_start = int(data_start_time[9:11])
    minute_data_start = int(data_start_time[11:13])


    def get_data(item, default):
        """
        Helper function that is used to get all the starting times below
        :param item:
        :param default:
        :return:
        """
        try:
            output = int(input("\nEnter start {}: ".format(item)))
        except ValueError:
            print("Assuming data start {}: {}".format(item, default))
            output = default
        return output

    # See if user even wants to enter data start time
    custom_start = input('Would you like to enter custom start time? [Y/n]')

    if str.upper(custom_start) == 'Y':
        custom_start = True
    else:
        custom_start = False


    if custom_start == True:
        # Get the start time information use get_data defined above
        year_start = get_data("Year", year_data_start)
        month_start = get_data("Month", month_data_start)
        day_start = get_data("Day", day_data_start)
        hour_start = get_data("Hour", hour_data_start)
        minute_start = get_data("Minute", minute_data_start)

        # Build the datetime object for the current time
        start_time = datetime.datetime(year_start, month_start, day_start, hour_start,
                                   minute_start, 0)
    else:
        start_time = datetime.datetime(year_data_start, month_data_start, day_data_start,
                                        hour_data_start, minute_data_start, 0)

    return start_time


def get_data(filepath, start_time):
    """
    Function that actually gets the data and returns the lists of data to be plotted later

    :param filepath: String of path to file.
    :param start_time: Time to start the graph. Use get_start to find this value
    :return: reutns time, temperature, pressure, relative humidity as large lists
    """
    with open(filepath) as f:
        data = f.readlines()

    time_list = []
    temperature_list = []
    pressure_list = []
    rel_hum_list = []

    # Sea Level Correction
    elevation = 288  # m
    gravity = 9.80665  # m/s^2
    R = 287

    def to_kelvin(T):
        return T + 273.15

    for line in data:
        # Ignores comments or new lines
        if line.startswith('#') or line == '\n':
            pass
        else:
            time_data = str(line.split(',')[0])
            year = int(time_data[0:4])
            month = int(time_data[4:6])
            day = int(time_data[6:8])
            hour = int(time_data[9:11])
            minute = int(time_data[11:13])
            second = int(time_data[13:15])

            in_time = datetime.datetime(year, month, day, hour, minute, second)
            # These are datetime object comparison
            if in_time > start_time:
                time_list.append(in_time)
                temperature = float(line.split(',')[1])
                temperature_list.append(temperature)
                input_pressure = float(line.split(',')[2])
                corrected_pressure = input_pressure * np.exp((elevation * gravity) / (R * to_kelvin(temperature)))
                pressure_list.append(corrected_pressure)
                rel_hum_list.append(float(line.split(',')[3]))

    return time_list, temperature_list, pressure_list, rel_hum_list
