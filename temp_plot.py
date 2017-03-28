"""
Created by Anthony Herrera to analyze Arduino weather station data.

This is just made to plot the temperature variable

"""

from modules.functions import get_start, get_data, data_start
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

the_file = 'datasets/testing_data/20170325_Response_Testing.TXT'

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(the_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(the_file, start_time)

if len(time) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()

# With data, create save path and title to give the functions
save_path = "{}_temperature.png".format(the_file.split('.')[0])
title_string = 'Temperature for: {}'.format(the_file.split('.')[0].split('/')[2])

# This is the makes the three plots

fig = plt.figure()
ax1 = plt.subplot(1, 1, 1)

ax1.plot(time, temperature)
plt.title(title_string)
plt.xlabel('time')
plt.ylabel('temperature (C)')

xfmt = mdate.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()

plt.savefig(save_path)
plt.show()


""" Variables used in main program to plot
three_plots(x=time,
            y1=temperature,
            y2=pressure,
            y3=rel_hum,
            title=title,
            xlabel='time',
            ylabel1='Temperature (C)',
            ylabel2='Pressure (hPa)',
            ylabel3='RH (%)',
            save_file=save_path)
"""
